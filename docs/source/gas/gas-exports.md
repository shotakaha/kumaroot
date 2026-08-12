# エクスポートしたい（`export` / `import`）

```ts
// src/sheets.ts
export function highlightRow(
  sheet: GoogleAppsScript.Spreadsheet.Sheet,
  rowIndex: number,
  color: string,
): void {
  sheet.getRange(rowIndex, 1, 1, sheet.getLastColumn()).setBackground(color);
}
```

`export`で、モジュールから関数やクラスを外部に公開できます。
これは[`tsc` + `rollup` + `clasp`](./gas-clasp.md)のワークフローで
ローカル開発する場合の標準的な書き方で、TypeScript・JavaScriptの言語機能そのものです。

:::{note}

`rollup`が`export`/`import`を解決してすべてのモジュールを1つのファイルにバンドルするため、
GAS本体が`export`/`import`に対応している必要はありません。
バンドル後のコードには`export`文自体は残りません。

GASエディターに直接コードを貼り付けて使う場合は事情が異なります。
その場合の書き方は、後述の「GASエディターに直接書きたい場合は」を参照してください。

:::

## まとめてエクスポートしたい（`export *`）

```ts
// src/index.ts（エントリーポイント）
export * from "./sheets";
```

プロジェクトルートにエントリーポイントを作成し、
外向けに公開するAPIをまとめてエクスポートできます。
エントリーポイントには`src/index.ts`のようなファイル名を使うことが多いです。

:::{caution}

`export * from "./sheets.ts"`のように拡張子（`.ts`）を含めて書くと、
`tsconfig.json`の設定によっては`An import path can only end with a '.ts' extension when...`
というエラーになります。
拡張子なし（`"./sheets"`）で書くのが基本です。

:::

## インポートしたい（`import`）

```ts
// src/main.ts
import { highlightRow } from "./sheets";
// もしくは、エントリーポイント経由でまとめて
import { highlightRow } from "./index";
```

`import`で、他のモジュールが`export`した関数やクラスを取り込めます。
`rollup`がバンドル時にこれらを解決するので、
実行時に`require`のような読み込み処理が発生するわけではありません。

## GASエディターに直接書きたい場合は

ここまでの`export`/`import`は、ローカルでTypeScriptを書いて`rollup`でバンドルする前提の書き方です。
GASエディターで直接`.gs`（`.js`）ファイルを編集するスタイルでは事情が異なります。
GASのスクリプトファイルには、標準の`export`/`import`もCommonJSの`require`もありません。
ファイル同士は単に同じグローバルスコープを共有しているだけです。

```js
// Node環境用のエクスポート（GAS環境では無視される）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        ModuleName,
        anotherModuleName,
        someFunction,
    };
}
// GAS環境用のエクスポート（Node環境では無視される）
else {
    this.ModuleName = ModuleName;
    this.anotherModuleName = anotherModuleName;
    this.someFunction = someFunction;
}
```

`module.exports`の有無を確認することで、
Node環境（`jest`などでのテスト実行時）かGAS環境かを区別し、
両方の環境で動くコードを書く、という古典的なテクニックです。
`rollup`を使わずに、ローカルでNode向けにテストしつつ、
同じファイルをそのままGASエディターにも貼り付けたい場合に使われます。

```js
function importClassName() {
    // ClassName が定義されている場合
    if (typeof ClassName !== 'undefined') {
        return new ClassName();
    }

    // ライブラリで定義されている場合
    if (typeof LibraryName !== 'undefined' && LibraryName.ClassName) {
        return new LibraryName.ClassName();
    }

    // requireが使える場合（=Node環境）
    if (typeof require === 'function') {
        try {
            const { ClassName } = require('./ModuleName');
            return new ClassName();
        } catch (e) {
            throw new Error(`ClassName not available via require()`);
        }
    }
    throw new Error(`ClassName is not available in this environment`);
}

const _cn = importClassName();
_cn.someFunction();
```

インポート側も同様に、`typeof`でグローバルに定義されているか、
`require`が使える環境かを実行時に確認してから読み込みます。

:::{hint}

`tsc` + `rollup` + `clasp`のワークフローが組める場合は、
このセクションの書き方をあえて使う必要はありません。
標準の`export`/`import`のほうがシンプルで、型チェックの恩恵も受けられます。

:::

## リファレンス

- [export - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Statements/export)
- [import - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Statements/import)
