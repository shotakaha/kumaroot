# 組み込みオブジェクトしたい

```js
const string = "String";
const number = 123;
const array = new Array();
const mapO = new Map();
const set = new Set();
const date = new Date();
```

GASはV8ランタイムを採用しているため、
基本的には最新のJavaScript（=ES2020以降）のビルトイン型（標準オブジェクト）が使えます。

```{toctree}
gas-primitives
gas-array
gas-object
gas-map
gas-set
```

## 日付したい（`Date`）

```js
const now = new Date();
```

## リファレンス

- [標準組み込みオブジェクト - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects)
