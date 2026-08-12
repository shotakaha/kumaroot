# グローバル変数したい（`globalThis`）

```ts
(globalThis as Record<string, unknown>)["myFn1"] = myFn1;
(globalThis as Record<string, unknown>)["myFn2"] = myFn2;
(globalThis as Record<string, unknown>)["myFn3"] = myFn3;
(globalThis as Record<string, unknown>)["myFn4"] = myFn4;

// もしくは
const g = globalThis as Record<string, unknown>;
g["myFn1"] = myFn1;
g["myFn2"] = myFn2;
```

`globalThis`は、ECMAScript標準の**環境に依存しないグローバル変数の置き場所**です。
`src/index.ts`のようなエントリーポイントとなるファイルで、
ほかのモジュールから`export`した関数を`globalThis`に登録しておくとよいです。

とくにGASでは、`rollup`でバンドルすると、関数は内部スコープに閉じ込められてしまいます。
そのままではGASから参照できませんが、`globalThis`に登録することで、外から呼べるようになります。

:::{note}

JavaScriptでは、ブラウザ環境だと`window`、Node環境だと`global`、
のように、環境によってグローバル変数名が違います。
`globalThis`を使えば、環境を気にせずに同じ書き方で利用できます。

:::

## 型安全に登録したい

```ts
import { myFn1, myFn2, myFn3 } from "./module";

interface GASGlobalThis {
  myFn1?: typeof myFn1;
  myFn2?: typeof myFn2;
  myFn3?: typeof myFn3;
}

if (typeof globalThis !== "undefined") {
  const gas = globalThis as unknown as GASGlobalThis;
  gas.myFn1 = myFn1;
  gas.myFn2 = myFn2;
  gas.myFn3 = myFn3;
}
```

`Record<string, unknown>`＋文字列キーの書き方は手軽ですが、
キー名をタイプミスしても型チェックでは検出できません。
公開する関数・クラスの一覧を`interface`として定義しておくと、
存在しないプロパティへの代入がコンパイルエラーになるため、より安全です。

`typeof globalThis !== "undefined"`のガードは、
`globalThis`が存在しない環境（テスト実行時など）でエラーにならないようにするためのものです。

## トリガー関数を登録したい

```ts
(globalThis as Record<string, unknown>)["onFormSubmit"] = onFormSubmit;
(globalThis as Record<string, unknown>)["onEdit"] = onEdit;

// 手動実行する関数は、先頭にアンダースコアを付けて登録する
(globalThis as Record<string, unknown>)["_setupTriggers"] = setupTriggers;
```

[`ScriptApp.newTrigger("関数名")`](./gas-trigger.md)でトリガーを作成する場合、
指定する文字列は`globalThis`に登録したキー名と完全に一致している必要があります。
`onFormSubmit`・`onEdit`のようなイベントハンドラー系の関数は、素の名前のまま登録します。

:::{hint}

Apps ScriptエディターのRunドロップダウン（実行ボタンの隣の関数選択）には、
トップレベルで宣言された関数しか表示されません。
`rollup`でバンドルした`code.js`の中身はすべて内部スコープに隠れてしまうため、
このままではエディターから手動実行できません。

対策として、エディターから直接実行したい関数だけ、別ファイル（例：`stubs.js`）に
以下のような「橋渡し用」のトップレベル関数を用意しておく方法があります。

```js
// stubs.js（clasp pushの対象に含める）
function setupTriggers() {
  globalThis["_setupTriggers"]();
}
```

このとき、バンドル本体（`code.js`）側では実装をアンダースコア付きの名前
（`_setupTriggers`）で登録しておく必要があります。
アンダースコアなしで登録してしまうと、GASがトップレベル宣言を`globalThis`に
巻き上げる際に`stubs.js`側の宣言と衝突し、
スタブが自分自身を呼び出して無限ループ（スタックオーバーフロー）になります。

:::

## リファレンス

- [globalThis - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
