# グラフしたい（`newChart`）

```js
const chart = sheet.newChart()
    .asBarChart()
    .addRange(データの範囲)
    .setNumHeaders(1)    // 見出しに使う行数を設定
    .setPosition(表示位置)  // (行番号, 列番号, オフセットX, オフセットY)
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

`setChartType`でグラフの種類を設定できます。
設定値は`Charts.ChartType`の列挙型を指定します。

| プロパティ | 説明 |
|---|---|
| `TIMELINE` | 時系列グラフ |
| `BAR` | 横棒グラフ |
| `COLUMN` | 縦棒グラフ |
| `HISTOGRAM` | ヒストグラム |
| `PIE` | 円グラフ |
| `SCATTER` | 散布図 |

```js
// 面グラフ
newChart().asAreaChart()

// 棒グラフ
newChart().asBarChart()
newChart().asColumnChart()

// ヒストグラム
newChart().asHistogramChart()
```

グラフを作成するときに`asTYPEChart`でも指定できます。

## リファレンス

- [Class EmbeddedChart](https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart)
- [Class EmbeddedChartBuilder](https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart-builder)
- [Enum ChartType](https://developers.google.com/apps-script/reference/charts/chart-type.html)
- [グラフのオプション](https://developers.google.com/apps-script/chart-configuration-options)
