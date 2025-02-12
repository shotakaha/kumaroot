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
const sum = numbers.reduce((left, right) => left + right, 0);
// step1. 初期値を 0 に設定
// step2. left=0, right=10 で計算 -> 10
// step3. left=直前の値, right=20 で計算 -> 30
// step4. left=直前の値, right=30 で計算 -> 60
// step5. left=直前の値, right=40 で計算 -> 100
const average = sum / numbers.length;
console.log(sum);  // -> 100
console.log(average);  // -> 25
```

## `flat`したい

```js
const array1 = [1, 2, [3, 4]];
const array2 = array1.flat();
console.log(array2);
// -> [1, 2, 3, 4];
```

`flat`メソッドで配列を平坦化できます。
引数に平坦化の深さを指定できます。
平坦化する際、配列の空要素は削除されます。

## 最大値・最小値したい（`Math.max` / `Math.min`）

```js
const numbers = [10, 20, 5, 40];
const max = Math.max(...numbers);
const min = Math.min(...numbers);
```

`Math.max`、`Math.min`とスプレッド演算子（`...配列名`）を使って、
最大値、最小値を取得できます。

## 配列同士の演算したい

```js
left = [1, 2, 3];
right = [4, 5, 6];
const added = left.map((value, index) => value + right[index]);
const subtracted = left.map((value, index) => value - right[index]);
const multiplied = left.map((value, index) => value * right[index]);
const divided = left.map((value, index) => value / right[index]);
const modulo = left.map((value, index) => value % right[index]);
const powered = left.map((value, index) => Math.pow(value, right[index]));
```

配列同士の演算はビルトインされていないので、`map`メソッドを使って自分で定義します。

```js
function addLists(left, right) {
    if (left.length !== right.length) {
        throw new Error("Arrays must have the same length.");
    }
    return left.map((value, index) => value + right[index]);
}
```

それぞれ関数にしておくとよさそうです。

```js
const arrays = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
const result = arrays.reduce((left, right) => AddLists(left, right));
// step1. arrays[0] を初期値として使用
// step2. left=arrays[0], right=arrays[1] を計算
//    -> [5, 7, 9]
// step3. left=直前の結果, right=arrays[2] を計算
//    -> [12, 15, 18]
```

複数の配列を処理する場合`reduce`メソッドを利用すると簡潔にかけます。

## リファレンス

- [Array - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array)
