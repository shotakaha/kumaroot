# 配列したい（`Array`）

```js
// 配列リテラル
const array = ["a1", "a2", "a3"];
```

`[]`リテラルで配列を初期化できます。

```js
const array = new Array("a1", "a2", "a3");
```

`new Array()`コンストラクタでも配列を初期化できます。

## 値を追加したい（`Array.push`）

```js
// 空の配列を作成し、値を追加する
const array = new Array();
array.push("a1");
array.push("a2");
array.push("a3");
```

`.push`で配列に値を追加できます。

```js
// 配列の要素を取得
console.log(array[0]);  // -> a1
console.log(array[1]);  // -> a2
console.log(array[3]);  // -> a3
```

配列のインデックスを指定して、要素を取得できます。

```js
array.length;  // -> 3
for (let i = 0; i < array.length; i++ ) {
    console.log(array[i]);
}
```

`.length`で配列の長さを取得できます。

## ループしたい

```js
// for...ofループ
for (const value of arrays) {
    console.log(value);
}
```

```js
// forEachメソッド
const newArrays = arrays.forEach(value => {
    // 処理
    console.log(value)
})
```

```js
// mapメソッド
const newArrays = arrays.map(value => {
    // 処理
    return 結果;
})
```

```js
// filterメソッド
const newArrays = arrays.filter(value => {
    // フィルター処理
    return 条件;
})
```

## リファレンス

- [Array - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array)
