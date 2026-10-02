# 問い

AIで自動生成したショート動画（YouTube Shorts / TikTok / Instagram Reels）で、日本の個人がどれくらい・どれくらいの期間で収益化できるか。そもそも収益化が許されるか。

- 対象：「越境インプット」（`config/brand.yaml`）。note 記事から 60 秒・9:16 の縦型ショートを自動生成。素材がなければ ffmpeg で「字幕だけのテキスト動画」。顔出し・ナレーションは未定。
- 調査日：2026-10-02（JST）。担当：マーケティング部門 調査担当。

---

## 結論（3行）

1. **広告収益（再生報酬）はほぼ期待できない。** YouTube Shorts の日本の RPM は実測で 1,000 回再生あたり約 7〜13 円。しかも 2027-02-01 から新規参加は「登録者1,000人＋90日2,000万回再生」、Shorts 収益の分配を受けるには毎月「直近90日1,000万回再生」が必要になる。新規の個人チャンネルにとって、月2〜3万円の広告収益でもかなりの大ヒットが前提。
2. **「字幕だけ・テンプレ・AI量産」は、規約上そのまま収益化 NG の型に当てはまる。** YouTube の inauthentic content ポリシー（2025-07-15 改定）は「最小限のナレーションしかないスクロールテキスト」「汎用テンプレで作った AI 生成コンテンツ」を名指しで対象外にしている。2026年に入って日本でも AI ショートの収益化停止が相次いでいる。TikTok は「1分以上」の動画しか報酬の対象にならず、60 秒ちょうどの設計ではそもそも対象外になりうる。
3. **現実的な使い道は「note への集客」。ただし転換率は低い。** Shorts の概要欄・コメントのリンクは 2023年からクリックできない（プロフィールのリンクのみ）。プロフィール→リンクのクリック率は業界目安で 1〜3%。動画1本ごとに独自の考察を入れ、人の手が入ったと分かる作りにすることが、収益化と集客の両方の前提になる。

---

## 事実（数字・出典付き）

### 1. YouTube パートナープログラム（YPP）と Shorts の収益分配

