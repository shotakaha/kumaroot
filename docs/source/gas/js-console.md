# コンソール出力したい（`console`）

```js
console.log("一般的なログ");
console.debug("デバッグのためのログ出力");
console.info("情報のためのログ出力");
console.warn("警告のためのログ出力");
console.error("エラーのためのログ出力");
```

`console`オブジェクトを介して、ブラウザのデバッグコンソールに出力できます。
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

## リファレンス

- [console - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/console)
