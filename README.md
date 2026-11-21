# AI 與人類駕駛，誰更安全？

正式版本為 **14頁離線HTML簡報**，沿用已確認的暖白與霧綠美術。依使用者最新要求，畫面只留簡報本體、左下資料來源及右下頁碼；沒有底部控制列、附錄、講稿、全螢幕程式、hash狀態或列印PDF功能。前輪講稿與簡報PDF已移除。

## 開啟與操作

在檔案總管雙擊 [簡報入口](presentation/index.html)，以桌面Edge或Chrome開啟。無須伺服器或網路。可將 `presentation-package.zip` 解壓縮，開啟其中同一路徑。

- 下一頁：右方向鍵、PageDown或空白鍵。
- 上一頁：左方向鍵或PageUp。
- 第一頁／最後一頁：Home／End。
- 每頁左下方文獻連結開啟本機原始PDF；該PDF是引用原文，並非簡報列印版。

換頁快捷鍵不顯示於畫面。重新開啟或重新整理由第1頁開始。簡報不另行改寫瀏覽器原生功能。

請保留 `presentation/index.html`、`deck.css`、`deck.js`、完整 `presentation/assets/` 及上層 `raw/papers/` 的相對位置。字型、圖表與插圖均在本機；字型來源與授權見 [素材紀錄](presentation/assets/font-sources.json)。交付包只收簡報所需檔案、字型授權、六份引用原文與簡要開啟說明，不收舊預覽、附錄、講稿、簡報PDF或檢查圖。

## 本次驗證

已在離線file URL，以Edge 157.0.4341.60及Chrome 157.0.8103.79無視窗模式實測14頁換頁鍵與首末頁界限；確認控制列、講稿與其他自訂操作已移除。本機字型載入成功，無HTTP資源請求或頁面程式錯誤。

1600×1000的14頁畫面已逐頁實際檢視；另全篇檢查1920×1080及1366×768，無內容越界或來源區重疊。手機僅390×844模擬，可開啟且無水平溢出；未測實體手機／投影機或進行人工計時試講。原大綱估計13分鐘，並非實測。依最新要求不產製或驗證列印PDF。

檢查證據：[互動與尺寸](process/presentation_revision2_checks_2026-11-21.json)、[內容與交付包](process/presentation_revision2_delivery_2026-11-21.json)。前輪23頁與列印PDF驗證保留為歷史，不代表本版功能。

## 研究與接手入口

畫面以中文研究用途及作者年份介紹資料，不使用內部編號。專案內部仍沿用P01、P02、P05、P08、P09五篇核心及P04方法補充，供查核與Wiki維護。道路事故與理賠研究來自同一Waymo車隊，部分時期重疊；里程不相加。

- [Wiki目錄](wiki/index.md)、[綜合回答](wiki/synthesis.md)、[資料依賴](wiki/comparisons/evidence-map.md)
- [來源總表](sources/catalog.md)、[選文理由](sources/selection.md)、[下載來源](sources/download_manifest.json)
- [道路事故證據](sources/P01-evidence.md)、[其餘研究證據](sources/remaining-evidence.md)
- [大綱歷史](presentation/outline.md)、[最新設計規範](presentation/design-spec.md)、[接手狀態](PROJECT_HANDOFF.md)
- [工作紀錄](process/log.md)、[檢查修正](process/checks.md)、[流程](process/workflow.md)、[反思](process/reflection.md)

六份原始PDF未改寫。三頁風格測試仍保留於 [preview.html](presentation/preview.html)，只作設計歷史，不是正式入口，也不放入新版交付包。
