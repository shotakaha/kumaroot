# 日付したい（`Date`）

```js
const now = new Date();
Logger.log(now);
// Mon Nov 11 2024 10:37:03 GMT+0900 (Japan Standard Time)

Logger.log(now.toISOString());
// 2024-11-11T01:37:03.620Z

Logger.log(now.toLocaleString());
// 11/11/2024, 10:37:03 AM

Logger.log(now.toLocaleString("ja-JP", {timeZone: "JST"}));
// 2024/11/11 10:37:03
```

JavaScriptの`Date`クラスで日付オブジェクトを操作できます。

:::{note}

タイムゾーンはGASのプロジェクト設定（全般設定）で変更できます。

:::

## 現在時刻したい（`new Date`）

```js
const now = new Date();
console.log(now);
// Mon Nov 11 2024 10:23:23 GMT+0900 (Japan Standard Time)
console.log(now.toISOString());
// 2024-11-11T01:23:23.137Z
```

引数なしで生成すると現在時刻を取得できます。

```js
const year = new Date("2024");
// 2024-01-01T00:00:00.000Z

const date = new Date("2024-11-11");
// 2024-11-11T00:00:00.000Z

const datetime = new Date("2024-11-11 12:34:56");
// 2024-11-11T03:34:56.000Z
```

引数に日時形式の文字列を与えて、Dateオブジェクトに変換できます。

```js
// TZ=+08:00に設定
const now = new Date("2024-11-11 12:34:56.789+08:00");


console.log(now);
// Mon Nov 11 2024 13:34:56 GMT+0900 (Japan Standard Time)
// ↑GASプロジェクトのTZ設定（Asia/Tokyo）に変換されている

console.log(now.toISOString());
// 2024-11-11T04:34:56.789Z
// ↑UTC+00:00に変換されている
```

タイムゾーンを明示した形式の場合、
GASプロジェクトの日時設定や、
UTC時刻に自動で変換されます。

## 表示形式したい（`toLocaleString`）

```js
const now = new Date();
const options = {
    year: "numeric",    // [2-digit, numeric]
    month: "2-digit",   // [2-digit, numeric, long, short]
    day: "2-digit",     // [2-digit, numeric]
    hour: "2-digit",    // [2-digit, numeric]
    minute: "2-digit",  // [2-digit, numeric]
    second: "2-digit",  // [2-digit, numeric]
    fractionalSecondDigits: 3,  // [0, 1, 2, 3]
    hour12: false,  // [false, true]
    timeZone: "Asia/Tokyo",  // [UTC, Asia/Tokyo, ...]
    timeZoneName: "shortOffset",  // [short, long, longOffset, shortOffset, longGeneric, shortGeneric]
    weekday: "long",  // [short, long]
}
console.log(now.toLocaleString("ja-JP", options));
// 2024/11/11月曜日 10時56分32.590秒 GMT+9
```

`Date`オブジェクトの`toLocaleString`で、ロケールに合わせた表示形式に変更できます。
ロケールは`ja-Jp-u-ca-japanese-hc-h12`のような形式で、
言語のユニコード拡張（`ja-Jp-u`）や
和暦（`ca-japanese`）、
12時間制（`hc-h12`）などのオプションを追加できます。

## ISO8601したい（`Utilities.formatDate`）

```js
const now = new Date();

// Utilities.formatDate(日付, "タイムゾーン", "表示形式");
const date = Utilities.formatDate(now, "Asia/Tokyo", "yyyy-MM-dd'T'HH:mm:ss.SSSZ");
Logger.info(date);
```

GASの`Utilities.formatDate`メソッドで、任意の表示形式に変更できます。
上記サンプルでは、現在時刻を日本の時刻にローカライズして、ISO8601形式で出力しています。

| 指定子 | 表示内容 | 型 | 例 |
|---|---|---|---|
| `G` | Era designator | Text | AD |
| `yyyy` | 年（4桁） | Year | 2024 / 24 |
| `MM` | 月（2桁） | Month | 01 - 12 |
| `dd` | 日（2桁） | Number | 01 - 31 |
| `hh` | 時（2桁） | Number | 1 - 24 |
| `mm` | 分（2桁） | Number | 00 - 59 |
| `ss` | 秒（2桁） | Number | 00 - 59 |
| `SSS` | ミリ秒（3桁） | Number | 000 - 999 |
| `E` | 曜日 | Text | Tuesday; Tue |
| `z` | タイムゾーン | General time zone | JST |
| `Z` | タイムゾーン | RFC 822 time zone | +0900 |
| `XX` | タイムゾーン | ISO 8601 time zone | +0900 |

## リファレンス

- [formatDate](https://developers.google.com/apps-script/reference/utilities/utilities?hl=ja#formatDate(Date,String,String))
- [Class SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html)
- [Date - mdn](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Date)
