# オブジェクトしたい（`Object`）

```ts
const object: Record<string, string> = {
  key1: "a1",
  key2: "b1",
  key3: "c1",
}
```

`Object`（オブジェクト型）はJavaScriptのビルトイン型のひとつで、
**キー**と**値**の組み合わせ（Key-Value Pair）を持つデータ構造です。
キーに文字列またはシンボルを使用できます。
TypeScriptで型付する場合は
`Record<string, T>`もしくは
`Record<symbol, T>`とします。

## 値を追加したい

```js
const object = new Object();
// ドット記法
object.key1 = "a1";
object.key2 = "b1";
// ブラケット記法
object["key3"] = "c1";

object.key1;  // -> "a1";
```

Objectのプロパティは`.`（ドット記法）もしくは`[]`（ブラケット記法）でアクセスできます。
存在しないプロパティにアクセスした場合は`undefined`になります。



```js
// キーの確認
if ("name" in person) {
    // キーが存在するときの処理
}
```

## 配列にしたい（`Object.keys` / `Object.values` / `Object.entries`）

```ts
// オブジェクト型のキーを配列に変換
const keys = Object.keys(object);
// -> ["key1", "key2", "key3"]

// オブジェクト型の値を配列に変換
const values = Object.values(object);
// -> ["a1", "b1", "c1"]

// オブジェクト型のアイテムを2次元配列に変換
const entries = Object.entries(object);
Object.entries(object);
// [["key1", "a1"], ["key2", "b1"], ["key3", "c1"]]
```

`Object.keys`、`Object.values`、`Object.entries`でオブジェクト型の変数を配列に変換できます。
TypeScriptの場合`as`で型アサーションすると型安全にできます。

## Map型にしたい

```ts
const map = new Map(Object.entries(object));
```

`Object.entries`からMap型に変換できます。

## ループしたい

```js
// for...ofループ
for (const [key, value] of object) {
    console.log(`${key}=${value}`);
}
```

## JSONしたい（`JSON.parse` / `JSON.stringify`）

```js
//
const object = JSON.parse("JSON文字列");

//
const json = JSON.stringify(object);
```

`JSON`クラスを使って、ObjectをJSON文字列に変換したり、
JSON文字列からオブジェクトを生成できたりします。

## リファレンス

- [Object - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object)
- [JSON - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/JSON)
