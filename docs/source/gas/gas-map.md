# Map型したい（`Map`）

```ts
const map = new Map();
```

`Map`型は、ECMAScript2015（ES6）で追加されたビルトイン型で、Object型と同じ、**キー**と**値**の組み合わせ（Key-Value Pair）を持つデータ構造です。
`new Map()`コンストラクターでMapを初期化できます。

Object型と異なり、プロパティの追加順が保証されています。
また、キーや値にオブジェクトとプリミティブ値を使用できたりします。
大量のデータを扱う場合には、Object型よりパフォーマンスがよいそうです。

```ts
const map = new Map([
  ["key1", "a1"],
  ["key2", "b1"],
  ["key3", "c1"],
])
```

`[key, value]`ペアを要素にもつ2次元配列を与えて初期化できます。

## 値を追加したい（`Map.set`）

```js
const map = new Map();
map.set("key1", "a1");
map.set("key2", "b1");
map.set("key3", "c1");
```

`set`メソッドで値（`Key-Value Pair`）を追加できます。

```js
map.get("key1");    // -> a1
map.get("NO_KEY");  // -> undefined
```

`get`メソッドでキーを指定して、値を取得できます。
存在しないキーを指定した場合は`undefined`になります。

```js
map.delete("key2");    // -> true
map.delete("NO_KEY");  // -> false
```

`delete`メソッドで指定したキーを削除できます。
返り値は`Boolean`になっているので、削除できたかどうかの判定に利用できます。

```js
// キーの確認
if (map.has("key3")) {
    // キーが存在するときの処理
}
```

`has`メソッドで、キーが存在するか確認できます。

```js
map.size;  // -> 3
```

`size`はプロパティ（メソッドではない）で、Mapオブジェクトの要素数を取得できます。

## 値を確認したい

```js
console.log(map);
// -> Map(3) { 'key1' => 'a1', 'key2' => 'b1', 'key3' => 'c1' }

Array.from(map);  // -> [[キー, 値]]
Array.from(map.entries()); // -> [[キー, 値]]
Array.from(map.keys());  // -> [キー]
Array.from(map.values());  // -> [値]
```

`console.log`でそのまま出力すると`Map(要素数) { ... }`の形式で確認できます。
`.keys`、`.values`、`.entries`で`Map`オブジェクトのプロパティを取得できます。
ただし、そのまま出力しても`Map(...) {}`という表示になるだけなので、
配列として中身を確認したい場合は`Array.from`で変換すると見やすいです。

## キー名を変更したい

```js
if (map.has("oldKey")) {
    map.set("newKey", map.get("oldKey"));
    map.delete("oldKey");
}
```

キー名を直接変更するメソッドはありませんが、`has`、`set`、`get`、`delete`を総動員させるとできます。
キーの順番が変更されるので注意が必要です。

## キーの順番をソートしたい

```js
const sorted = [...sourceMap.entries()].sort((a, b) => {
    // キーを文字列として比較
    return a[0].localeCompare(b[0]);
});
const sortedMap = new Map(sorted);
```

`entries()`をスプレッド演算子で配列に変換し、`sort`で並び替えてから、
`new Map()`に渡すとキーの順番をソートし直せます。

## ループしたい

```js
// for...ofループ
for (const [key, value] of map) {
    console.log(`${key}=${value}`);
}
```

`Map`はそれ自体が反復可能（iterable）なので、`Object`と違い`for...of`にそのまま渡せます。

## グループ化したい（`Map.groupBy`）

```js
const people = [
    { name: "Alice", age: 20 },
    { name: "Bob", age: 30 },
    { name: "Carol", age: 20 },
];

const grouped = Map.groupBy(people, (person) => person.age);
// -> Map(2) {
//      20 => [{ name: "Alice", age: 20 }, { name: "Carol", age: 20 }],
//      30 => [{ name: "Bob", age: 30 }]
//    }
```

`Map.groupBy(反復可能なオブジェクト, 条件を定義した関数)`で、
関数の戻り値ごとにグループ化されたMapオブジェクトを作れます。

## 配列にしたい

```js
const entries = Array.from(map.entries());
const keys = Array.from(map.keys());
const values = Array.from(map.values());
```

`Array.from`で配列に変換できます。

## オブジェクトにしたい

```js
const object = Object.fromEntries(map);
console.log(JSON.stringify(object));
```

`Object.fromEntries`でオブジェクトに変換できます。
`Map`自体が反復可能なので`.entries()`は省略できますが、
明示的に書きたい場合は`Object.fromEntries(map.entries())`としても同じ結果になります。

## 特定のキーを取得したい

```js
// 取得したいキー
const filterKeys = new Set(["key1", "key2"]);

// 中間処理
const filtered = Array.from(map.entries()).filter(([key]) => filterKeys.has(key));
// -> [["key1", "a1"], ["key2", "b1"]]

const filteredMap = new Map(filtered);
// -> Map(2) { "key1" => "a1", "key2" => "b1" }
```

`Map.entries`で配列に変換し、`filter`メソッドを使うことで、
Mapオブジェクトから特定のキー（とその値）を抽出できます。

## リファレンス

- [Map - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Map)
