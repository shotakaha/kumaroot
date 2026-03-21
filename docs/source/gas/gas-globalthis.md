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
