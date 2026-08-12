# グラフを操作したい（`newChart`）

```js
const range = sheet.getRange("A1:B10");

const chart = sheet.newChart()
    .asBarChart()
    .addRange(range)
    .setNumHeaders(1)               // 見出しに使う行数を設定
    .setPosition(1, 4, 0, 0)        // (行番号, 列番号, オフセットX, オフセットY)
    .setOption("height", 300)
    .setOption("width", 500)
    .setOption("title", "グラフタイトル")
    .build();

sheet.insertChart(chart);
```

`Sheet.newChart`でグラフ（のビルダー）を新しく作成し、
`Sheet.insertChart`でシートに挿入します。

## グラフの種類を変更したい（`setChartType`）

```js
const chart = sheet.newChart()
    .setChartType(Charts.ChartType.PIE)
    .addRange(range)
    .build();
```

`setChartType`でグラフの種類を設定できます。
設定値は`Charts.ChartType`の列挙型を指定します。

| プロパティ | 説明 |
| --- | --- |
| `TIMELINE` | 時系列グラフ |
| `BAR` | 横棒グラフ |
| `COLUMN` | 縦棒グラフ |
| `HISTOGRAM` | ヒストグラム |
| `PIE` | 円グラフ |
| `SCATTER` | 散布図 |

```js
// 面グラフ
sheet.newChart().asAreaChart()

// 棒グラフ
sheet.newChart().asBarChart()
sheet.newChart().asColumnChart()

// ヒストグラム
sheet.newChart().asHistogramChart()
```

グラフを作成するときに`asTYPEChart`でも指定できます。
`setChartType`を使うか`asTYPEChart`を使うかは好みの問題です。

## 棒グラフにしたい（`asBarChart` / `asColumnChart`）

```js
const range = sheet.getRange("A1:B10");

// 横棒グラフ
const barChart = sheet.newChart()
    .asBarChart()
    .addRange(range)
    .setNumHeaders(1)
    .setOption("title", "横棒グラフ")
    .build();
sheet.insertChart(barChart);

// 縦棒グラフ
const columnChart = sheet.newChart()
    .asColumnChart()
    .addRange(range)
    .setNumHeaders(1)
    .setOption("title", "縦棒グラフ")
    .build();
sheet.insertChart(columnChart);
```

`asBarChart`で横棒グラフ、`asColumnChart`で縦棒グラフを作成できます。
カテゴリごとの数値を比較したいときによく使います。

## 散布図にしたい（`asScatterChart`）

```js
const range = sheet.getRange("A1:B10");

const scatterChart = sheet.newChart()
    .asScatterChart()
    .addRange(range)
    .setNumHeaders(1)
    .setOption("title", "散布図")
    .build();
sheet.insertChart(scatterChart);
```

`asScatterChart`で散布図を作成できます。
2つの数値データの相関関係を確認したいときによく使います。

## リファレンス

- [Class EmbeddedChart](https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart)
- [Class EmbeddedChartBuilder](https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart-builder)
- [Enum ChartType](https://developers.google.com/apps-script/reference/charts/chart-type.html)
- [グラフのオプション](https://developers.google.com/apps-script/chart-configuration-options)
