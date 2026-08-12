# クラスしたい（`class`）

```ts
class SimpleFrame {
  private readonly data: Record<string, unknown[]>;

  private constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  static fromColumns(columns: Record<string, unknown[]>): SimpleFrame {
    return new SimpleFrame(columns);
  }

  get headers(): string[] {
    return Object.keys(this.data);
  }
}

const frame = SimpleFrame.fromColumns({ name: ["Alice", "Bob"], age: [25, 30] });
frame.headers;  // -> ["name", "age"]
```

`class`でクラスを定義できます。
上のサンプルは、列指向のデータ（列名 → 値の配列）を保持するだけの最小限のクラスです。

`constructor`は、クラスのインスタンスを初期化するときに呼ばれる関数です。
`this.data = data;`のように、渡された値をインスタンスのプロパティに保存するのが典型的な使い方です。

## プロパティを非公開にしたい（`private`）

```ts
class SimpleFrame {
  private readonly data: Record<string, unknown[]>;
  // ...
}
```

`private`を付けたプロパティは、クラスの外から直接アクセスできません。
`readonly`を組み合わせると、コンストラクター以外での再代入も禁止できます。
内部で保持しているデータを外から書き換えられたくない場合に使います。

:::{hint}

TypeScriptの`private`はコンパイル時のチェックであり、実行時には強制されません。
本当に実行時にもアクセスを禁止したい場合は、
`#data`のようなJavaScript標準の[プライベートフィールド](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes/Private_properties)を使います。

:::

## ファクトリーメソッドしたい（`static`）

```ts
class SimpleFrame {
  private readonly data: Record<string, unknown[]>;

  private constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  static fromColumns(columns: Record<string, unknown[]>): SimpleFrame {
    return new SimpleFrame(columns);
  }
}

const frame = SimpleFrame.fromColumns({ name: ["Alice"] });  // OK
const frame2 = new SimpleFrame({ name: ["Alice"] });         // エラー：コンストラクターがprivate
```

`constructor`に`private`（もしくは`protected`）を付けると、
クラスの外から`new クラス名(...)`で直接インスタンス化できなくなります。
代わりに`static`な**ファクトリーメソッド**（ここでは`fromColumns`）を用意して、
そこから間接的にインスタンスを作らせます。

入力の形式ごとに`fromArrays`・`fromRows`・`fromColumns`のような複数のファクトリーメソッドを用意すると、
それぞれの名前で「何を渡せばよいか」が分かりやすくなります。

## メソッドを追加したい

```ts
class SimpleFrame {
  private readonly data: Record<string, unknown[]>;

  private constructor(data: Record<string, unknown[]>) {
    this.data = data;
  }

  static fromColumns(columns: Record<string, unknown[]>): SimpleFrame {
    return new SimpleFrame(columns);
  }

  select(headers: string[]): SimpleFrame {
    const result: Record<string, unknown[]> = {};
    for (const h of headers) {
      if (!(h in this.data)) {
        throw new Error(`SimpleFrame.select: column "${h}" does not exist`);
      }
      result[h] = this.data[h];
    }
    return new SimpleFrame(result);
  }
}

const frame = SimpleFrame.fromColumns({ name: ["Alice", "Bob"], age: [25, 30] });
const names = frame.select(["name"]);   // 指定した列だけを持つ新しいSimpleFrame
frame.select(["missing"]);              // -> Error: column "missing" does not exist
```

インスタンスメソッド（`select`）の中では、`this`でインスタンス自身のプロパティにアクセスできます。
既存のインスタンスを直接書き換えるのではなく、
`select`の結果として**新しいインスタンスを返す**ようにしておくと、
元のデータを保持したまま加工を連鎖させやすくなります（イミュータブルな設計）。

存在しない列名を指定したときは、`throw`でエラーを投げて早めに気づけるようにしています。

## getterを使いたい（`get`）

```ts
class SimpleFrame {
  // ...
  get headers(): string[] {
    return Object.keys(this.data);
  }
}

const frame = SimpleFrame.fromColumns({ name: ["Alice"], age: [25] });
frame.headers;  // -> ["name", "age"]（メソッドだが () は不要）
```

`get`を付けたメソッドは、プロパティのように`()`なしでアクセスできます。
「保持しているデータから毎回計算して返す値」を、
あたかも普通のプロパティであるかのように見せたいときに使います。

## `prototype`を使った方法

もともとJavaScriptには「クラス」を作る機能がなく、
`prototype`という機能を使って「クラスのような」実装をしていました。
これから新しく作成するスクリプトでは、この書き方を真似する必要はありません。

```js
function SimpleFrame(data) {
    this.data = data;
}

SimpleFrame.fromColumns = function (columns) {
    return new SimpleFrame(columns);
};

SimpleFrame.prototype.select = function (headers) {
    var result = {};
    for (var i = 0; i < headers.length; i++) {
        var h = headers[i];
        if (!(h in this.data)) {
            throw new Error('SimpleFrame.select: column "' + h + '" does not exist');
        }
        result[h] = this.data[h];
    }
    return new SimpleFrame(result);
};
```

`function`自体がコンストラクターの役割を持ち、
`関数名.prototype.メソッド名 = function() {...}`の形でメソッドを追加します。
`static`に相当するものは、関数オブジェクト自体にプロパティを生やして表現します（`SimpleFrame.fromColumns = ...`）。
`private`のようなアクセス制御の仕組みはないため、`this.data`は常に外部から書き換え可能です。

## リファレンス

- [Classes - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes)
- [Private properties - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes/Private_properties)
