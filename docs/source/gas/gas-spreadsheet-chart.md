# グラフしたい（`newChart`）

```js
const chart = sheet.newChart()
    .asBarChart()
    .addRange(データの範囲)
    .setPosition(表示位置)
    .setOption("height", 高さ)
    .setOption("width", 幅)
    .setOption("title", タイトル);

sheet.insertChart(chart.build());
```

`Sheet.newChart`でグラフ（のビルダー）を新しく作成し、
`Sheet.insertChart`でシートに挿入します。

## グラフの種類したい（`setChartType`)

```js
chartBuilder.setChartType(種類)
```

```js
// 面グラフ
newChart().asAreaChart()

// 棒グラフ
newChart().asBarChart()
newChart().asColumnChart()

// ヒストグラム
newChart().asHistogramChart()
```

## リファレンス

- [Class EmbeddedChart](https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart)
- [Class EmbeddedChartBuilder](https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart-builder)
