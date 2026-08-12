# フィルターしたい（`filter`）

```js
const people = [
    { name: "Alice", age: 19 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 34 },
    { name: "David", age: 18 },
];

const adults = people.filter(person => person.age >= 20);
// -> [{ name: "Bob", age: 30 }, { name: "Charlie", age: 34 }]
```

`filter`メソッドで、配列から条件を満たす要素だけを抽出できます。
`Array`の基本的な`filter`の使い方は[配列したい（`filter`したい）](./gas-array.md)を参照してください。
このページでは、オブジェクトの配列（シートから読み込んだ行データなど）を
条件でフィルタリングする実用的なパターンをまとめます。

## 複数条件で抽出したい

```js
const people = [
    { name: "Alice", age: 19, active: true },
    { name: "Bob", age: 30, active: false },
    { name: "Charlie", age: 34, active: true },
    { name: "David", age: 18, active: true },
];

// AND条件（&&）
const activeAdults = people.filter(person => person.age >= 20 && person.active);
// -> [{ name: "Charlie", age: 34, active: true }]
```

`&&`（AND）や`||`（OR）を組み合わせて、複数の条件を1つの式にまとめられます。
条件が複雑になってきたら、条件式を別の関数に切り出すと読みやすくなります。

```js
function isActiveAdult(person) {
    return person.age >= 20 && person.active;
}

const activeAdults = people.filter(isActiveAdult);
```

## リストに含まれるかどうかで抽出したい（`includes`）

```js
const targetNames = ["Alice", "David"];
const targeted = people.filter(person => targetNames.includes(person.name));
// -> [{ name: "Alice", ... }, { name: "David", ... }]
```

`Array.includes`と組み合わせると、
特定の値のリストに含まれる要素だけを抽出できます。
スプレッドシートで選択したIDや名前の一覧を元に絞り込みたい場合などに便利です。

## リファレンス

- [Array.prototype.filter() - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
