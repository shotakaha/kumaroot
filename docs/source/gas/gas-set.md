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

`add`メソッドで値を追加できます。
すでに存在する値を追加しても無視されるだけで、エラーにはなりません。

## 値を確認・削除したい（`has` / `delete` / `size`）

```js
set.has("a1");       // -> true
set.has("NO_VALUE");  // -> false
```

`has`メソッドで、値が存在するか確認できます。

```js
set.delete("a2");       // -> true
set.delete("NO_VALUE");  // -> false
```

`delete`メソッドで指定した値を削除できます。
返り値は`Boolean`になっているので、削除できたかどうかの判定に利用できます。

```js
set.size;  // -> 2
```

`size`はプロパティ（メソッドではない）で、Setオブジェクトの要素数を取得できます。

## ループしたい

```js
for (const item of set) {
    console.log(item);
}
```

`Set`はそれ自体が反復可能（iterable）なので、`for...of`にそのまま渡せます。

## 配列にしたい

```js
const array = Array.from(set);
// または、スプレッド演算子でも変換できる
const array2 = [...set];
```

`Array.from`もしくはスプレッド演算子（`...`）で配列に変換できます。

## 配列の重複を除去したい

```js
const array = ["a1", "a2", "a1", "a3", "a2"];
const uniqueArray = [...new Set(array)];
// -> ["a1", "a2", "a3"]
```

配列を`Set`に変換してから配列に戻すと、重複した値を除去できます。
`Set`の代表的な使いどころのひとつです。

## 集合演算したい（`union` / `intersection` / `difference`）

```js
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

a.union(b);               // -> Set(4) {1, 2, 3, 4}    和集合
a.intersection(b);        // -> Set(2) {2, 3}          積集合
a.difference(b);          // -> Set(1) {1}             差集合（aのみ）
a.symmetricDifference(b); // -> Set(2) {1, 4}          対称差（どちらか一方のみ）
```

`union`（和集合）、`intersection`（積集合）、`difference`（差集合）、
`symmetricDifference`（対称差）で集合演算ができます。

:::{note}

これらのメソッドはECMAScript2025（ES2025）で追加された比較的新しい機能です。
GAS V8ランタイムでの対応状況は未確認です。
実際に使う前に対象のGASプロジェクトで動作確認してください。

`tsc`で型チェックする場合、`tsconfig.json`の`lib`に`ES2020`しか指定していないと、
これらのメソッドが型エラーになります（`"lib": ["ES2020", "ES2025"]`のように追加が必要です）。

:::

## リファレンス

- [Set - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Set)
