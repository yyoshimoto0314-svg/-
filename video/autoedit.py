#!/usr/bin/env python3
"""動画自動編集エンジン（動画編集部門）

ffmpeg だけで動く。PyYAML があれば config/brand.yaml の video 設定を既定値に使う。

使い方:
  python3 video/autoedit.py probe       <動画>
  python3 video/autoedit.py cut-silence <入力> <出力> [--threshold-db -35] [--min-silence 0.6] [--padding 0.15]
  python3 video/autoedit.py subtitles   <入力> <字幕.srt> <出力> [--font-size 64]
  python3 video/autoedit.py bgm         <入力> <BGM> <出力> [--volume 0.15]
  python3 video/autoedit.py vertical    <入力> <出力> [--mode blur|crop]
  python3 video/autoedit.py thumbnail   <入力> <出力.png> --text "タイトル" [--at 1.0]
  python3 video/autoedit.py from-srt    <字幕.srt> <出力> [--background 画像|#色] [--size 1080x1920]
  python3 video/autoedit.py transcribe  <入力> <出力.srt>   ※ faster-whisper が必要
  python3 video/autoedit.py run         <ジョブ.json>
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND_FILE = ROOT / "config" / "brand.yaml"

DEFAULTS = {
    "font": "IPAGothic",
    "font_size": 80,
    "bgm_volume": 0.15,
    "threshold_db": -35.0,
    "min_silence_sec": 0.6,
    "padding_sec": 0.15,
}


def load_defaults() -> dict:
    d = dict(DEFAULTS)
    try:
        import yaml  # type: ignore

        video = (yaml.safe_load(BRAND_FILE.read_text(encoding="utf-8")) or {}).get("video", {})
    except Exception:
        return d
    subs = video.get("subtitles", {})
    silence = video.get("silence", {})
    d["font"] = subs.get("font", d["font"])
    d["font_size"] = subs.get("font_size", d["font_size"])
    d["bgm_volume"] = video.get("bgm_volume", d["bgm_volume"])
    d["threshold_db"] = silence.get("threshold_db", d["threshold_db"])
    d["min_silence_sec"] = silence.get("min_silence_sec", d["min_silence_sec"])
    d["padding_sec"] = silence.get("padding_sec", d["padding_sec"])
    return d


CFG = load_defaults()


# ---------------------------------------------------------------- ffmpeg 共通

def run(cmd: list[str]) -> subprocess.CompletedProcess:
    print("$ " + " ".join(str(c) for c in cmd), file=sys.stderr)
    proc = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr[-3000:])
        raise SystemExit(f"コマンドが失敗しました（exit {proc.returncode}）")
    return proc


def ffmpeg(*args) -> None:
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *args])


def probe(path: str | Path) -> dict:
    out = run([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration:stream=codec_type,width,height", "-of", "json", path,
    ]).stdout
    data = json.loads(out)
    video = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    return {
        "duration": float(data["format"]["duration"]),
        "width": video["width"] if video else None,
        "height": video["height"] if video else None,
        "has_audio": any(s["codec_type"] == "audio" for s in data["streams"]),
    }


ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p"]
AENC = ["-c:a", "aac", "-b:a", "192k"]


# ---------------------------------------------------------------- 無音カット

def detect_silences(src: str, threshold_db: float, min_silence: float) -> list[tuple[float, float]]:
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", src, "-af",
         f"silencedetect=noise={threshold_db}dB:d={min_silence}", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", proc.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: (-?[\d.]+)", proc.stderr)]
    return list(zip(starts, ends + [None] * (len(starts) - len(ends))))  # type: ignore[arg-type]


def keep_segments(silences, duration: float, padding: float) -> list[tuple[float, float]]:
    keeps, cursor = [], 0.0
    for start, end in silences:
        end = duration if end is None else end
        seg_end = min(duration, start + padding)
        if seg_end - cursor > 0.05:
            keeps.append((cursor, seg_end))
        cursor = max(cursor, end - padding)
    if duration - cursor > 0.05:
        keeps.append((cursor, duration))
    return keeps


def cut_silence(src, dst, threshold_db=None, min_silence=None, padding=None) -> dict:
    threshold_db = CFG["threshold_db"] if threshold_db is None else threshold_db
    min_silence = CFG["min_silence_sec"] if min_silence is None else min_silence
    padding = CFG["padding_sec"] if padding is None else padding
    info = probe(src)
    if not info["has_audio"]:
        raise SystemExit("無音カットには音声トラックが必要です")
    keeps = keep_segments(detect_silences(src, threshold_db, min_silence), info["duration"], padding)
    if not keeps:
        raise SystemExit("音声がすべて無音と判定されました。--threshold-db を下げてください")

    parts, labels = [], []
    for i, (s, e) in enumerate(keeps):
        parts.append(f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=PTS-STARTPTS[v{i}];")
        parts.append(f"[0:a]atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS[a{i}];")
        labels.append(f"[v{i}][a{i}]")
    graph = "".join(parts) + "".join(labels) + f"concat=n={len(keeps)}:v=1:a=1[v][a]"
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(graph)
        script = f.name
    try:
        ffmpeg("-i", src, "-filter_complex_script", script, "-map", "[v]", "-map", "[a]", *ENC, *AENC, dst)
    finally:
        Path(script).unlink(missing_ok=True)
    after = probe(dst)["duration"]
    result = {"before_sec": round(info["duration"], 2), "after_sec": round(after, 2), "segments": len(keeps)}
    print(json.dumps(result, ensure_ascii=False))
    return result


# ---------------------------------------------------------------- 字幕

def parse_srt(text: str) -> list[tuple[float, float, str]]:
    def ts(s: str) -> float:
        h, m, rest = s.strip().replace(",", ".").split(":")
        return int(h) * 3600 + int(m) * 60 + float(rest)

    cues = []
    for block in re.split(r"\n\s*\n", text.strip().replace("\r\n", "\n")):
        lines = [l for l in block.split("\n") if l.strip()]
        idx = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if idx is None:
            continue
        start, end = lines[idx].split("-->")
        cues.append((ts(start), ts(end), "\n".join(lines[idx + 1:])))
    return cues


def ass_time(t: float) -> str:
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def srt_to_ass(srt: str, width: int, height: int, font_size: int, center: bool = False) -> str:
    """動画の実ピクセルを基準にした ASS を作る（font_size がそのままピクセルになる）。"""
    align = 5 if center else 2
    margin_v = 0 if center else int(height * 0.12)
    header = (
        "[Script Info]\nScriptType: v4.00+\n"
        f"PlayResX: {width}\nPlayResY: {height}\nWrapStyle: 0\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        f"Style: Default,{CFG['font']},{font_size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,"
        f"1,0,0,0,100,100,0,0,1,{max(2, font_size // 14)},0,{align},60,60,{margin_v},1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    newline = "\\N"
    events = [
        f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Default,,0,0,0,,{t.replace(chr(10), newline)}"
        for s, e, t in parse_srt(srt)
    ]
    return header + "\n".join(events) + "\n"


def _filter_path(p: str) -> str:
    return p.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")


def subtitles(src, srt, dst, font_size=None) -> None:
    info = probe(src)
    ass = srt_to_ass(Path(srt).read_text(encoding="utf-8"), info["width"], info["height"],
                     font_size or CFG["font_size"])
    with tempfile.NamedTemporaryFile("w", suffix=".ass", delete=False, encoding="utf-8") as f:
        f.write(ass)
        ass_path = f.name
    try:
        audio = ["-c:a", "copy"] if info["has_audio"] else []
        ffmpeg("-i", src, "-vf", f"ass='{_filter_path(ass_path)}'", *ENC, *audio, dst)
    finally:
        Path(ass_path).unlink(missing_ok=True)


# ---------------------------------------------------------------- BGM

def bgm(src, music, dst, volume=None) -> None:
    volume = CFG["bgm_volume"] if volume is None else volume
    info = probe(src)
    if info["has_audio"]:
        # 話し声があるところだけ BGM を自動で下げる（サイドチェイン・ダッキング）
        graph = (
            f"[1:a]aloop=loop=-1:size=2e9,volume={volume}[bg];"
            "[0:a]asplit=2[voice][key];"
            "[bg][key]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
            "[voice][duck]amix=inputs=2:duration=first:normalize=0[a]"
        )
    else:
        graph = f"[1:a]aloop=loop=-1:size=2e9,volume={volume}[a]"
    ffmpeg("-i", src, "-i", music, "-filter_complex", graph,
           "-map", "0:v", "-map", "[a]", "-c:v", "copy", *AENC, "-t", f"{info['duration']:.3f}", dst)


# ---------------------------------------------------------------- 縦型化

def vertical(src, dst, mode="blur", width=1080, height=1920) -> None:
    if mode == "crop":
        vf = f"crop='min(iw,ih*9/16)':ih,scale={width}:{height},setsar=1"
        args = ["-vf", vf]
    else:
        graph = (
            f"[0:v]split[a][b];"
            f"[a]scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height},"
            f"boxblur=20:5[bg];"
            f"[b]scale={width}:{height}:force_original_aspect_ratio=decrease[fg];"
            f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[v]"
        )
        args = ["-filter_complex", graph, "-map", "[v]", "-map", "0:a?"]
    audio = ["-c:a", "copy"] if probe(src)["has_audio"] else []
    ffmpeg("-i", src, *args, *ENC, *audio, dst)


# ---------------------------------------------------------------- サムネイル

def find_font_file() -> str:
    out = subprocess.run(["fc-match", "-f", "%{file}", f"{CFG['font']}:lang=ja"],
                         capture_output=True, text=True).stdout.strip()
    if not out:
        raise SystemExit("日本語フォントが見つかりません（fonts-ipafont などを入れてください）")
    return out


def thumbnail(src, dst, text, at=1.0) -> None:
    info = probe(src)
    at = min(at, max(0.0, info["duration"] - 0.1))
    w, h = info["width"], info["height"]
    size = int(min(w, h) * 0.11)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(text)
        text_path = f.name
    try:
        vf = (
            f"drawtext=fontfile='{_filter_path(find_font_file())}':textfile='{_filter_path(text_path)}':"
            f"fontsize={size}:fontcolor=white:borderw={max(4, size // 12)}:bordercolor=black:"
            f"box=1:boxcolor=black@0.35:boxborderw={size // 3}:x=(w-text_w)/2:y=(h-text_h)/2"
        )
        ffmpeg("-ss", f"{at:.2f}", "-i", src, "-frames:v", "1", "-vf", vf, dst)
    finally:
        Path(text_path).unlink(missing_ok=True)


# ---------------------------------------------------------------- 台本（SRT）だけから動画を作る

def from_srt(srt, dst, background="#111827", size="1080x1920", font_size=None) -> None:
    """素材がないときに、字幕を大きく出す「テキスト動画」を作る。"""
    width, height = (int(x) for x in size.lower().split("x"))
    cues = parse_srt(Path(srt).read_text(encoding="utf-8"))
    if not cues:
        raise SystemExit("字幕が空です")
    duration = cues[-1][1] + 0.5
    ass = srt_to_ass(Path(srt).read_text(encoding="utf-8"), width, height,
                     font_size or int(CFG["font_size"] * 1.4), center=True)
    with tempfile.NamedTemporaryFile("w", suffix=".ass", delete=False, encoding="utf-8") as f:
        f.write(ass)
        ass_path = f.name
    try:
        if background.startswith("#") or not Path(background).exists():
            color = background if background.startswith("#") else "#111827"
            inp = ["-f", "lavfi", "-i", f"color=c={color}:s={width}x{height}:d={duration:.2f}:r=30"]
            pre = ""
        else:
            inp = ["-loop", "1", "-t", f"{duration:.2f}", "-i", background]
            pre = (f"scale={width}:{height}:force_original_aspect_ratio=increase,"
                   f"crop={width}:{height},eq=brightness=-0.25,")
        inp += ["-f", "lavfi", "-t", f"{duration:.2f}", "-i", "anullsrc=r=44100:cl=stereo"]
        ffmpeg(*inp, "-vf", f"{pre}ass='{_filter_path(ass_path)}'", "-map", "0:v", "-map", "1:a",
               "-r", "30", *ENC, *AENC, "-shortest", dst)
    finally:
        Path(ass_path).unlink(missing_ok=True)


# ---------------------------------------------------------------- 文字起こし（任意）

def transcribe(src, dst_srt, model="small") -> None:
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except ImportError:
        raise SystemExit("faster-whisper が未インストールです: pip install faster-whisper")

    def fmt(t: float) -> str:
        ms = int(round(t * 1000))
        h, ms = divmod(ms, 3600000)
        m, ms = divmod(ms, 60000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    segments, _ = WhisperModel(model, compute_type="int8").transcribe(src, language="ja")
    lines = [f"{i}\n{fmt(s.start)} --> {fmt(s.end)}\n{s.text.strip()}\n"
             for i, s in enumerate(segments, 1)]
    Path(dst_srt).write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------- ジョブ実行

def run_job(job_path: str) -> None:
    """JSON ジョブの steps を順番に実行する。各ステップの出力が次の入力になる。"""
    job_file = Path(job_path)
    job = json.loads(job_file.read_text(encoding="utf-8"))

    def resolve(p: str) -> str:
        path = Path(p)
        return str(path if path.is_absolute() else ROOT / path)

    out_dir = Path(resolve(job["output_dir"]))
    out_dir.mkdir(parents=True, exist_ok=True)
    current = resolve(job["input"]) if job.get("input") else None
    log = [f"# 編集ログ: {job_file.name}", ""]

    for n, step in enumerate(job["steps"], 1):
        op = step["op"]
        dst = str(out_dir / f"{n:02d}_{op}.mp4")
        if op == "from_srt":
            from_srt(resolve(step["srt"]), dst, step.get("background", "#111827"),
                     step.get("size", "1080x1920"), step.get("font_size"))
        elif current is None:
            raise SystemExit(f"step {n} ({op}) の入力がありません。input か from_srt を指定してください")
        elif op == "cut_silence":
            r = cut_silence(current, dst, step.get("threshold_db"), step.get("min_silence_sec"),
                            step.get("padding_sec"))
            log.append(f"- 無音カット: {r['before_sec']}秒 → {r['after_sec']}秒（{r['segments']}区間）")
        elif op == "vertical":
            vertical(current, dst, step.get("mode", "blur"))
        elif op == "transcribe":
            srt = str(out_dir / f"{n:02d}_transcript.srt")
            transcribe(current, srt, step.get("model", "small"))
            log.append(f"- 文字起こし: {srt}")
            continue
        elif op == "subtitles":
            srt = step.get("srt")
            if not srt:
                srts = sorted(out_dir.glob("*_transcript.srt"))
                if not srts:
                    raise SystemExit("subtitles: srt 未指定で、transcribe の結果もありません")
                srt = str(srts[-1])
            subtitles(current, resolve(srt), dst, step.get("font_size"))
        elif op == "bgm":
            bgm(current, resolve(step["file"]), dst, step.get("volume"))
        else:
            raise SystemExit(f"未知の op: {op}")
        current = dst
        log.append(f"- step {n} {op} → {Path(dst).name}")

    final = out_dir / job.get("final_name", "final.mp4")
    shutil.copyfile(current, final)
    info = probe(final)
    log.append(f"\n完成: {final.name}（{info['duration']:.1f}秒, {info['width']}x{info['height']}）")

    if job.get("thumbnail"):
        thumb = out_dir / "thumbnail.png"
        thumbnail(str(final), str(thumb), job["thumbnail"]["text"], job["thumbnail"].get("at", 1.0))
        log.append(f"サムネ: {thumb.name}")

    if not job.get("keep_intermediate", False):
        for p in out_dir.glob("[0-9][0-9]_*.mp4"):
            p.unlink()

    (out_dir / "edit_log.md").write_text("\n".join(log) + "\n", encoding="utf-8")
    print("\n".join(log))


# ---------------------------------------------------------------- CLI

def main() -> None:
    p = argparse.ArgumentParser(description="動画自動編集エンジン")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("probe"); s.add_argument("src")
    s = sub.add_parser("cut-silence"); s.add_argument("src"); s.add_argument("dst")
    s.add_argument("--threshold-db", type=float); s.add_argument("--min-silence", type=float)
    s.add_argument("--padding", type=float)
    s = sub.add_parser("subtitles"); s.add_argument("src"); s.add_argument("srt"); s.add_argument("dst")
    s.add_argument("--font-size", type=int)
    s = sub.add_parser("bgm"); s.add_argument("src"); s.add_argument("music"); s.add_argument("dst")
    s.add_argument("--volume", type=float)
    s = sub.add_parser("vertical"); s.add_argument("src"); s.add_argument("dst")
    s.add_argument("--mode", choices=["blur", "crop"], default="blur")
    s = sub.add_parser("thumbnail"); s.add_argument("src"); s.add_argument("dst")
    s.add_argument("--text", required=True); s.add_argument("--at", type=float, default=1.0)
    s = sub.add_parser("from-srt"); s.add_argument("srt"); s.add_argument("dst")
    s.add_argument("--background", default="#111827"); s.add_argument("--size", default="1080x1920")
    s = sub.add_parser("transcribe"); s.add_argument("src"); s.add_argument("dst")
    s.add_argument("--model", default="small")
    s = sub.add_parser("run"); s.add_argument("job")

    a = p.parse_args()
    if a.cmd == "probe":
        print(json.dumps(probe(a.src), ensure_ascii=False))
    elif a.cmd == "cut-silence":
        cut_silence(a.src, a.dst, a.threshold_db, a.min_silence, a.padding)
    elif a.cmd == "subtitles":
        subtitles(a.src, a.srt, a.dst, a.font_size)
    elif a.cmd == "bgm":
        bgm(a.src, a.music, a.dst, a.volume)
    elif a.cmd == "vertical":
        vertical(a.src, a.dst, a.mode)
    elif a.cmd == "thumbnail":
        thumbnail(a.src, a.dst, a.text, a.at)
    elif a.cmd == "from-srt":
        from_srt(a.srt, a.dst, a.background, a.size)
    elif a.cmd == "transcribe":
        transcribe(a.src, a.dst, a.model)
    elif a.cmd == "run":
        run_job(a.job)


if __name__ == "__main__":
    main()
