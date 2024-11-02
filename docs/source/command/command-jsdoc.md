# JSDocしたい（`jsdoc`）

```console
$ jsdoc ./パス/**/*.js
$ jsdoc -c 設定.json -d ./出力先 ./パス/**/*.js
```

`jsdoc`でJavaScriptのdocstringからドキュメントを作成できます。

## インストールしたい（`jsdoc`）

```console
$ brew install jsdoc3
$ jsdoc --version
JSDoc 4.0.4 (Sat, 19 Oct 2024 19:05:34 GMT)
```

## 設定ファイルしたい（`conf.json`）

```json
{
  "source": {
    "include": ["パス1", "パス2"],
    "includePattern": ".+\\.js$"
  },
  "opts": {
    "destination": "./docs/jsdoc",
    "recurse": true,
    "template": "templates/default"
  }
}
```

`conf.json`でJSDocのオプションを設定できます。

## ドキュメントしたい

```js
/**
 * 関数の説明
 *
 * @param {型} 引数名 - 説明
 * @return {型} 返り値 - 説明
 * /
function 関数名(引数) { ... }
```

- `string`: 文字列
- `number`: 数値
- `boolean`: 真偽値
- `undefined`: 未定義
- `null`: ヌル型
- `symbol`: シンボル型
- `Object`: オブジェクト型
- `Array.<型>`: 配列オブジェクト型
- `Function`: 関数オブジェクト型
- `Date`: 日付オブジェクト型
- `any`: 任意の型
- `型1|型2`: ユニオン型

## リファレンス

- [JSDoc](https://jsdoc.app/)
