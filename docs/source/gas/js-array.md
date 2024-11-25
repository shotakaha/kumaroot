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
    const item = array[i];
    console.log(item);
}
```

`.length`で配列の長さを取得できます。

## 結合したい（`Array.concat`）

```js
const array1 = ["a", "b", "c"];
const array2 = [1, 2, 3];
const array3 = ["7", "8", "9"];
const array4 = array1.concat(array2, array3);
console.log(array4);
// -> ["a", "b", "c", 1, 2, 3, "7", "8", "9"];
```

`concat`メソッドで配列を連結できます。
複数の配列を連結できます。

```js
const array5 = [...array1, ...array2];
console.log(array5);
// -> ["a", "b", "c", 1, 2, 3];
```

スプレッド演算子（`...配列`）でも連結できます。

## ループしたい

```js
// for...ofループ
for (const item of arrays) {
    console.log(item);
}
```

## `forEach`したい

```js
// forEachメソッド
const newArrays = arrays.forEach(item => {
    // 処理
    console.log(item)
})
```

## `map`したい

```js
// mapメソッド
const newArrays = arrays.map(item => {
    // 処理
    return 結果;
})
```

`map`メソッドで配列の要素に対して、同じ処理を適用できます。

```js
// 平方根を計算したい
const numbers = [1, 4, 9, 16];
const sqrtNumbers = numbers.map(Math.sqrt);
console.log(sqrtNumbers);
// -> [1, 2, 3, 4];
```

## `filter`したい

```js
// filterメソッド
const newArrays = arrays.filter(callbackFn);

const newArrays = arrays.filter(item => {
    // フィルター処理
    return 条件;
})
```

`filter`メソッドを使って、配列から条件にマッチした要素を抽出できます。

```js
// 正の数を取得したい
const numbers = [1, -4, 9, -16];
const positives = numbers.filter(num => num > 0);
console.log(positives);
// -> [1, 9];
```

## `reduce`したい

```js
const newScalar = arrays.reduce(callbackFn, initialValue);
```

```js
const numbers = [10, 20, 30, 40];
const sum = numbers.reduce((total, num) => total + num, 0);
const average = sum / numbers.length;
console.log(sum);  // -> 100
console.log(average);  // -> 25
```

## 最大値・最小値したい（`Math.max` / `Math.min`）

```js
const numbers = [10, 20, 5, 40];
const max = Math.max(...numbers);
const min = Math.min(...numbers);
```

`Math.max`、`Math.min`とスプレッド演算子（`...配列名`）を使って、
最大値、最小値を取得できます。

## リファレンス

- [Array - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array)
