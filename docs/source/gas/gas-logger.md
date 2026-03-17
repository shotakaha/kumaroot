# ログしたい（`Logger`）

```js
Logger.log("シートを取得");

// 文字列連結
Logger.log("シート名: " + sheetName);

// テンプレートリテラル
Logger.log(`シート名: ${sheetName}`)
```

`Logger.log`はGAS専用のログ機能です。
実行結果画面でログを確認できます。

機能はシンプルなため、デバッグ用途に最適です。
より複雑なログを取得したい場合は、
スプレッドシートに書き出すなど、
別の方法を検討したほうがよいです。

# ロギングしたい（`console` / `Logger.log`）

```js
console.log("一般的なログ");
console.debug("デバッグのためのログ出力");
console.info("情報のためのログ出力");
console.warn("警告のためのログ出力");
console.error("エラーのためのログ出力");
```

`console`オブジェクトでロギングできます。
よくあるロガーのように、状況に合わせて使い分けるとよいです。

## GASのコンソール出力したい（`Logger.log`）

```js
Logger.log("オブジェクトも含めていろいろ出力");
console.log("一般的なログ");
console.info("情報のためのログ出力");
console.warn("警告のためのログ出力");
console.error("エラーのためのログ出力");
console.time();
console.timeEnd();
```

GASでは利用できる`console`メソッドが上記に限定されています。
また独自の`Logger`クラスも用意されています。

# ログしたい（`Logger.log`）

```js
Logger.log("シートを取得");

// 文字列連結
Logger.log("シート名: " + sheetName);

// テンプレートリテラル
Logger.log(`シート名: ${sheetName}`)
```

`Logger.log`はGAS専用のログ機能です。
実行結果画面でログを確認できます。

機能はシンプルなため、デバッグ用途に最適です。
より複雑なログを取得したい場合は、
スプレッドシートに書き出すなど、
別の方法を検討したほうがよいです。


## リファレンス

- [console - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/console)
