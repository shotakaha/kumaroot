# 配列したい（`[]` / `Array`）

```js
// JavaScript
const array = ["a1", "a2", "a3"];

// TypeScript
const array: string[] = ["a1", "a2", "a3"];
const array: Array<string> = ["a1", "a2", "a3"];
```

`[]`リテラルで配列を初期化できます。
TypeScriptでは、配列の要素の型名も指定する必要があります。

```js
const array = new Array("a1", "a2", "a3");
```

`new Array()`コンストラクターでも配列を初期化できます。
ただし、引数の扱いに注意が必要なため、通常はリテラル記法で記述すれば問題ありません。

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
const result = arrays.reduce((left, right) => addLists(left, right));
// step1. arrays[0] を初期値として使用
// step2. left=arrays[0], right=arrays[1] を計算
//    -> [5, 7, 9]
// step3. left=直前の結果, right=arrays[2] を計算
//    -> [12, 15, 18]
```

複数の配列を処理する場合`reduce`メソッドを利用すると簡潔にかけます。

## 2次元配列したい（`[][]`）

```ts
// セル用の型を定義
type Cell = string | number | boolean | Date | null;
const values: Cell[][] = sheet.getDataRange().getValues();
```

スプレッドシートにあるデータを取得すると、2次元配列（行x列）として返ってきます。
`Cell`型を定義することで型安全を保つことができます。

```ts
// ヘッダー（header）とデータ（rows）に分割
// ヘッダー = 1行目：文字列に変換（Cell[] -> string[]）
// データ = 2行目以降：型はそのまま（Cell[]）
const header = values[0].map(String);
const rows = values
  .slice(1)
  .filter(row => row.some(cell => cell !== null && cell !== ""));
```

さらに、1行目がヘッダー、2行目以降がデータ領域となっていることが多いです。
ヘッダー（`header`）とデータ（`rows`）に分割しておくとよいです。

:::{hint}

スプレッドシートから取得したデータは `Cell[][]`型となっています。
ヘッダーに相当する1行目も`Cell[]`になっているため、
上記のサンプルでは`string[]`に変換しています。
また、データ領域からは、`["", ""]` や `["", null]`、`[null, null]`のようなどのカラムにも値が入っていない空行を除外しています。

:::

データ（`rows`）は、そのまま2次元配列（`Cell[][]`）として扱えます。
用途に応じて、行アクセス、列アクセス、オブジェクト・Map型への変換などができます。

### 行インデックスでアクセスしたい

```ts
for (const row of rows) {
    const col0 = row[0];
    const col1 = row[1];
}
```

`for...of`で1行（`Cell[]`）ずつ取り出せます。
行の中の値には、さらに列インデックスでアクセスします。

### 列インデックスでアクセスしたい

```ts
// age列（インデックス1）だけを取り出す
const ageColumn: Cell[] = rows.map(row => row[1]);
```

`row[列インデックス]`で特定の列だけを取り出せます。
ただし列の並び順が変わるとインデックスもズレるため、
次の「カラム名でアクセスしたい」のほうが安全です。

### カラム名でアクセスしたい

```ts
function getColumn(rows: Cell[][], header: string[], columnName: string): Cell[] {
  const index = header.indexOf(columnName);
  if (index === -1) {
    throw new Error(`列が見つかりません: ${columnName}`);
  }
  return rows.map(row => row[index]);
}

const ageColumn = getColumn(rows, header, "age");
```

`header.indexOf(カラム名)`で列インデックスを求めてからアクセスすると、
列の並び順が変わってもコードを修正せずに済みます。
存在しないカラム名を指定したときにすぐ気づけるよう、`-1`（見つからない）はエラーにしています。

### 特定のカラムのデータ型をチェックしたい

```ts
function isNumberColumn(rows: Cell[][], header: string[], columnName: string): boolean {
  return getColumn(rows, header, columnName).every(value => typeof value === "number");
}

const ok = isNumberColumn(rows, header, "age");
```

`typeof`と`Array.every`を組み合わせて、列内のすべての値が期待する型かチェックできます。
`getValues()`が返す`Cell[][]`は型が混在しうるため、
集計処理の前にこうしたチェックを挟んでおくと、
数値のつもりが文字列だった、といった事故を早期に検出できます。

### 特定のカラムのデータ内容でフィルタリングしたい

```ts
const ageIndex = header.indexOf("age");
const adults = rows.filter(
  row => typeof row[ageIndex] === "number" && (row[ageIndex] as number) >= 30
);
```

`Array.filter`で、特定カラムの値が条件を満たす行だけを抽出できます。
`Cell`型は`number`以外の型も含むため、
比較演算子を使う前に`typeof`で数値であることを確認しておくと安全です。

### オブジェクトに変換したい

```ts
// ヘッダー名をキーとして利用
const data = rows.map(row =>
  Object.fromEntries(
    header.map( (key, i) => [key, row[i]] )
  )
);
```

`Object.fromEntries`と`header`を組み合わせると、
1行を「カラム名: 値」のオブジェクトに変換できます。
`data[0].age`のようにプロパティ名でアクセスできるようになるので、
列インデックスやカラム名を毎回指定するより読みやすくなります。

### Mapに変換したい

```ts
const maps: Map<string, Cell>[] = rows.map(row =>
  new Map(header.map((key, i) => [key, row[i]]))
);
```

オブジェクトの代わりに`Map`型に変換することもできます。
キーの並び順を保証したい場合や、キーが動的に変わる場合は`Map`のほうが扱いやすいです。

:::{hint}

シートへの書き込み（`setValues`）は、
[セル操作したい（`Range`）](./gas-spreadsheet-range.md)で扱います。

:::

## リファレンス

- [Array - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array)
