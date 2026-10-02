---
name: note-pipeline
description: note記事部門の業務フロー。前回作った note-article スキル（「越境インプット」）の手順を、リサーチ→執筆→校正→QA の部門サブエージェントで回し、下書き保存まで行う。「note記事を作って」「今日のnote」などで使う。
---

# note記事パイプライン（note-article スキルの部門版）

引数：テーマ（省略時はおまかせ）。手順とルールの原本は `note-article` スキル。食い違ったら原本を優先する。

## 準備
1. 日付（JST）：`TZ=Asia/Tokyo date +%F`。**今日すでに `output/<日付>/*/article.md` があれば作らない**（1日1本まで）。
2. 型を決める：`output/` の直近記事の `delivery.md` の型を見て、同じ型が続かないように A/B/C を選ぶ。
3. 出力先 `output/<日付>/<slug>/` を作る。

## 工程
1. **リサーチ**：`note-researcher` → `research.md`（テーマ未指定なら3案 → ユーザーに選ばせる。定期実行時は1案目）
2. **執筆**：`note-writer` → `draft.md`
3. **校正**：`note-editor` → `article.md`, `delivery.md`
4. **QA**：`qa-reviewer` → `qa.md`。FIX なら差し戻し（最大2回）、REJECT なら人に相談。
5. **下書き投稿**：Claude in Chrome（`mcp__claude-in-chrome__*`）が使える場合のみ
   https://note.com/notes/new でタイトル・本文を入力して**下書き保存**。公開はしない。
   使えない・失敗した場合は、その旨をはっきり伝え、article.md を貼り付けてもらう。
6. **納品**：`delivery.md` の内容（型・自分で書く箇所・タイトル案5つ・投稿推奨時間・X要約）を伝える。

## 週次レビュー
投稿実績（ビュー・スキ・コメント）をもらったら、`note-article` スキルの「週次レビュー」に従う
（スキ率3%合格、2%未満が3本続いたら方向転換、改善点は1つだけ）。結果は `metrics/weekly/<日付>.md` に残す。
