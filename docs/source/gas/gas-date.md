# 日付したい

```js
const date = Utilities.formatDate(日付, "タイムゾーン", "表示形式");
```

日付を取得する場合は[UtilitiesクラスのformatDate](https://developers.google.com/apps-script/reference/utilities/utilities#formatdatedate,-timezone,-format)を使います。

## ISO8601したい

```js
const now = new Date();
const date = Utilities.formatDate(now, "Asia/Tokyo", "yyyy-MM-ddTHH:mm:ssZ");
Logger.info(date);
```

現在時刻は``new Date``で取得できますが、タイムゾーンが日本ではありません。
上記サンプルでは、日本の時刻にローカライズして、ISO8601形式で出力しています。
