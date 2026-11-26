# クラスしたい（`class`）

```ts
// PublicClass の定義は下に記載
const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
frame.headers;  // -> ["name", "age"]
frame.length;   // -> 2
```

`new PublicClass(...)`で、クラスのインスタンスを作成できます。
`class`でクラスを定義し、下の節で修飾子を1つずつ足しながら、クラスを育てていきます。

:::{note}

このページのサンプルは、[gaslamp](https://gaslamp.readthedocs.io/en/latest/)の開発で得た経験をもとにしています。

:::

## publicしたい（`public`）

```ts
class PublicClass {
  data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  select(headers: string[]): PublicClass {
    const result: Record<string, unknown[]> = {};
    for (const h of headers) {
      if (!(h in this.data)) {
        throw new Error(`PublicClass.select: column "${h}" does not exist`);
      }
      result[h] = [...this.data[h]];
    }
    return new PublicClass(result);
  }

  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }

  get [Symbol.toStringTag](): string {
    return "PublicClass";
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
const names = frame.select(["name"]);  // 指定した列だけを持つ新しいPublicClass
frame.headers;                         // -> ["name", "age"]
frame.length;                          // -> 2
```

`public`で、publicなプロパティやメソッドを持つクラスを定義できます。
デフォルトで`public`なので、省略できます。
クラスの外から、データもメソッドもプロパティも自由に使えます。
以降の節では、このクラスの一部を抜き出して説明します。

## 初期化したい（`constructor`）

```ts
class PublicClass {
  data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
```

`constructor`は、クラスのインスタンスを初期化するときに呼ばれる関数です。
`this.data = data;`のように、渡された値をインスタンスのプロパティに保存するのが典型的な使い方です。

## メソッドしたい

```ts
class PublicClass {
  // ...
  select(headers: string[]): PublicClass {
    const result: Record<string, unknown[]> = {};
    for (const h of headers) {
      if (!(h in this.data)) {
        throw new Error(`PublicClass.select: column "${h}" does not exist`);
      }
      result[h] = [...this.data[h]];
    }
    return new PublicClass(result);
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
const names = frame.select(["name"]);  // 指定した列だけを持つ新しいPublicClass
frame.select(["missing"]);             // -> Error: PublicClass.select: column "missing" does not exist
```

インスタンスメソッド（`select`）の中では、`this`でインスタンス自身のプロパティにアクセスできます。
既存のインスタンスを直接書き換えるのではなく、
`select`の結果として**新しいインスタンスを返す**ようにしておくと、
元のデータを保持したまま加工を連鎖させやすくなります（イミュータブルな設計）。
列の配列も`[...this.data[h]]`でコピーしておくと、新しいインスタンスと元のインスタンスが配列を共有しません。

存在しない列名を指定したときは、`throw`でエラーを投げて早めに気づけるようにしています。

## メンバー変数したい

```ts
class PublicClass {
  data: Record<string, unknown[]>;  // メンバー変数（プロパティ）
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
frame.data;       // -> { name: ["Alice", "Bob"], age: [25, 30] }
frame.data = {};  // OK：publicなので外から書き換えられてしまう
```

メンバー変数は、インスタンスのプロパティとしてアクセスできます。
`public`のままだと、外から値を読むだけでなく、書き換えることもできてしまいます。
この問題は、次の`readonly`や`private`の節で防ぎます。

## getterしたい（`get`）

```ts
class PublicClass {
  // ...
  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
frame.headers;  // -> ["name", "age"]（メソッドだが () は不要）
frame.length;   // -> 2
```

`get`を付けたメソッドは、プロパティのように`()`なしでアクセスできます。
「保持しているデータから毎回計算して返す値」を、
あたかも普通のプロパティであるかのように見せたいときに使います。

## toStringTagしたい（`Symbol.toStringTag`）

```ts
class PublicClass {
  // ...
  get [Symbol.toStringTag](): string {
    return "PublicClass";
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicClass(columns);
Object.prototype.toString.call(frame);  // -> "[object PublicClass]"
```

`Symbol.toStringTag`というキーを持つgetterを定義すると、
`Object.prototype.toString.call()`の結果にその文字列が使われます。
`instanceof`ではクラスの判定が難しい場合（別のモジュールから読み込んだ場合など）でも、
この文字列でクラスを判定できます。

:::{note}

GASではライブラリーをまたぐと`instanceof`では型を正しく判定できないことがあります。
そのため`Object.prototype.toString.call()`で型の名前を確認する方法を使います。

:::

## privateしたい（`private`）

```ts
class PrivateClass {
  private readonly data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  private hasColumn(name: string): boolean {
    return name in this.data;
  }

  select(headers: string[]): PrivateClass {
    const result: Record<string, unknown[]> = {};
    for (const h of headers) {
      if (!this.hasColumn(h)) {
        throw new Error(`PrivateClass.select: column "${h}" does not exist`);
      }
      result[h] = [...this.data[h]];
    }
    return new PrivateClass(result);
  }

  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PrivateClass(columns);
frame.headers;            // -> ["name", "age"]
frame.data;               // エラー：privateなので外から読めない
frame.hasColumn("name");  // エラー：privateメソッドも外から呼べない
```

`private`を付けたプロパティやメソッドは、クラスの外から直接アクセスできません。
内部で保持しているデータや、外から呼ばれたくない補助メソッドに使います。
上の例では、`hasColumn`を`select`の中だけで使っています。

:::{hint}

TypeScriptの`private`はコンパイル時のチェックであり、実行時には強制されません。
本当に実行時にもアクセスを禁止したい場合は、
`#data`のようなJavaScript標準の[プライベートフィールド](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes/Private_properties)を使います。

:::

## readonlyしたい（`readonly`）

```ts
class PrivateClass {
  private readonly data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;  // OK：コンストラクターでは代入できる
  }

  replace(data: Record<string, unknown[]>): void {
    this.data = data;  // エラー：readonlyなので再代入できない
  }
}
```

`readonly`を付けたプロパティは、コンストラクター以外で再代入できなくなります。
ただし、`readonly`が禁止するのは「別の値を代入すること」だけです。
配列の中身（例：`this.data.name.push(...)`）は変えられるので、
完全に変更できないようにしたい場合は、コピーを返すなどの工夫が必要です。

## staticしたい（`static`）

```ts
class StaticClass {
  private readonly data: Record<string, unknown[]>;

  private constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  static fromColumns(columns: Record<string, unknown[]>): StaticClass {
    return new StaticClass(columns);
  }

  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = StaticClass.fromColumns(columns);  // OK
frame.headers;                                    // -> ["name", "age"]
const frame2 = new StaticClass(columns);          // エラー：コンストラクターがprivate
```

`static`を付けたメソッドは、インスタンスではなくクラスに属します。
`constructor`に`private`（もしくは`protected`）を付けると、
クラスの外から`new クラス名(...)`で直接インスタンス化できなくなります。
代わりに`static`な**ファクトリーメソッド**（ここでは`fromColumns`）を用意して、
そこから間接的にインスタンスを作らせます。
継承先のクラスからも使わせたい場合は、`private`の代わりに`protected`を付けます。

入力の形式ごとに`fromArrays`・`fromRows`・`fromColumns`のような複数のファクトリーメソッドを用意すると、
それぞれの名前で「何を渡せばよいか」が分かりやすくなります。

## prototypeしたい（`prototype`）

```js
function ProtoFrame(data) {
  this.data = data;
}

ProtoFrame.fromColumns = function (columns) {
  return new ProtoFrame(columns);
};

ProtoFrame.prototype.select = function (headers) {
  var result = {};
  for (var i = 0; i < headers.length; i++) {
    var h = headers[i];
    if (!(h in this.data)) {
      throw new Error('ProtoFrame.select: column "' + h + '" does not exist');
    }
    result[h] = this.data[h].slice();
  }
  return new ProtoFrame(result);
};

var columns = { name: ["Alice", "Bob"], age: [25, 30] };
var frame = ProtoFrame.fromColumns(columns);
frame.select(["name"]);  // 指定した列だけを持つ新しいProtoFrame
```

もともとJavaScriptには「クラス」を作る機能がなく、
`prototype`という機能を使って「クラスのような」実装をしていました。
これから新しく作成するスクリプトでは、この書き方を真似する必要はありません。

`function`自体がコンストラクターの役割を持ち、
`関数名.prototype.メソッド名 = function() {...}`の形でメソッドを追加します。
`static`に相当するものは、関数オブジェクト自体にプロパティを生やして表現します（`ProtoFrame.fromColumns = ...`）。
`private`のようなアクセス制御の仕組みはないため、`this.data`は常に外部から書き換え可能です。

## リファレンス

- [Classes - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes)
- [Private properties - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes/Private_properties)
