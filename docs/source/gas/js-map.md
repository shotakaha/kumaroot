# Map型したい（`Map`）

```js
const map = new Map([
    ["key1", "a1"],
    ["key2", "b1"],
    ["key3", "c1"],
])
```

`new Map()`コンストラクターでMapを初期化できます。

`Map`型は、ECMAScript2015（ES6）で追加されたビルトイン型で、Object型と同じ、**キー**と**値**の組み合わせ（Key-Value Pair）を持つデータ構造です。

Object型と異なり、プロパティの追加順が保証されています。
また、キーや値にオブジェクトとプリミティブ値を使用できたりします。
大量のデータを扱う場合には、Object型よりパフォーマンスがよいそうです。

## 値を追加したい（`Map.set`）

```js
const map = new Map();
map.set("key1", "a1");
map.set("key2", "b1");
map.set("key3", "c1");
```

`set`メソッドで値（`Key-Value Pair`）を追加できます。

```js
map.get("key1");  // -> a1
```

`get`メソッドでキーを指定して、値を取得できます。

```js
map.delete("key2");
```

`delete`メソッドで指定したキーを削除できます。

```js
// キーの確認
if (map.has("key3")) {
    // キーが存在するときの処理
}
```

`has`メソッドで、キーが存在するか確認できます。

```js
map.size();  // -> 3
```

`size`メソッドで、Mapオブジェクトの要素数を取得できます。

## ループしたい

```js
// for...ofループ
for (const [key, value] of map) {
    console.log(`${key}=${value}`);
}
```

## リファレンス

- [Map - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Map)
