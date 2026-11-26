# クラスしたい（`class`）

```ts
// PublicFrame の定義は下に記載
const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
frame.headers;  // -> ["name", "age"]
frame.length;   // -> 2
```

`class`は、データ（プロパティ）と処理（メソッド）をひとまとめにする仕組みです。
`class`が設計図で、`new`で作った実物がインスタンスです。
上の`new PublicFrame(...)`は、`PublicFrame`クラスのインスタンスを作っています。

GASでシートを読むと、`getValues()`は列名のない2次元配列になります。
列名で扱えるように、データと処理をまとめたものがクラスです。

このページでは、次の順に説明します。
`public` → `readonly` → `private` → `protected` → `static` → `prototype`

:::{note}

このページのコードはTypeScriptです。GASのエディターにそのまま貼っても動きません。
[`tsc`](./gas-typescript.md)でJavaScriptに変換してから、[`clasp`](./gas-clasp.md)でGASに送ります。

:::

:::{note}

このページのサンプルは、[gaslamp](https://gaslamp.readthedocs.io/en/latest/)（GASでデータフレームを扱うライブラリー）の開発で得た経験をもとにしています。

:::

## publicしたい（`public`）

```ts
class PublicFrame {
  data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {  // 詳しくは「初期化したい」
    this.data = data;
  }

  select(headers: string[]): PublicFrame {       // 詳しくは「メソッドしたい」
    // ...
  }

  get headers(): string[] {                      // 詳しくは「getterしたい」
    return Object.keys(this.data);
  }

  get length(): number {                         // 詳しくは「getterしたい」
    return Object.values(this.data)[0]?.length ?? 0;
  }

  get [Symbol.toStringTag](): string {           // 詳しくは「toStringTagしたい」
    return "PublicFrame";
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
const names = frame.select(["name"]);  // 指定した列だけを持つ新しいPublicFrame
frame.headers;                         // -> ["name", "age"]
frame.length;                          // -> 2
```

`public`は、プロパティやメソッドを外から使えるようにするキーワードです。
何も付けなければ`public`になるので、省略できます。
このクラスは、データもメソッドもプロパティも、クラスの外から自由に使えます。

この後の「初期化したい」から「toStringTagしたい」までは、このクラスの一部を抜き出して説明します。

## 初期化したい（`constructor`）

```ts
class PublicFrame {
  data: Record<string, unknown[]>;  // 詳しくは「メンバー変数したい」

  constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
```

`constructor`は、クラスのインスタンスを初期化するときに呼ばれる関数です。
`this.data = data;`のように、渡された値をインスタンスのプロパティに保存するのが典型的な使い方です。

## メソッドしたい

```ts
class PublicFrame {
  // ...
  select(headers: string[]): PublicFrame {
    const result: Record<string, unknown[]> = {};
    for (const h of headers) {
      if (!(h in this.data)) {
        throw new Error(`PublicFrame.select: column "${h}" does not exist`);
      }
      result[h] = [...this.data[h]];
    }
    return new PublicFrame(result);
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
const names = frame.select(["name"]);  // 指定した列だけを持つ新しいPublicFrame
frame.select(["missing"]);             // -> Error: PublicFrame.select: column "missing" does not exist
```

メソッドは、クラスの中に書いた関数です。
`this`で、インスタンス自身のプロパティにアクセスできます。
存在しない列名を指定したときは、`throw`でエラーを投げて、早めに気づけるようにしています。

:::{hint}

`select`は、元のインスタンスを書き換えず、**新しいインスタンスを返す**ようにしています。
このような設計を**イミュータブル**（変更できない）な設計と呼びます。
元のデータを保持したまま、加工を連鎖させやすくなります。

また、列の配列も`[...this.data[h]]`でコピーしています。
コピーしないと、新しいインスタンスと元のインスタンスが配列を共有してしまうためです。

:::

## メンバー変数したい

```ts
class PublicFrame {
  data: Record<string, unknown[]>;  // メンバー変数（プロパティ）
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
frame.data;       // -> { name: ["Alice", "Bob"], age: [25, 30] }
frame.data = {};  // OK：publicなので外から書き換えられてしまう
```

メンバー変数は、インスタンスのプロパティとしてアクセスできます。
`public`のままだと、外から値を読むだけでなく、書き換えることもできてしまいます。
この問題は、この後の`readonly`や`private`の節で防ぎます。

## getterしたい（`get`）

```ts
class PublicFrame {
  // ...
  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
frame.headers;  // -> ["name", "age"]（メソッドだが () は不要）
frame.length;   // -> 2
```

`get`を付けたメソッドは、プロパティのように`()`なしでアクセスできます。
「保持しているデータから毎回計算して返す値」を、
あたかも普通のプロパティであるかのように見せたいときに使います。

## toStringTagしたい（`Symbol.toStringTag`）

```ts
class PublicFrame {
  // ...
  get [Symbol.toStringTag](): string {
    return "PublicFrame";
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PublicFrame(columns);
Object.prototype.toString.call(frame);  // -> "[object PublicFrame]"
```

`Symbol.toStringTag`というキーを持つgetterを定義すると、
`Object.prototype.toString.call()`の結果にその文字列が使われます。
`Symbol`は、プロパティのキーとして使える特別な値です。
`Symbol.toStringTag`は、JavaScriptが決めている特別なキーです。
`Object.prototype.toString.call()`は、値の型名を調べるための標準的な関数です。

`instanceof`ではクラスの判定が難しい場合（別のモジュールから読み込んだ場合など）でも、
この文字列でクラスを判定できます。

:::{note}

GASのライブラリーをまたぐと、`instanceof`では型を正しく判定できないことがあります。
そのため`Object.prototype.toString.call()`で型の名前を確認する方法を使います。

:::

## readonlyしたい（`readonly`）

```ts
class PublicFrame {
  readonly data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;  // OK：コンストラクターでは代入できる
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const otherColumns = { name: ["Carol"], age: [40] };
const frame = new PublicFrame(columns);
frame.data = otherColumns;  // エラー：readonlyなので再代入できない
```

`readonly`を付けたプロパティは、コンストラクター以外で再代入できなくなります。
前の「メンバー変数したい」の例では`frame.data = {}`が書けましたが、`readonly`を付けると書けなくなります。

ただし、`readonly`が禁止するのは「別の値を代入すること」だけです。
配列の中身（例：`frame.data.name.push(...)`）は変えられるので、
完全に変更できないようにしたい場合は、コピーを返すなどの工夫が必要です。

## privateしたい（`private`）

```ts
class PrivateFrame {
  private readonly data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  private hasColumn(name: string): boolean {
    return name in this.data;
  }

  select(headers: string[]): PrivateFrame {
    const result: Record<string, unknown[]> = {};
    for (const h of headers) {
      if (!this.hasColumn(h)) {
        throw new Error(`PrivateFrame.select: column "${h}" does not exist`);
      }
      result[h] = [...this.data[h]];
    }
    return new PrivateFrame(result);
  }

  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new PrivateFrame(columns);
frame.headers;            // -> ["name", "age"]
frame.data;               // エラー：privateなので外から読めない
frame.hasColumn("name");  // エラー：privateメソッドも外から呼べない
```

`private`を付けたプロパティやメソッドは、クラスの外から直接アクセスできません。
内部で保持しているデータや、外から呼ばれたくない補助メソッドに使います。
上の例では、`hasColumn`を`select`の中だけで使っています。

`readonly`と組み合わせた`private readonly`にすると、外からのアクセスも再代入も防げます。

:::{hint}

TypeScriptの`private`はコンパイル時のチェックであり、実行時には強制されません。
本当に実行時にもアクセスを禁止したい場合は、
`#data`のようなJavaScript標準の[プライベートフィールド](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes/Private_properties)を使います。

:::

## protectedしたい（`protected`）

```ts
class ProtectedFrame {
  protected readonly data: Record<string, unknown[]>;

  constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }
}

class ChildFrame extends ProtectedFrame {
  get firstHeader(): string | undefined {
    return Object.keys(this.data)[0];  // OK：継承先のクラスからはアクセスできる
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const frame = new ChildFrame(columns);
frame.firstHeader;  // -> "name"
frame.data;         // エラー：protectedなので外から読めない
```

`protected`を付けたプロパティやメソッドは、そのクラスの中と、継承先のクラスの中からアクセスできます。
継承先のクラスは、`extends`で既存のクラスを引き継いで作ります。
`private`と違って、継承先のクラスからは使えます。
クラスの外からは、`private`と同じくアクセスできません。

## staticしたい（`static`）

```ts
class StaticFrame {
  private readonly data: Record<string, unknown[]>;

  private constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  static fromColumns(columns: Record<string, unknown[]>): StaticFrame {
    const lengths = new Set(Object.values(columns).map((col) => col.length));
    if (lengths.size > 1) {
      throw new Error("StaticFrame.fromColumns: all columns must have the same length");
    }
    return new StaticFrame(columns);
  }

  get headers(): string[] {
    return Object.keys(this.data);
  }

  get length(): number {
    return Object.values(this.data)[0]?.length ?? 0;
  }
}

const columns = { name: ["Alice", "Bob"], age: [25, 30] };
const invalidColumns = { name: ["Alice"], age: [25, 30] };
const frame = StaticFrame.fromColumns(columns);        // OK
frame.headers;                                          // -> ["name", "age"]
const frame2 = new StaticFrame(columns);                // エラー：コンストラクターがprivate
StaticFrame.fromColumns(invalidColumns);                // エラー：列の長さが違う
```

`static`を付けたメソッドは、インスタンスではなくクラスに属します。
そのため、`StaticFrame.fromColumns(...)`のように、`new`を使わずにクラス名から呼び出せます。

`constructor`に`private`（もしくは`protected`）を付けると、
クラスの外から`new クラス名(...)`で直接インスタンス化できなくなります。
代わりに`static`な**ファクトリーメソッド**（ここでは`fromColumns`）を用意して、
そこから間接的にインスタンスを作らせます。
継承先のクラスからも使わせたい場合は、`private`の代わりに`protected`を付けます。

入力の形式ごとに`fromArrays`・`fromRows`・`fromColumns`のような複数のファクトリーメソッドを用意すると、
それぞれの名前で「何を渡せばよいか」が分かりやすくなります。

また、ファクトリーメソッドを追加するだけで、新しい入力形式に簡単に対応できます。
さらに、ファクトリーメソッドの中で入力値をチェックすれば、
インスタンスを作る前に不正な入力を見つけて、エラーにできます。
上の例では、列の長さがそろっていない入力を`throw`で弾いています。

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
