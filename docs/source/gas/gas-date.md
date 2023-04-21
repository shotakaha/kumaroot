# 日付したい

```js
const date = Utilities.formatDate(日付, "タイムゾーン", "表示形式");
const now = Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy-MM-dd HH:mm:DD");
Logger.info(now);
```

日付を取得する場合は[UtilitiesクラスのformatDate](https://developers.google.com/apps-script/reference/utilities/utilities#formatdatedate,-timezone,-format)を使います
