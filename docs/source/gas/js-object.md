# オブジェクトしたい（`Object`）

```js
const object = {
    key1: "a1",
    key2: "b1",
    key3: "c1",
}
```

`Object`（オブジェクト型）はJavaScriptにビルトインされている型のひとつで、
**キー**と**値**の組み合わせ（Key-Value Pair）を持つデータ構造です。
キーに文字列またはシンボルを使用できます。

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
Object.keys(object);
// -> ["key1", "key2", "key3"]
```

```js
Object.values(object);
// -> ["a1", "b1", "c1"]
```

```js
Object.entries(object);
// ["key1", "a1"]
// ["key2", "b1"]
// ["key3", "c1"]
```

```js
// キーの確認
if ("name" in person) {
    // キーが存在するときの処理
}
```

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
