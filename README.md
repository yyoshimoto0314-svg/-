# AIエージェント組織

Claude の中に「AIエージェントの会社」を作り、**note記事の自動作成** と **動画の自動編集** を部門として運営する。

- 手順（ロードマップ）：[docs/00_roadmap.md](docs/00_roadmap.md)
- 組織憲章（CEO の行動規範）：[CLAUDE.md](CLAUDE.md)
- ブランド設定：[config/brand.yaml](config/brand.yaml)

## 使い方（Claude Code でこのリポジトリを開いて）

| コマンド | やること |
|---|---|
| `/note-pipeline <テーマ>` | note記事を1本（リサーチ→執筆→校正→QA） |
| `/video-pipeline <素材 or 記事ディレクトリ>` | 動画の自動編集 / 記事からショート動画 |
| `/daily-run` | 上の2つを連携して1日分を作り、日報を出す |

## 動画編集エンジン

```bash
./video/selftest.sh                              # 動作確認
python3 video/autoedit.py run video/jobs/example.json
```

必要なもの：`ffmpeg`、Python 3.10+、日本語フォント（IPAゴシック等）。
任意：`pip install pyyaml`（brand.yaml の設定を反映）、`pip install faster-whisper`（自動文字起こし）。