| 項目 | 数字 | 時点 | 出典 |
|---|---|---|---|
| YPP 参加条件（現行・広告収益あり） | 登録者1,000人＋（直近12か月の総再生時間4,000時間 **または** 直近90日の Shorts 視聴1,000万回） | 2026-10 確認 | [YouTube ヘルプ 72851](https://support.google.com/youtube/answer/72851?hl=ja) |
| YPP 参加条件（2027-02-01〜・新規） | 登録者1,000人＋（直近365日の総再生時間8,000時間 **または** 直近90日の Shorts 視聴2,000万回）。基準は**2倍** | 2026-08-10 発表 | [YouTube 公式ブログ](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/)、[YouTube ヘルプ 12843009](https://support.google.com/youtube/answer/12843009?hl=en) |
| Shorts 収益分配を受ける条件（2027-02-01〜） | 直近90日の対象 Shorts 視聴が**1,000万回以上の月だけ**、Shorts の広告・サブスク収益を受け取れる（未達でも YPP からは外れない） | 同上 | 同上、[Search Engine Journal（2026-08-11）](https://www.searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331/) |
| 既存 YPP 参加者 | 参加資格はそのまま（2027-01-31 までに新規約への同意が必要） | 同上 | [YouTube ヘルプ 12843009](https://support.google.com/youtube/answer/12843009?hl=en) |
| ファン資金（メンバーシップ・Super Thanks 等）の条件 | 登録者500人＋（総再生時間3,000時間 または 90日 Shorts 視聴300万回）。2027年の変更なし。**広告収益はこの段階では入らない** | 同上 | 同上 |
| 1,000万回に届かないチャンネル向けの代替 | 「YouTube Shopping のボーナス」「ブランド案件のインセンティブ」「トレンドの起点に対するボーナス」を導入予定（詳細は未公表） | 2026-08-10 | [YouTube 公式ブログ](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/) |
| Shorts 収益分配の仕組み | Shorts フィードの広告収益を毎月プール → 音楽ライセンス分を差し引き（楽曲1曲使用なら半分が音楽側）→ 対象チャンネルの「エンゲージビュー」シェアで按分 → **クリエイターの取り分は45%**（音楽の有無に関係なく） | 2026-10 確認 | [YouTube ヘルプ 12504220](https://support.google.com/youtube/answer/12504220?hl=en) |
| 収益・YPP 判定に使う再生数 | 2025-03-31 から表示上の「視聴回数」は再生開始ごとに数えるが、YPP の判定と収益は従来基準の「エンゲージビュー」 | 2025-03 | [Search Engine Journal](https://www.searchenginejournal.com/youtube-changes-shorts-view-counts-no-change-to-monetization/543005/) |
| Shorts 全体の規模 | 1日あたり2,000億回超の再生 | 2025-06（2026-08 の公式ブログでも同じ数字） | [YouTube 公式ブログ](https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/) |
| YPP 参加者のうち Shorts で収益を得ている割合 | 25%超 | 2024-03（2年以上前のため参考値） | [Tubefilter](https://www.tubefilter.com/2024/03/28/youtube-partner-program-shorts-monetization-ads-one-year-stats/) |

#### 日本の Shorts RPM（1,000回再生あたりの収益）

| データ | RPM | 時点 | 出典 |
|---|---|---|---|
| 個人の実測（8本・1.1万〜2,118万回再生） | **約6.5〜12.3円**（1,025万回で約81,800円＝8.0円、2,118万回で約166,900円＝7.9円） | 公開日の記載なし | [つっしー（note）](https://note.com/tsusshi_24/n/nfcac3cfecf8f) |
| 同じ人物の別動画（イラスト系・400万回） | **約13.2円**（52,900円） | 2026-03-06 | [つっしーのブログ](https://www.tsusshinofudeblog.com/youtube-6/10333/) |
| MCN（AIR Media-Tech）の数千チャンネル集計 | 日本 **$0.144**（米国 $0.328、インド $0.008） | 2025年データ（2026-01-23 更新） | [AIR Media-Tech](https://air.io/en/monetization/what-rpm-can-you-expect-from-shorts-in-2026) |

- 推計：$0.144 × 150円/ドル ≒ **約21.6円**（為替150円は仮定）。個人の実測（7〜13円）より高い。MCN の集計は収益化済みで上手くいっているチャンネルに寄っている可能性がある。
- 日本のまとめ記事に多い「1再生0.003〜0.01円」（＝RPM 3〜10円）や「RPM 30円台に上がった」は、出典やデータの出どころが書かれていない（[herozz](https://herozz.co.jp/blog/youtubeshort-how-much-profit/)、[bloomeria](https://bloomeria.jp/blog/youtube-shorts-monetization-guide) で確認）。そのため採用しない。

### 2. AI 量産・テンプレ・テキストだけの動画に関する規約

| 項目 | 内容 | 時点 | 出典 |
|---|---|---|---|
| inauthentic content（旧 repetitious content） | 2025-07-15 に名称変更。収益化の対象外になる例は次のとおり：「教育的価値の低い、似た／繰り返しのコンテンツ」「**画像スライドショー、テンプレート化されたストーリー、または最小限のナレーションしかない（もしくはナレーションのない）スクロールテキスト**」「クリエイター独自の洞察がない、**汎用的・非独創的なテンプレートで作った AI 生成コンテンツ**」 | 2025-07-15 改定 | [YouTube ヘルプ 1311392](https://support.google.com/youtube/answer/1311392?hl=en) |
| reused content（再利用コンテンツ） | 他人の素材を、独自の解説や大きな改変を加えずに使うと対象外。「**自分が作っていない資料の読み上げだけ**のコンテンツ」も例に入っている | 同上 | 同上 |
| YouTube 側の説明 | Rene Ritchie（Creator Liaison）は「量産・反復を見分けやすくする**小さな更新**」と説明。この種のコンテンツは「何年も前から収益化の対象外」だった | 2025-07-09 | [TechCrunch](https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows) |
| AI 生成の開示ルール（YouTube） | 開示が必要なのは「**写実的**な」改変・合成（実在の人物が言っていないことを言う、実際の出来事の改変、本物に見える架空の場面）だけ。**台本・字幕・サムネ・タイトルに AI を使うこと、自分の声のクローンでナレーションすることは開示不要**。開示しても配信や収益化は制限されない。開示を怠り続けると、ラベルの強制付与・削除・YPP 停止の可能性がある | 2026-10 確認 | [YouTube ヘルプ 14328491](https://support.google.com/youtube/answer/14328491?hl=en) |
| 取り締まりの実績 | 2026-01 に CEO の Neal Mohan が年頭書簡で「低品質な AI コンテンツ」への対策を最優先事項に挙げた。Kapwing の追跡では、AI スロップ系チャンネル16〜18件が削除または非表示（合計登録者3,500万・生涯再生47億回） | 2026-01 | [Tubefilter（2026-01-29）](https://www.tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/amp/) |
| 巻き添え | 顔出しなしでも人が作っているチャンネルが減収・収益化停止になった報告がある（例：登録者170万人の Doctor NOS が「顔を出さずに同じことをしている人の多くが収益化停止されている」と発言） | 2026-06-15 | [The Next Web](https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage) |
| 日本での状況 | 「2026年の年始、YouTube ショートで収益化停止やアカウント削除が相次いだ」 | 2026-01-14 | [ウォーカープラス](https://www.walkerplus.com/article/1319640/) |

### 3. TikTok / Instagram（日本）

| 項目 | 数字・内容 | 時点 | 出典 |
|---|---|---|---|
| TikTok Creator Rewards Program（日本） | 2024-03-19 に日本で開始。条件は**18歳以上・フォロワー1万人以上・動画再生10万回以上**（直近30日、おすすめフィード）。評価指標は「オリジナリティ」「再生時間（完了率含む）」「エンゲージメント」「検索価値」の4つ。広告価値も報酬に反映される | 2024-03-19 | [TikTok Newsroom（日本）](https://newsroom.tiktok.com/ja-jp/tiktok-creator-rewards-program) |
| TikTok 動画の長さ・アカウントの条件 | **1分以上**のオリジナル動画が対象。個人アカウントのみ（ビジネスアカウントは不可）。他 SNS からの転載は不可 | 2026-06-22 | [THE CKB](https://www.theckb.com/archive/how-to-apply-for-tik-tok-monetisation/)（TikTok 公式ヘルプはページを取得できず未確認） |
| TikTok の日本の RPM | 1,000回再生あたり **20〜80円**（まとめ記事の相場。実測の出典ははっきりしない） | 2026 | [ours-magazine](https://www.ours-magazine.jp/articles/tiktok-creator-rewards-monetization)、[THE CKB](https://www.theckb.com/archive/how-to-apply-for-tik-tok-monetisation/) |
| TikTok のプロフィールリンク | 個人アカウントはフォロワー1,000人以上で設置できる。ビジネスアカウントなら0人から可能（ただしビジネスアカウントは Creator Rewards の対象外） | 2026-09-23 | [THE CKB](https://www.theckb.com/archive/how-to-add-a-tiktok-link/) |
| Instagram（日本） | ギフト：フォロワー500人以上。サブスク：1万人以上（招待制）。ライブバッジ：1万人以上。リールのボーナス：招待制で「過去3か月、毎月500万回再生以上」。**リールの再生数に応じた広告収益分配は日本では一般提供されていない** | 2025-12-31 | [pamxy](https://pamxy.co.jp/marke-driven/sns-marketing/instagram/instagram-monetize/)（Meta 公式ヘルプは本文を取得できず未確認） |

### 4. ショート→note 集客の導線と転換率

| 項目 | 数字・内容 | 時点 | 出典 |
|---|---|---|---|
| YouTube Shorts のリンク | 2023-08-31 から、**Shorts の概要欄・コメントのリンクはクリックできない**。代わりにチャンネルプロフィール（登録ボタン付近）にリンクを置ける。関連動画（長尺）へのリンク機能あり | 2023-08（仕様。現在も同じかは要確認） | [TechCrunch](https://techcrunch.com/2023/08/10/youtube-is-disabling-links-on-shorts-to-cut-down-on-spam) |
| プロフィール訪問→リンククリック率 | 業界の目安は **1〜3%**。高意図ジャンルなら8〜10% | 出典の年なし | [Hopp](https://www.hopp.co/post/understanding-ctr-and-clicks-on-your-link-in-bio) |
| プロフィールリンク vs DM 自動返信 | プロフィールリンク 2.1〜3.4%、DM 自動返信 12.3〜17.8%（アフィリエイトキャンペーン1,200件超、2025年第4四半期） | 2025 Q4 | [CreatorFlow](https://creatorflow.so/blog/bio-link-vs-dm-automation-affiliate-clicks/)（ツール販売会社のブログ） |
| note への流入の実例 | 「TikTok を始めて2週間で note の閲覧数が3倍」（相対値のみ。絶対数は書かれていない） | 2026-03-16 | [まもる（note）](https://note.com/fukugyo_ouen/n/nab2cf66842f8) |
| 動画再生→プロフィール訪問率 | **信頼できる公開ベンチマークは見つからなかった**。日本の運用会社も「他社平均でなく自社の中央値を基準に」と説明している | — | [albit](https://albit.co.jp/knowledge/short-video-kpi-measurement) |

### 6. 編集を自動化する価値（参考）

| 項目 | 数字 | 時点 | 出典 |
|---|---|---|---|
| ショート動画編集の外注相場（クラウドワークス） | TikTok・ショート動画は **3,000円〜/本**、納期は3日程度 | 2026-10-01 | [クラウドワークス発注相場](https://crowdworks.jp/pages/guides/employer/pricing) |
| フリーランス・制作会社の相場 | ランサーズ 1,500〜5,000円、クラウドワークス 3,000〜50,000円、制作会社は 20,000〜98,000円/本 | 2025-03-28 | [アビリブ](https://www.ab-net.co.jp/abilivepromotion/news/246/) |
| 編集にかかる時間（30〜60秒） | 標準 **60〜90分**（カット20〜30分、テロップ20〜30分、速度5分、音10分）。慣れると40〜50分。カットとテロップで全体の約8割 | 2026-09-18 更新 | [solezore](https://solezore.co.jp/blog/short-video-editing) |

- 推計：1日1本 × 30日 × 3,000円 ＝ **外注なら月9万円相当**。自分でやると 1本60〜90分 × 30本 ＝ **月30〜45時間**。`video/autoedit.py` が自動化するのは、まさにこの「カット＋テロップ」の約8割にあたる工程。

---

## 成功例 / 失敗例・中央値

### 成功例
- **個人（イラスト系、顔出しなし・手描き）**：400万回再生で約52,900円、登録者 +4,619人（2026-03）。[出典](https://www.tsusshinofudeblog.com/youtube-6/10333/)。人が手を動かしている本物のコンテンツで、AI 量産とは違う。
- **AI 歴史・浮世絵ジャンルで生き残ったチャンネル**（江戸好奇心、AI Historia など）の共通点は、コメントにこまめに返信している、総集編（使い回し）を出していない、キャラクターのビジュアルを毎回変えている、の3つ（2026年4月の観察）。[オコジョ（note）](https://note.com/okojo_youtube/n/ne33affd4bdac)
- **AI ショートで審査に3回落ちた後に合格**：ChatGPT 台本＋AI ボイス＋Canva スライドで3回とも「再利用されたコンテンツ」を理由に不合格。低品質な初期動画を全部消し、1本あたりの制作時間を3倍にして4回目で合格（2025-10-11）。[出典](https://note.com/freelife_creator/n/n54b740a08f9d)
- **ベンダーの実験（参考程度）**：顔出しなしショート100本を30日で3媒体に投稿し、合計約240万回再生・フォロワー1.87万人・アフィリエイト $1,450（2025-08）。広告分配ではなく**アフィリエイトで稼いだ**点に注目。ただし AI ツール会社の宣伝記事。[Clippie](https://clippie.ai/blog/100-faceless-shorts-in-30-days)

### 失敗例・中央値
- **AI ショートの収益化停止（日本・2026-04）**：「ヨクアルハナシ」「ボーン博士（AI 音声）」「日本浮世絵ばなし」「歴史再現トラベラー（全編 AI）」に加え、顔出しの声優チャンネルまで停止された。共通点は、コメントに返信していない、総集編を出している、同じ AI 音声を使い続けている、の3つ。[オコジョ（note）](https://note.com/okojo_youtube/n/ne33affd4bdac)
- **AI で自動化した海外のチャンネル**：90日で登録者213人、収益0ドル。「AI のスライドショー型は、テンポの速い独自コンテンツに勝てない」として長尺に方針転換した（2025-01）。[出典](https://automatedincomelifestyle.substack.com/p/90-days-into-my-faceless-automated)
- 視聴者の反応として「AI の声だと分かるとすぐスワイプする」という声がある（2026-01）。[ウォーカープラス](https://www.walkerplus.com/article/1319640/)
- **中央値**：日本の個人の Shorts 収益の中央値や、YPP 到達までの期間の中央値を出している一次データは**見つからなかった**。公開されている実績はバズった動画ばかりで、生存者バイアスが強い。

### 伸びた例と伸びなかった例の差（観察からの整理）
| 伸びた・残った側 | 伸びなかった・止まった側 |
|---|---|
| 1本ごとに中身が違う（独自の視点・調査・手作業） | 台本の骨組みが毎回同じ（テンプレ） |
| コメント返信など「人がいる」ことが見える | 運営に人の気配がない |
| 音声やビジュアルに変化がある | 同じ AI 音声・同じ構図の繰り返し |
| 使い回しや総集編を出さない | 総集編・他人の素材のまとめ |
| 収益源が広告分配以外（アフィリエイト・自社商品） | 広告分配だけに頼る |

---

## リスク・規約

1. **「字幕だけのテキスト動画」は規約の例そのもの。** YouTube は「最小限のナレーションしかない、またはナレーションのないスクロールテキスト」と「汎用テンプレの AI 生成」を、収益化対象外の例に名指しで挙げている。ffmpeg で同じテンプレの字幕動画を毎日出すと、YPP 審査に通らない可能性が高い（停止事例と照らした推測）。
2. **note 記事の読み上げ・要約だけでは reused content になるおそれ。** 自分の note 記事なら「自分が作っていない資料」には当たらない。ただし、記事が海外 YouTube の要約を中心にしている場合、動画も「他人の素材の要約」と見られるリスクがある。**動画ごとに独自の考察・実験結果を入れること**が必要（CLAUDE.md の「要約と自分の考察で書く」とも合う）。
3. **TikTok は1分以上が条件。** `brand.yaml` の `video.short.seconds: 60` のままでは境界上になる。TikTok で報酬を狙うなら、TikTok 用の版を61秒以上にする必要がある（「60秒ちょうど」がどう扱われるかは公式の文言で確認できていない）。
4. **2027-02-01 の YPP 改定。** 新規の Shorts 経由の参加基準が90日2,000万回に上がる。今から始める個人チャンネルが2027年1月末までに現行基準（90日1,000万回）を満たすのは非現実的と見るべき（推計）。さらに、YPP に入った後も、直近90日1,000万回を下回る月は Shorts 収益がゼロになる。
5. **AI の開示。** 字幕だけ・AI 音声のナレーション自体は、写実的でなければ YouTube では開示不要。実在の人物（引用元の YouTuber など）を AI で合成して話させる表現は開示が必須で、権利・炎上リスクも高いので避ける。TikTok は写実的な AI コンテンツにラベル付けが必要（二次情報。公式ページは取得できず）。
6. **リンク導線。** YouTube Shorts の概要欄リンクはクリックできない。TikTok の個人アカウントはフォロワー1,000人まではプロフィールリンクを置けない。導線は「プロフィール→note」の1本だけで、取りこぼしが大きい。
7. **ステマ規制。** note 側にアフィリエイトがある場合、動画からの誘導にも PR 表記が必要になりうる（本調査の範囲外。別途確認が必要）。

---

## 収益シミュレーション用の主要数字（推計の材料）

- YouTube Shorts の RPM（日本）：**7〜13円**（個人の実測）／**約21円**（MCN 集計 $0.144 を150円で換算）
- 例（推計）：月100万回 × 8円/1,000 ＝ **月8,000円**。ただし2027-02以降は90日1,000万回（月平均約333万回）に届かなければ **0円**。到達ラインちょうどなら 333万 × 8円/1,000 ≒ **月2.7万円**
- YPP 新規参加（2027-02〜）：登録者1,000人＋90日 Shorts 2,000万回
- TikTok：フォロワー1万人・30日10万回・1分以上の動画。RPM 20〜80円（まとめ記事の相場）
- 集客の転換：プロフィール→リンククリックは1〜3%。動画再生→プロフィール訪問の信頼できる数字はない（自社計測が必要）
- 編集の外注相場：3,000円〜/本。標準の作業時間は60〜90分/本

---

## 確信度（高/中/低）とその理由

- **YPP の条件・2027年改定・Shorts の分配の仕組み・inauthentic content ポリシー・AI 開示ルール：高**（YouTube 公式ヘルプと公式ブログを直接確認）
- **日本の Shorts RPM：中**（個人の実測は1人分だけ。MCN 集計は日本の値が1つだけで、母集団に偏りがある。顔出しなし AI ショートの RPM はこれより低い可能性もある）
- **TikTok の条件：中〜高**（日本の公式ニュースルームで確認。「1分以上」「個人アカウントのみ」は二次情報）。**TikTok の RPM：低**（出典がはっきりしない相場）
- **Instagram：中**（二次情報。Meta 公式は取得できず）
- **集客の転換率：低**（ベンチマークは海外のツール会社の推定。note への流入の実数データは見つからなかった）
- **収益化までの期間：低**（中央値のデータが存在しない。公開されている実績はバズの事例に偏っている）

---

## 出典一覧（URL）

- https://support.google.com/youtube/answer/72851?hl=ja
- https://support.google.com/youtube/answer/12843009?hl=en
- https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- https://www.searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331/
- https://support.google.com/youtube/answer/12504220?hl=en
- https://www.searchenginejournal.com/youtube-changes-shorts-view-counts-no-change-to-monetization/543005/
- https://www.tubefilter.com/2024/03/28/youtube-partner-program-shorts-monetization-ads-one-year-stats/
- https://support.google.com/youtube/answer/1311392?hl=en
- https://support.google.com/youtube/answer/14328491?hl=en
- https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows
- https://www.tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/amp/
- https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage
- https://www.walkerplus.com/article/1319640/
- https://note.com/okojo_youtube/n/ne33affd4bdac
- https://note.com/freelife_creator/n/n54b740a08f9d
- https://note.com/tsusshi_24/n/nfcac3cfecf8f
- https://www.tsusshinofudeblog.com/youtube-6/10333/
- https://air.io/en/monetization/what-rpm-can-you-expect-from-shorts-in-2026
- https://herozz.co.jp/blog/youtubeshort-how-much-profit/
- https://bloomeria.jp/blog/youtube-shorts-monetization-guide
- https://newsroom.tiktok.com/ja-jp/tiktok-creator-rewards-program
- https://www.theckb.com/archive/how-to-apply-for-tik-tok-monetisation/
- https://www.theckb.com/archive/how-to-add-a-tiktok-link/
- https://www.ours-magazine.jp/articles/tiktok-creator-rewards-monetization
- https://pamxy.co.jp/marke-driven/sns-marketing/instagram/instagram-monetize/
- https://techcrunch.com/2023/08/10/youtube-is-disabling-links-on-shorts-to-cut-down-on-spam
- https://www.hopp.co/post/understanding-ctr-and-clicks-on-your-link-in-bio
- https://creatorflow.so/blog/bio-link-vs-dm-automation-affiliate-clicks/
- https://albit.co.jp/knowledge/short-video-kpi-measurement
- https://note.com/fukugyo_ouen/n/nab2cf66842f8
- https://clippie.ai/blog/100-faceless-shorts-in-30-days
- https://automatedincomelifestyle.substack.com/p/90-days-into-my-faceless-automated
- https://crowdworks.jp/pages/guides/employer/pricing
- https://www.ab-net.co.jp/abilivepromotion/news/246/
- https://solezore.co.jp/blog/short-video-editing
