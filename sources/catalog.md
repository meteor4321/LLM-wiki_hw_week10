# 候選原始資料總表

**本輪現行狀態（2026-11-21）：**使用者已確認P01、P02、P05、P08、P09五篇核心、P04方法補充及首篇格式，六篇均已完成本輪ingest與重要原頁核對。見[Wiki目錄](../wiki/index.md)、[P01證據](P01-evidence.md)、[其餘證據](remaining-evidence.md)；完整書目與資格依據仍依本表及[第二輪查核](review-v2.md)。下一步為簡報大綱，尚未製作HTML。作者／車隊依賴及原稿差異均保留；未新增PDF，也未獨立重現統計分析。下方舊狀態是歷史，現行分工以[selection開頭](selection.md)為準。

以下保存前兩輪查核紀錄，當時的完成狀態不代表現況。查核日期：2026-11-21（臺灣時間）。**第一版五篇組合已被使用者指出互補性不足，已撤回。** 第二版新增P06／P08／P09及待查P07的完整登記見 [選文重審](review-v2.md)；當時未確認最終五篇，也未完成Wiki ingest。下方P01–P05保存第一輪書目與查證紀錄，現行狀態以本檔及selection開頭為準。

**最新清理：依使用者要求已刪除raw中的P03模擬PDF及P06混合樣本PDF，兩篇不再列核心候選。現存6份PDF為P01、P02、P04、P05、P08、P09，數量可再增加；保留不等於全部納入核心。來源、排除理由及歷史檢查紀錄仍保存，manifest以removed_path及status記錄刪除。**

本輪是選文審查：已核對書目、研究對象、方法、主要限制、作者關係與公開檔案。已閱讀摘要及相關方法、討論、限制與資料公開聲明；未宣稱逐頁精讀、逐項重算或完整查驗所有圖表。本文不提供跨論文合併的安全排名。

## 門檻與檔案驗證

- 正式審查判斷依期刊出版紀錄、研究文章類型、接受紀錄及出版識別交叉核對；PubMed 收錄本身不是審查證明。
- 接受稿可以作為已正式發表研究的合法公開全文，但須有出版頁佐證及清楚的接受稿標示。**出現在 arXiv 並不自動表示已審查，也不自動表示只有預印本。**
- 第一輪五份PDF曾完成檢查，其中P03其後依使用者要求刪除。現存檔案保留原始下載位元組；網址、日期、大小、SHA-256及移除狀態見 [download_manifest.json](download_manifest.json)，頁數與檢查／移除狀態見 [pdf_checks.json](pdf_checks.json)。歷史通過紀錄不表示已刪檔案仍存在。
- 已用 Poppler 將各篇首頁及選文相關頁渲染；實際視覺檢視了五篇首頁，以及 P01 PDF 頁18、P02 頁6、P03 頁17、P04 頁13、P05 頁13。只代表已檢查這些相關原頁，不代表整份圖表查證完成。
- 本文頁序一律以 1 起算。接受稿頁碼不可直接替換成正式期刊頁碼。擷取文字及預覽放在 `extracted/`，原始 PDF 不改寫。

## P01｜實際營運事故涉及率及事故類型（推薦）

**完整標題：** Comparison of Waymo Rider-Only crash rates by crash type to human benchmarks at 56.7 million miles

**作者：** Kristofer D. Kusano、John M. Scanlon、Yin-Hsiu Chen、Timothy L. McMurry、Tilia Gode、Trent Victor。

**年份／發表處：** 2025，*Traffic Injury Prevention* 26(sup1), S8–S20。

