# 集合したい（`Set`）

```js
const set = new Set(["a1", "a2", "a1", "a3"]);
```

`new Set()`コンストラクターでSetを初期化できます。
このとき重複した値はひとつに整理されます。

## 値を追加したい（`Set.add`）

```js
const set = new Set();
set.add("a1");
set.add("a2");
set.add("a1");  // <- 同じ値は追加されない
set.add("a3")
```

## ループしたい

```js
for (const item of set) {
    console.log(item);
}
```

## リファレンス

- [Set - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Set)
