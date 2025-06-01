# トランスパイルしたい（`tsc`）

```console
$ npm install --save-dev typescript

// すべてのファイルを変換（tsconfig.json）
$ npx tsc

// 単一ファイルを変換
$ npx tsc example.ts
```

`tsc`はTypeScriptをJavaScriptに変換するコマンドです。
この変換作業はトランスパイルと呼ばれます。

## 型をつけたい

```ts
// 変数の定義
const 変数名: 型名 = 値

// 関数の定義
function 関数名(引数名: 型名): 戻り値の型名 {...}
```

`: 型名`で変数や関数の型を指定できます。
この型を使って、トランスパイルや静的解析で潜在的なエラーを検出します。

:::{note}

トランスパイルしたあとのJavaScriptには型の情報は残りません。

:::

## 設定したい（`tsconfig.json`）

```json
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "CommonJS",
        "outDir": "dist",
        "rootDir": "src",
        "strict": true
    },
    "include": [
        "src/**/*"
    ],
    "exclude": [
        "node_modules",
        "coverage",
    ]
}
```

トランスパイル時の設定は`tsconfig.json`に保存します。
