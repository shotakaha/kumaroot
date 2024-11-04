# 日付したい（`Date`）

```js
const now = new Date();
Logger.log(now);
// Mon Nov 04 09:54:29 GMT+09:00 2024
```

`Date`クラスで日付オブジェクトを作成できます。
引数なしで生成すると現在時刻を取得できます。

:::{note}

タイムゾーンはGASのプロジェクト設定（全般設定）で変更できます。

:::

## ISO8601したい

```js
const now = new Date();

// Utilities.formatDate(日付, "タイムゾーン", "表示形式");
const date = Utilities.formatDate(now, "Asia/Tokyo", "yyyy-MM-dd'T'HH:mm:ss.SSSZ");
Logger.info(date);
```

`Utilities.formatDate`で表示形式を変更できます。
``new Date``で取得した現在時刻のタイムゾーンが日本ではありません。
上記サンプルでは、日本の時刻にローカライズして、ISO8601形式で出力しています。

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
