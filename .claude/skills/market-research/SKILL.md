---
name: market-research
description: マーケティング部門の業務フロー。事業や施策が収益化につながるかを、調査（marketing-researcher を論点ごとに並列）→ 戦略・収益シミュレーション（marketing-strategist）→ QA の順で判断し、レポートにまとめる。「儲かるか調べて」「市場調査」「収益化の検証」などで使う。
---

# 市場・収益化調査

引数：調べたい事業・施策（例：「note と動画編集の収益化」）。

1. 問いを3〜4個の独立した論点に分ける（例：収益源A／収益源B／規約リスク／代替の稼ぎ方）。
2. 論点ごとに `marketing-researcher` を**並列で**起動し、`docs/marketing/research/<論点>.md` に書かせる。
3. `marketing-strategist` に全レポートを読ませ、`docs/marketing/<日付>_<テーマ>_report.md` に
   シミュレーションと結論を書かせる。
4. `qa-reviewer` に、数字と出典の整合（特に strategist の前提がレポートの数字と一致するか）を確認させる。
5. 結論・根拠・次の一手を短く報告する。
