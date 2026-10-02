#!/usr/bin/env bash
# 動画編集エンジンの動作確認。合成素材を作ってサンプルジョブを2本流す。
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p media
ffmpeg -y -hide_banner -loglevel error -f lavfi -i testsrc=s=1280x720:d=10:r=30 \
  -f lavfi -i "sine=f=440:d=10,volume='if(lt(mod(t,3),1.5),1,0)':eval=frame" \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest media/sample.mp4
ffmpeg -y -hide_banner -loglevel error -f lavfi -i "sine=f=220:d=20" -c:a libmp3lame media/bgm.mp3
python3 video/autoedit.py run video/jobs/example.json 2>/dev/null
python3 video/autoedit.py run video/jobs/text-only.json 2>/dev/null
echo "OK: output/example/ を確認してください"
