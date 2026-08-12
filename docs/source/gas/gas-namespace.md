# 名前空間したい

```js
const 名前空間 = {キー: 値};
```

GASプロジェクトの中で、関数はグローバルに定義されます。
そのため、ファイル名を分けても、同じ名前の関数は利用できません。

もし、同じ名前の関数を使用する必要がある場合、
オブジェクト型を使って名前空間（のようなもの）を定義できます。

:::{note}

オブジェクトを使った名前空間の作成は、モジュール（`import`や`require`）が標準化される以前のJavaScriptで一般的な方法だったようです。

:::

```js
// ns1.gs
const ns1 = {
    sameFnName: function (arg) {
        Logger.log("これは ns1 の関数");
    }
};
```

```js
// ns2.gs
const ns2 = {
    sameFnName: function (arg) {
        Logger.log("これは ns2 の関数");
    }
};
```

```js
// ns3.gs
const ns3 = {};
ns3["sameFnName"] = function (arg) {
    Logger.log("これは ns3 の関数");
};
```

```js
// main.gs
function main() {
    ns1.sameFnName();  // -> これは ns1 の関数
    ns2.sameFnName();  // -> これは ns2 の関数
    ns3.sameFnName();  // -> これは ns3 の関数
}
```

:::{caution}

`ns3["sameFnName"]`のようにブラケット記法でキーを指定する場合、
キー名はクォートで囲んだ文字列にする必要があります。
`ns3[sameFnName]`（クォートなし）と書くと、
`sameFnName`という名前の変数を探しにいってしまい、
そのような変数が存在しなければ`ReferenceError`になります。

:::

:::{caution}

GASはV8エンジン対応でモダンなJSを使えるようになりましたが、ES6のモジュールシステムはサポートされてないらしいです。
いろいろがんばればモジュールシステムを使うこともできるようですが、ここでは深追いしません。

:::

## TypeScriptの`namespace`を使いたい

```ts
namespace MyNamespace {
  export function sameFnName(): void {
    Logger.log("これは MyNamespace の関数");
  }
}

MyNamespace.sameFnName();
```

ここまでのオブジェクトを使った書き方とは別に、
TypeScriptには`namespace`という専用の構文があります。
`export`を付けた要素だけが、`名前空間名.要素名`の形で外部から参照できます。

:::{note}

[`@types/google-apps-script`](./gas-typescript.md)の型定義（`GoogleAppsScript.Drive`など）は、
実際にこの`namespace`構文で書かれています。

:::

:::{hint}

TypeScript公式のガイドでは、
[`tsc` + `rollup`](./gas-typescript.md)のようにESModule（`import`/`export`）でモジュールを分割できる環境では、
`namespace`ではなく通常の`export`/`import`を使うことが推奨されています。
GASエディターに直接コードを書くスタイル（モジュールバンドラーを使わない場合）で、
グローバルの汚染を避けたいときの選択肢として覚えておくとよいです。

:::

## リファレンス

- [Namespaces - TypeScript](https://www.typescriptlang.org/docs/handbook/namespaces.html)
