# 成大棒球 線上觀賽

觀眾打開網址就能看 YouTube 直播，同時看到即時比分、陣容、聊天彈幕，還可以替球員刷火箭。

## 每場比賽前要做的事（約 1 分鐘）

1. 在 YouTube 排好這場直播，複製直播網址，例如 `https://www.youtube.com/live/xxxxxxxxxxx`。
2. 在 GitHub 打開這個 repo 的 `config.json`，按右上角的鉛筆（Edit）。
3. 把網址貼進 `"yt": ""` 的引號裡。
4. 比賽當天把 `"source"` 改成 `"live"`，比分和陣容就會讀紀錄系統的即時資料；改成 `"demo"` 則是義守 DEMO 劇本。
5. 按 **Commit changes** 儲存。大約 1 分鐘後生效，已經開著網頁的人也會自動換上新的直播。

改好後的範例：

```json
{
  "yt": "https://www.youtube.com/live/xxxxxxxxxxx",
  "source": "live",
  "api": "（不用動）"
}
```

分享給觀眾的連結永遠是同一個：本 repo 的 GitHub Pages 網址。

## 其他

- 臨時想分享某一部影片：在網址後面加 `?v=影片ID`，會優先播放那一部。
- 只想看 DEMO：在網址後面加 `?demo=1`。
- `index.src.html` 是原始碼；`index.html` 由 `build_live.py` 產生（會把 DEMO 資料內嵌進去）。
