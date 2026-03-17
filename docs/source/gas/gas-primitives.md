# プリミティブ型したい

## 文字列したい（`string`）

```js
// string
const name = "Taro"
```

```ts
const name: string = "Taro";
```

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

## 真偽値したい（`boolean`）

```js
const isActive = true;
```

```ts
const isActive: boolean = true;
```

## 未定義したい（`undefined`）

```js
let value;
```

```ts
let value: string | undefined = undefined;
```

## nullしたい（`null`）

```js
const data = null;
```

```ts
const data: string | null = null;
```

## BigIntしたい（`bigint`）

```js
const big = 12345678901234567890n;
```

```ts
const big: bigint = 12345678901234567890n;
```

## シンボルしたい（`symbol`）

```js
const id = Symbol("id");
```

```ts
const id: symbol = Symbol("id");
```

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
