# ログしたい（`Logger`）

```js
Logger.log("シートを取得");

// 文字列連結
Logger.log("シート名: " + sheetName);

// テンプレートリテラル
Logger.log(`シート名: ${sheetName}`)
```

`Logger`はGAS専用のログクラスです。
出力結果はスクリプトエディターの「実行ログ」で確認できます。

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
GASでも利用でき、スクリプトエディターの「実行ログ」に加えて、
Cloud Loggingとの連携にも対応しています。

`console.info`、
`console.warn`、
`console.error`、
のようにログレベル別に表示を変更できるのが特徴です。

また、実行時間を測定して出力できる
`console.time`、
`console.timeEnd`
もあります。

:::{note}

[GAS公式ドキュメント](https://developers.google.com/apps-script/guides/logging)では、
複数ユーザーが使う本番環境ではCloud Loggingとの連携を前提に、
`Logger`より`console`を使うことがオススメされています。
個人的なスクリプトの動作確認には、手軽な`Logger.log`でも十分です。

:::

## リファレンス

- [console - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/console)
- [Class Logger](https://developers.google.com/apps-script/reference/base/logger)
- [Class console](https://developers.google.com/apps-script/reference/base/console)
