# エクスポートしたい（`module.exports`）

```ts
// 内部モジュール: src/sheets.ts
export function highlightRow(
  sheet: GoogleAppsScript.Spreadsheet.Sheet,
  rowIndex: number,
  color: string,
): void {
  sheet.getRange(rowIndex, 1, 1, sheet.getLastColumn()).setBackground(color);
}
```

`export`で、内部モジュールをエクスポートします。

```ts
// 公開API: src/index.ts
export * from "./sheet.ts"
```

プロジェクトルートにエントリーポイントを作成し、
外向けに公開するAPIを設定します。
エントリーポイントには`src/index.ts`や`src/モジュール名/index.ts`というファイル名を使うことが多いです。

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
Node環境かGAS環境かを区別できます。

GASにはエクスポート機能がないため、
すべてをグローバルの下にぶら下げる必要があります。

## インポートしたい

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
```

GASにはインポート機能もありません。
グローバルに定義されたモジュール名（クラス名）の有無を確認し、
必要なところでインスタンスを作成しています。

```js
// 別のGASの先頭で読み込む
const _cn = importClassName();
_cn.someFunction(...);
```

別のGASの先頭で、上記のように読み込むことで、
モジュールにアクセスできるようになります。
