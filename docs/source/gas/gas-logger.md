# ログしたい（`Logger`）

```js
Logger.log("シートを取得");

// 文字列連結
Logger.log("シート名: " + sheetName);

// テンプレートリテラル
Logger.log(`シート名: ${sheetName}`)
```

`Logger`はGAS専用のログクラスです。
出力結果は管理画面の「実行ログ」で確認できます。
Cloud Loggingと連携しており、自動で記録されます。

## ログしたい（`console`）

```js
console.log("一般的なログ");
console.debug("デバッグのためのログ出力");
console.info("情報のためのログ出力");
console.warn("警告のためのログ出力");
console.error("エラーのためのログ出力");
console.time();
console.timeEnd();
```

`console`はJS標準のログ機能です。
GASでも利用でき、`Logger`クラスと同じようにCloud Logging連携にも対応しています。

`console.info`、
`console.warn`、
`console.error`、
のようにログレベル別に表示を変更できるのが特徴です。

また、実行時間を測定して出力できる
`console.time`、
`console.timeEnd`
もあります。

## リファレンス

- [console - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/console)
- [Class Logger](https://developers.google.com/apps-script/reference/base/logger)
- [Class console](https://developers.google.com/apps-script/reference/base/console)
