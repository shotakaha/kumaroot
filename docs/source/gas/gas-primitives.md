# プリミティブ型したい

## 文字列したい（`string`）

```js
// string
const name = "Taro"
```

```ts
const name: string = "Taro";
```

`""`（もしくは`''`、`` `` ``）で囲んだ文字の並びが`string`型になります。

## 数値したい（`number`）

```js
// number
const count = 42;
const price = 3.14;
```

```ts
const count: number = 42;
const price: number = 3.14;
```

整数・小数を問わず、数値はすべて`number`型として扱われます。
JavaScriptには整数専用の型はありません。

## 真偽値したい（`boolean`）

```js
const isActive = true;
```

```ts
const isActive: boolean = true;
```

`true`または`false`のいずれかの値をとる型です。

## 未定義したい（`undefined`）

```js
let value;
console.log(value);  // -> undefined
```

```ts
let value: number | undefined;
```

宣言だけして値を代入していない変数は`undefined`になります。
明示的に`undefined`を代入することもできます。

## nullしたい（`null`）

```js
const data = null;
```

```ts
const data: string | null = null;
```

「値が存在しない」ことを意図的に表す型です。
`undefined`が「未代入」であるのに対して、`null`は「値がないことを明示的に代入した」状態を表します。

## BigIntしたい（`bigint`）

```js
const big = 12345678901234567890n;
```

```ts
const big: bigint = 12345678901234567890n;
```

`number`型では正確に扱えないほど大きな整数を扱いたいときに使う型です。
数値リテラルの末尾に`n`を付けると`bigint`になります。

## シンボルしたい（`symbol`）

```js
const id = Symbol("id");
```

```ts
const id: symbol = Symbol("id");
```

`Symbol()`を呼ぶたびに、常に一意な値が生成される型です。
オブジェクトのプロパティ名を他と衝突させたくない場合などに使います。

## リテラル型したい

```ts
let status: "success" | "error";
status = "success";  // OK
status = "fail";     // Error
```

リテラル型（literal types）は、
「値そのものを型」として扱うTypeScriptの仕組みです。
文字列（`string`）以外にも数値（`number`）や真偽値（`boolean`）をリテラル型として使えます。

上記のサンプルでは`status`の値として`"success"`と`"error"`がOKとなります。
それ以外の値を代入するとエラーになります。

```ts
type Status = "idle" | "loading" | "success" | "error";

let status: Status = "idle";
```

リテラル型で指定する値が多い場合は、`type`で新しく型名を作成するほうがよいかもしれません。
