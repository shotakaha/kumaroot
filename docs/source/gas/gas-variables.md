# 変数したい（`var` / `let` / `const`）

```js
var a = 任意のオブジェクト

// ES6で追加
let b = 再代入できるオブジェクト
const c = 再代入できないオブジェクト
```

変数を宣言する方法は``var``、``const``、``let``の3種類があります。
``var``はどのような変数にも使うことができます。
``const``は再代入ができない変数、``let``は再代入してもよい変数に使います。

もともと``var``しかなかった世界に、``const``と``let``が導入されたみたいです。
プログラミングでは、変数のスコープは最小限にするほうがよいとされています。
なので基本は``const``か``let``を使えばよく、``var``はあまり出番がないでしょう。

:::{hint}

``const``は「定数」というイメージがあったため、**あとから書き換えることができない**ように変数を宣言するときに使うものだと思っていましたが、大きく間違っていました。
あくまで**再代入を禁止**する宣言なので、オプジェクトのプロパティは変更できます。

:::

ウェブで検索したコードは``var``や``const``/``let``が入り混じっています。
``var``になっているものは積極的に``const``に書き換えればよいでしょう。
そこで、エラーがでる場合は``let``に置きかえましょう。
そして、プログラムが動けばOKです。

## 分割代入したい

```js
const person = {
    "name": "John Doe",
    "age": 999,
}

// オブジェクトを分割代入
// - 変数名はプロパティと同じにしなければならない
const {name, age} = person;

// 新しい変数名に分割代入
// - オブジェクトのキーはプロパティと同じにする
// - 値を新しい変数名で受け取ることができる
const {name: anotherName, age: anotherAge} = person;

// 配列に分割代入
// - オブジェクトを配列で受け取ることはできない
const [name, age] = person;  // これはエラーになる
```

複数のプロパティを持つオブジェクトを、アンパックした状態で受け取ることができます。
上のサンプルだとありがたみが分かりづらいですが、
オブジェクトを返り値に持つ関数を受け取るときに便利です。

## 配列型したい（`Array`）

```js
// 配列リテラル
const fruits = ["apple", "banana"];

// Arrayコンストラクタ
const fruits = new Array("apple", "banana");

// 空の配列
const fruits = [];

// 配列に追加
fruits.push("apple");
fruits.push("banana");

// 配列の要素を取得
console.log(fruits[0]);
console.log(fruits[1]);

// 配列の長さ
fruits.length;

// forループ
for (let i = 0; i < fruits.length; i++) {
    // 処理
    const fruit = fruits[i];
    console.log(fruit);
}

// forEachメソッド
const newFruits = fruits.forEach(fruit => {
    // 処理
    console.log(fruit);
    });

// mapメソッド
const newFruits = fruits.map(fruit => {
    // 処理
    return 結果;
})

// filterメソッド
const newFruits = fruits.filter(fruit => {
    // 処理
    return 条件;
})
```

## オブジェクト型したい（`Object`）

```js
// オブジェクトリテラル
const person = {
    name: "Alice",
    age: 25,
    job: "Engineer"
};

// Objectコンストラクター
const person = new Object();
person.name = "Alice";
person.age = 25;
person.job = "Engineer";

// ドット表記法
person.name

// ブラケット記法
person["name"]

// キーの確認
if ("name" in person) {
    // キーが存在するときの処理
}

// キーを取得
const keys = Object.keys(person);

// 値を取得
const values = Object.values(person);

// 要素のペア [キー, 値] を取得
const entries = Object.entries(person);

// for...inループ
for (let key in person) {
    item = `${key}: ${person[key]}`;
    console.log(item);
}

// for...ofループ
for (let [key, value] of entries) {
    const item = `${key}: ${value}`;
    console.log(item);
}
```

オブジェクト型（`Object`）はキーと値の組み合わせ（Key-Value Pair）を持つデータ構造です。
`for...in`でキーをループ、
`for...of`で要素（`[キー, 値]`）をループできます。

## Map型したい（`Map`）

```js
// Mapコンストラクター
const map = new Map();

// 値を追加
map.set("name", "Alice");
map.set("age", 25);
map.set(1, "Number 1");
map.set(true, "Boolean");

// 値を取得
map.get("name");

// 値の削除
map.delete("age");

// サイズの確認
map.size();

// キーの確認
if (map.has(1)) {
    // キーが存在するときの処理
}

// for...ofループ
for (let [key, value] of map){
    const item = `${key}: ${value}`;
    console.log(item);
}
```

Map型は順序を保ったオブジェクト型です。
また、要素数が大きくなったときは、オブジェクト型に比べて高速に動作するそうです。

## Set型したい（`Set`）

```js
// Setコンストラクター
const numbers = [1, 4, 3, 2, 4];
const set = new Set(numbers);

// 値を追加
set.add(10);
set.add(10);
set.add(13);
```

Set型は重複しない値を保持する配列です。

## 型変換したい

```js
// 数値に変換
Number("123");     // -> 123（数値）
Number("123abc");  // -> NaN（変換できない）
Number(true);      // -> 1
Number(false);     // -> 0

// 文字列から数値を抽出
parseInt("42px");      // -> 42
parseFloat("3.14em");  // -> 3.14

// 文字列に変換
String(456);        // -> "456"（文字列）
String(true):       // -> "true"
String([1, 2, 3]);  // -> "1,2,3"

// 真偽値に変換
Boolean(1);        // true
Boolean(0);        // false
Boolean("");       // false（空の文字列はfalse）
Boolean("hello");  // true
Boolean([]);       // true（空の配列はtrue）
Boolean({});       // true（空のオブジェクトはtrue）

// JSON形式の文字列に変換
const data = {...};
JSON.stringify(data);

// 等価演算子／厳密等価演算子
5 == "5";     // true（暗黙の型変換）
5 === "5";    // false（暗黙の型変換されない）
```

型を変換するメソッドも多数用意されています。
JSでは**暗黙の型変換**がデフォルトになっているのですが、これは予期せぬバグを引き起こす可能性があります。
とくに等価演算子を使って条件分岐する際は、
`===`（厳密等価演算子）を使うとよいと思います。
