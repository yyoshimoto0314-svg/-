---
name: video-pipeline
description: 動画編集部門の業務フロー。素材動画を自動編集（無音カット・縦型化・字幕・BGM・サムネ）する。素材がなければ note 記事から台本と字幕だけのテキスト動画を作る。「動画を編集して」「ショート動画を作って」などで使う。
---

# 動画パイプライン

引数：素材動画のパス、編集ジョブ JSON、または note 記事のディレクトリ（`output/<日付>/<slug>/`）。

## パターンA：素材動画がある
1. `video-editor` に素材パスと出力先を渡す。ジョブが無ければ `video/jobs/example.json` をコピーして
   `input` / `output_dir` / 字幕 / BGM を書き換えたジョブを作らせる。
2. 字幕は、`faster-whisper` が入っていればジョブに `{"op":"transcribe"}` を `cut_silence` の後に入れ、
   `{"op":"subtitles"}`（srt 省略）で文字起こし結果を使う。無ければ台本の SRT を使う。
   ※ 無音カット後に尺が変わるので、字幕は必ずカット後の動画に合わせること。

## パターンB：note 記事から作る
1. `video-scriptwriter` に記事ディレクトリを渡す → `script.md`, `subtitles.srt`, `thumbnail.txt`, `video_job.json`
2. 素材 `media/<slug>.mp4` が無ければ、ジョブを `from_srt` ステップ（`video/jobs/text-only.json` と同じ形）
   に置き換えて「テキスト動画」を作る。BGM ファイルがあれば `bgm` ステップを足す。
3. `video-editor` に `python3 video/autoedit.py run <video_job.json>` を実行させる。

## 共通
- 完成後、`qa-reviewer` に動画ディレクトリをチェックさせる（字幕誤字・尺・フック）。
- BGM・画像素材は権利がクリアなもの（自作・商用利用可ライセンス）だけを使う。
