# 組み込みオブジェクトしたい

```js
const string = "String";
const number = 123;
const array = new Array();
const mapO = new Map();
const set = new Set();
const date = new Date();
```

```{toctree}
js-array
js-map
```

## 集合したい（`Set`）

```js
const set = new Set();
set.add("a1");
set.add("b1");
set.add("a1");  // <- 同じ値を追加しても
```

```js
// 配列を渡してユニークな値を取得する
const set = new Set(["a1", "b1", "a1"]);
```

## 日付したい（`Date`）

```js
const now = new Date();
```

## リファレンス

- [標準組み込みオブジェクト - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects)