- 正式出版與審查依據：[期刊出版識別](https://doi.org/10.1080/15389588.2025.2499887)；出版頁標示 Research Article、Open access，Received 2025-03-05、Accepted 2025-04-25、online 2025-05-16，所屬增刊標示 Peer-Reviewed Journal。[PubMed 書目交叉核對](https://pubmed.ncbi.nlm.nih.gov/40378124/)。
- [合法免費 PDF：作者接受稿](https://storage.googleapis.com/waymo-uploads/files/documents/safety/Safety%20Impact%20Crash%20Type%20Manuscript.pdf)；[本機 PDF](../raw/papers/P01_kusano_2025_56_7m.pdf)，58 頁，包含附錄。首頁明示已獲期刊接受；不是出版排版版，引用接受稿頁序。
- 地區／對象：美國 Waymo 無車內駕駛服務，主要比較區域為鳳凰城、舊金山、洛杉磯及奧斯汀；分析一般市區道路，排除高速公路。累積里程至 2025 年1月底；不同城市開始累積里程的年份不同，不是四城同期完整追蹤。
- 方法／用途：將事故通報與業者公開里程，對照經地區、道路、車種與空間行駛分布調整的人類基準；區分受傷、氣囊作動、疑似重傷以上結果及事故類型。回答「這個車隊在這些條件下的實際事故涉及率如何」，並提供路口、行人等分組的後續教學素材。
- 主要限制：觀察性比較，並非隨機試驗；人類與系統的通報、里程估計、行駛時段與乘員配置仍可能不同。指標是涉及事故，不是肇事責任；沒有顯著增加不等於證明沒有風險。不可擴大為所有系統、道路、天候或獨立的死亡率保證。
- 業者關係／獨立核對：全部作者為 Waymo 員工。事故來源包含 NHTSA 通報及州資料；里程由 Waymo 自報。公開資料有助重現部分計算，但不等於外部獨立收集每次行駛紀錄。
- 本輪出處：接受稿 PDF 頁4（問題與範圍）、6–7（道路及地區）、10–11／表2（里程期間）、18–21（限制）、22（作者及資料公開聲明）。已視覺核對頁18。
- 重疊：沿用 P04 的比較基準方法，屬方法依賴；與 P02 是同一業者、期間部分重疊，不能作兩份獨立車隊驗證。

## P02｜第三方責任保險理賠（第二輪轉背景候選）

**完整標題：** Comparative safety performance of autonomous- and human drivers: A real-world case study of the Waymo Driver

**作者：** Luigi Di Lillo、Tilia Gode、Xilin Zhou、Margherita Atzei、Ruoshu Chen、Trent Victor。

**年份／發表處：** 2024，*Heliyon* 10(14), e34379。

- 正式出版與審查依據：[出版社 DOI](https://doi.org/10.1016/j.heliyon.2024.e34379)；正式 PDF 頁1標示 Research article、Received 2024-04-25、revised 2024-06-14、Accepted 2024-07-09。PDF 標示 Available online 2024-07-14；部分網頁的線上日期列7月13日，本文以所存 PDF 的版本日期為準。[PMC 全文紀錄](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305169/)。
- [合法免費 PDF：PMC 官方公開資料服務](https://pmc-oa-opendata.s3.amazonaws.com/PMC11305169.1/PMC11305169.1.pdf)；[本機 PDF](../raw/papers/P02_dilillo_2024_insurance.pdf)，7頁，期刊排版版，CC BY-NC-ND。公開資料服務身分由 [PMC 官方說明](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/) 核實，不是第三方擅自上傳。
- 地區／對象：舊金山與鳳凰城地區。Waymo 資料期間 2018-01-01 至 2023-08-01；人類保險基準為2016–2021年。文章同時分析手動、有安全員測試、無車內駕駛及合併類別；本專案只以 **無車內駕駛類別（RO）** 作主要安全比較。
- 方法／用途：使用 Swiss Re 的私人乘用車第三方財損與身體傷害責任理賠，依郵遞區號及責任條件建立人類基準，按 Waymo 地區里程分布加權。RO 子樣本為 3,868,506 英里（PDF 頁4）；這是暴露量，並非事故減幅。回答「對其他用路人的責任理賠是否不同」，讓讀者理解事故涉及與責任理賠的差異。
- 主要限制：理賠頻率不是所有事故率，也不是傷勢分級；財損與人身傷害不能直接相加成事故總數。兩邊資料年代不同；投保車主郵遞區號不等於每次事故地點；人類里程為估算；RO 樣本仍有限，零次觀察不代表真實風險為零。理賠也不是完美的肇事責任測量。
- 業者關係／獨立核對：Swiss Re 與 Waymo 合作，作者包括雙方人員；部分作者另有大學關係，不能因此稱為完全獨立。原始理賠資料因商業敏感不公開，無法由本專案獨立重算。作者的無已知利益衝突聲明與實際僱用關係分開記錄。
- 本輪出處：期刊印刷頁與 PDF 頁序同為1–7；頁1（作者、接受紀錄與授權）、3（期間與模式）、4–5／圖2C（RO）、5–6（限制）、6（資料不可公開）、7（利益聲明）。已視覺核對頁6。
- 重疊：與 P01 車隊及部分時期重疊，但觀察的結果與資料管道不同；提供互補視角，不能把理賠與事故涉及率直接排名或合併。

## P03｜歷史致命事故的反事實模擬（已移出核心，保留補充）

**完整標題：** Waymo simulated driving behavior in reconstructed fatal crashes within an autonomous vehicle operating domain

**作者：** John M. Scanlon、Kristofer D. Kusano、Tom Daniel、Christopher Alderson、Alexander Ogle、Trent Victor。

**年份／發表處：** 2021，*Accident Analysis & Prevention* 163, 106454。

- 正式出版與審查依據：[出版社研究文章](https://www.sciencedirect.com/science/article/pii/S0001457521004851)，[DOI](https://doi.org/10.1016/j.aap.2021.106454)，[PubMed 書目](https://pubmed.ncbi.nlm.nih.gov/34700249/)；2021-10-23線上、2021年12月卷期。Waymo 的[正式研究目錄](https://waymo.com/safety/research/)另列同一作者、題名、DOI及 Peer-reviewed Research 標籤。期刊文章身分及出版紀錄是主依據，不只採信業者標籤。
- [合法免費 PDF：作者公開全文](https://storage.googleapis.com/waymo-uploads/files/documents/Waymo-Simulated-Driving-Behavior-in-Reconstructed-Collisions.pdf)；原本機PDF已依使用者要求刪除，曾為24頁。此檔為業者公開的作者版本，**未標明是接受稿或最終排版版**；曾核對作者、題名、研究設計與出版社公開摘要的一致性，未宣稱全文與期刊版逐字相同。研究本身已正式發表，但因對主要教學問題屬間接模擬證據而移除。
- 地區／對象：美國亞利桑那州 Chandler，重建2008–2017年落在研究營運範圍內、符合納入條件的人類致命事故。以當時研究版本的 Waymo 系統在模擬中逐一替代原先駕駛。
- 方法／用途：反事實模擬意即「同一個歷史事故，如果其中一名駕駛換成系統，可能怎樣」。分開考察先發起衝突與回應衝突的角色。適合教學解釋主動避免危險與危險發生後閃避的差異。
- 主要限制：情境是歷史上人類已出事的案例，不能完整涵蓋系統特有失誤；情境重建、感測模擬與軌跡對齊有假設，沒有充分探索所有不確定性。模擬成功率不能直接當成真實每里事故率或死亡率，也不等於較新版本系統的完整能力。
- 業者關係／獨立核對：全部作者屬 Waymo，系統、模擬平台及部分重建資料非完全公開；外部無法獨立執行整套系統重現。歷史事故來源可核對的程度，與完整重現模擬須分開說明。
- 本輪出處：作者版 PDF 頁1（摘要及期間）、4–6（適用範圍與方法）、17–20／§4.2（限制）。作者版印刷頁與 PDF 頁序一致。已視覺核對頁17。
- 重疊：與 P01、P02同一業者，但不是同一種事故結果資料；可補足「如何測危險情境」，不能作為第三份真實營運事故率證明。

## P04｜如何建立公平的人類比較基準（第二輪轉背景）

**完整標題：** Benchmarks for retrospective automated driving system crash rate analysis using police-reported crash data

**作者：** John M. Scanlon、Kristofer D. Kusano、Laura A. Fraade-Blanar、Timothy L. McMurry、Yin-Hsiu Chen、Trent Victor。

**年份／發表處：** 2024，*Traffic Injury Prevention* 25(sup1), S51–S65。

- 正式出版與審查依據：[期刊全文頁](https://www.tandfonline.com/doi/full/10.1080/15389588.2024.2380522)，Research Article、Open access，Received 2024-03-22、Accepted 2024-07-11、online 2024-11-01；所屬增刊明示 Peer-Reviewed Journal。
- [合法免費 PDF：arXiv v2 作者接受稿](https://arxiv.org/pdf/2312.13228v2)；[版本頁及期刊 DOI 對應](https://arxiv.org/abs/2312.13228v2)；[本機 PDF](../raw/papers/P04_scanlon_2024_benchmarks.pdf)，29頁。v2於2024-07-24更新，版本頁明示 Accepted Manuscript，PDF 頁2起也明示接受稿與期刊 DOI。**未使用2023年 v1 作為已接受版本。**
- 地區／對象：美國全國及 Maricopa、Los Angeles、San Francisco等區域的人類車輛事故與里程資料；方法為當時市區乘用車無人駕駛部署建立比較基準，而非直接量測一個新系統。
- 方法／用途：分析警察通報、漏報修正、地區、道路與車種限制及分母匹配；特別區分「一次事故」和「涉及事故的車輛數」。回答「為何不能拿全美人類平均，直接比較某城市車隊」。
- 主要限制：低嚴重度事故的漏報修正不穩定，不同修正法可能差異大；可用里程資料限制了可調整因素，不能控制所有時段、天候與駕駛特徵。這是基準研究，不是新的獨立車隊安全驗證；不要將舊基準自動當成2026年最新道路風險。
- 業者關係／獨立核對：全部作者為 Waymo 人員。使用公開州與聯邦資料，可重現性較佳，但仍需逐一核對分類、排除及里程估算。
- 本輪出處：接受稿 PDF 頁2（接受稿與對象）、3（問題與目標）、11（事故／涉事車輛）、12–15（漏報、基準選擇與影響因素）；PDF 頁13已視覺核對。正式期刊 S51–S65 不與接受稿頁序直接對換。
- 重疊：為 P01 的方法來源；與 P05 有部分概念重疊，但 P04實際計算人類基準，P05則提供研究判讀規則。

## P05｜如何判讀安全比較研究的品質（第二輪方法候選）

**完整標題：** RAVE checklist: Recommendations for overcoming challenges in retrospective safety studies of automated driving systems

**作者：** John M. Scanlon、Eric R. Teoh、David G. Kidd、Kristofer D. Kusano、Jonas Bärgman、Geoffrey Chi-Johnston、Luigi Di Lillo、Francesca M. Favarò、Carol A. Flannagan、Henrik Liers、Bonnie Lin、Magdalena Lindman、Shane McLaughlin、Miguel A. Perez、Trent Victor。

**年份／發表處：** 2025，*Traffic Injury Prevention* 26(5), 608–621。

- 正式出版與審查依據：[期刊全文頁](https://www.tandfonline.com/doi/full/10.1080/15389588.2024.2435620)，Research Articles、Open access；Received 2024-08-06、Accepted 2024-11-25、online 2025-01-21。[出版社傳送至 ScienceDirect 的文章頁](https://www.sciencedirect.com/org/science/article/pii/S1538958824001887)另註明負責審查的副編輯；[PubMed 交叉核對](https://pubmed.ncbi.nlm.nih.gov/39836538/)。DOI含2024不代表正式出版年是2024。
- [合法免費 PDF：Chalmers大學典藏](https://research.chalmers.se/publication/544909/file/544909_Fulltext.pdf)；[本機 PDF](../raw/papers/P05_scanlon_2025_rave.pdf)，16頁，含大學封面及期刊封面，後接正式期刊頁面。CC BY-NC授權依 PDF 頁3。
- 地區／對象：主要針對已部署第4級系統與人類車隊的事後觀察研究；作者來自美國與歐洲的學界、保險與產業。不是另一個國家車隊的事故實測。
- 方法／用途：跨機構工作小組提出15項主建議，涵蓋品質與效度、透明度、解釋。這是正式審查的**方法與共識研究**，不是新車隊試驗，也不是系統性效果量統合。可直接轉成閱讀研究時的檢查問題，例如里程與事故範圍是否一致、是否公開不確定性、是否把輕傷結果推到死亡風險。
- 主要限制：部分規則與符合程度需專家判斷；遵循清單不保證研究無偏，也不證明任一系統安全。工作小組共識並非強制法規或認證標準。
- 業者關係／獨立核對：包括 Waymo、Cruise、Torc、Swiss Re、If保險，也有 IIHS、Chalmers、UMTRI、VTTI等機構。不能稱為完全獨立於業者的研究。PDF聲明本研究無相關資助，且各方未分享機密資料；沒有新的事故資料集供重算。
- 本輪出處：PDF 頁3 = 期刊608頁（作者、授權、接受紀錄）、PDF 頁12–14 = 期刊617–619頁（推論限制、清單表3–5及聲明）；已視覺核對 PDF 頁13 = 期刊618頁。
- 重疊：與 P04共同支援比較方法，但可用於檢查其餘四篇；不應再計為一份獨立實證效果。

## 其他已搜尋候選與保留／排除理由

| ID | 書目與原始來源 | 本輪判斷 |
| --- | --- | --- |
| C01 | Kusano、Scanlon、Chen、McMurry、Chen、Gode、Victor（2024），*Comparison of Waymo rider-only crash data to human benchmarks at 7.1 million miles*，Traffic Injury Prevention 25(sup1), S66–S77。[正式 DOI](https://doi.org/10.1080/15389588.2024.2380786)；[出版社 PDF](https://www.tandfonline.com/doi/pdf/10.1080/15389588.2024.2380786) | 已確認正式期刊研究。與P01同車隊且範圍高度重疊，保留作歷史比較，不占核心名額。本輪未下載或全文審查。 |
| C02 | Mohamed Abdel-Aty、Shengxuan Ding（2024），*A matched case-control analysis of autonomous vs human-driven vehicle accidents*，Nature Communications 15, 4931。[出版頁](https://www.nature.com/articles/s41467-024-48526-4)；[免費 PDF](https://www.nature.com/articles/s41467-024-48526-4.pdf) | 已確認正式開放期刊文章，接受日期2024-05-02。美國事故樣本含第2級輔助與第4級系統，且配對事故樣本分析不是每里事故率。未主推為無車內駕駛營運風險的核心證據；並非因研究「得出不利結果」而排除。作者均列UCF學術單位，業者資助細節尚未完整核對。本輪未下載、未完整精讀。 |
| C03 | Eric R. Teoh、David G. Kidd、Luke E. Riexinger（2026），*Rise of the machines: crash experiences of highly automated vehicles and human drivers*，IIHS，2026年7月。[機構原始研究頁](https://www.iihs.org/research-areas/bibliography/ref/2374) | 與主題高度相關，且外部分析有補強價值；本輪核實頁只列IIHS及日期，沒有期刊與已完成審查證據。保留待查，不列已合格核心。IIHS為保險業支持機構，不應簡化成完全無產業關係。 |
| C04 | Luigi Di Lillo、Tilia Gode、Xilin Zhou、John Scanlon、Ruoshu Chen、Trent Victor，*Do Autonomous Vehicles Outperform Latest-Generation Human-Driven Vehicles? A Comparison to Waymo's Auto Liability Insurance Claims at 25 Million Miles*。[業者公開 PDF](https://storage.googleapis.com/waymo-uploads/files/documents/safety/Comparison%20of%20Waymo%20and%20Human-Driven%20Vehicles%20at%2025M%20miles.pdf) | 較新保險研究，可能補強「與較新有人駕駛車比」的問題。Waymo目錄雖加已審查標籤，本輪未獨立核實其正式發表處與審查紀錄，因此不直接取代P02；未下載。不能將它誤登記為Heliyon e34379。 |
| C05 | Nidhi Kalra、Susan M. Paddock（2016），*Driving to safety: How many miles of driving would it take to demonstrate autonomous vehicle reliability?*，Transportation Research Part A 94, 182–193。[期刊 DOI](https://doi.org/10.1016/j.tra.2016.09.010)；[RAND同題報告](https://www.rand.org/pubs/research_reports/RR1478.html)及其公開 PDF入口 | 教學價值高：罕見傷亡需要多少證據。期刊研究已發表，但RAND公開版為不同識別的機構報告，未確認與期刊定稿的版本一致性；下載RAND PDF回應403，本機未取得。保留補充候選，不把報告冒充期刊PDF。 |
| C06 | John M. Scanlon、Kristofer D. Kusano、Johan Engström、Trent Victor（2026），*Collision Avoidance Effectiveness of an Automated Driving System Using a Human Driver Behavior Reference Model in Reconstructed Fatal Collisions*，SAE Technical Paper 2026-01-0520。[SAE正式頁](https://saemobilus.sae.org/papers/collision-avoidance-effectiveness-automated-driving-system-using-a-human-driver-behavior-reference-model-reconstructed-fatal-collisions-2026-01-0520)；[作者PDF入口](https://waymo.com/research/collision-avoidance-effectiveness-of-an-automated/) | 正式發表處已找到；以理想化專注駕駛模型比較避撞，全部作者為Waymo。與P03情境及重建資料有高度關聯。早期2022作者PDF與2026正式版本須分開，尚未完成版本及出版方審查規範查核，不額外算一篇獨立情境驗證。 |

上述候補若未全文審查，其用途與限制只限本輪可核實範圍；不得在後續直接標為已 ingest。

## 官方補充文件（不占五篇）

- **NHTSA，Automated Driving Systems／AV 2.0 官方說明頁**：[原始頁](https://www.nhtsa.gov/vehicle-manufacturers/automated-driving-systems)。用途為解釋自動化分級、指定營運範圍及自願安全評估性質；非事故比較研究，不能當成安全成效證據。本輪只登記網頁，未下載官方 PDF，也未作2026法律解釋。
- **Waymo Safety Impact 官方資料中心**：[原始頁](https://waymo.com/safety/impact/)。用途為追蹤原始里程、事故識別與資料更新。動態網頁的新數字不自動等同P01的已審查研究期間；本輪未將其較新數字混入論文結果，未下載動態資料集。
- **PMC 官方公開資料服務說明**：[原始頁](https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/)。僅用於核實P02的合法取得路徑，不是駕駛安全內容來源。
