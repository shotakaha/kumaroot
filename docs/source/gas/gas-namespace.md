# 名前空間したい

```js
const 名前空間 = {キー: 値};
```

GASエディターで直接`.gs`（`.js`）ファイルを編集していると、
プロジェクト内のすべての関数はファイルをまたいでグローバルに定義されます。
そのため、ファイル名を分けても、同じ名前の関数は共存できません。

もし、同じ名前の関数を使用する必要がある場合、
オブジェクト型を使って名前空間（のようなもの）を定義できます。
これは**言語機能としての名前空間ではなく**、
グローバルな関数名の衝突を避けるための、GASエディター上での実装上の工夫です。

:::{note}

オブジェクトを使った名前空間の作成は、モジュール（`import`や`require`）が標準化される以前のJavaScriptで一般的な方法だったようです。
GASエディターにはモジュールシステムがないため、今でも同じ発想が有効です。

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

GASエディターでは、`ns1.gs`・`ns2.gs`・`ns3.gs`・`main.gs`のようにファイルを分けて保存しても、
1つのプロジェクトとしてすべてまとめて実行されます。
`ns1`・`ns2`・`ns3`はそれぞれ別の変数名なので、
中の`sameFnName`という同じ名前のプロパティが衝突することはありません。

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

## `tsc` + `rollup`が使える場合は

ここまでの「オブジェクトによる疑似的な名前空間」は、
GASエディターに直接コードを書くスタイル特有の工夫です。
[`tsc` + `rollup` + `clasp`](./gas-clasp.md)のワークフローが組める場合は、
そもそもファイルごとにモジュールスコープが分かれるため、
この工夫自体が不要になります。
同じ関数名を別ファイルで使いたい場合は、
[`export`/`import`](./gas-exports.md)で明示的にやり取りすればよく、
グローバルな名前の衝突を意識する必要はありません。

:::{hint}

TypeScriptには`namespace`という専用の構文もあります。
[`@types/google-apps-script`](./gas-typescript.md)の型定義（`GoogleAppsScript.Drive`など）は
実際にこの構文で書かれていますが、
これは型定義パッケージ側の実装の都合によるものです。
自分のプロジェクトのコードでモジュールを分けたい場合は、
`namespace`ではなく`export`/`import`を使うほうが今風です。

:::

## リファレンス

- [Namespaces - TypeScript](https://www.typescriptlang.org/docs/handbook/namespaces.html)
