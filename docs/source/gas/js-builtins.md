# 組み込みオブジェクトしたい

```js
const string = "String";
const number = 123;
const array = new Array();
const mapO = new Map();
const set = new Set();
const date = new Date();
```

## 配列したい（`Array`）

## 辞書したい（`Map`）

```js
const map = new Map();
map.set("key1", "value1");
map.set("key2", "value2");
```

```js
// まとめて初期化
const map = new Map( [["key1", "value1"], ["key2", "value2"]]);
```

```js
// Mapオブジェクトの中身を確認
for (const [key, value] of map) {
    console.log(`${key}=${value}`);
}
```

## 集合したい（`Set`）

```js
const set = new Set();
set.add("name1");
set.add("name2");
set.add("name1");  // <- 同じ値を追加しても
```

```js
// 配列を渡してユニークな値を取得する
const set = new Set([...]);
```

## 日付したい（`Date`）

```js
const now = new Date();
```

## リファレンス

- [標準組み込みオブジェクト - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects)
