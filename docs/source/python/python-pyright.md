# 型チェックしたい（`pyright`）

```console
$ pyright --version
pyright 1.1.383

$ pyright ファイル名 or ディレクトリ名
```

`pyright`はMicrosoftが開発しているPython用の型チェッカーです。

:::{note}

VS Code拡張`Pylance`の内部で使用されています。

:::

## インストールしたい（`pyright`）

- `pipx`でインストール

```console
$ pipx install pyright
```

- `poetry`でインストール

```console
$ poetry add pyright --dev test
```

- `uv`でインストール

```console
$ uv tool install pyright
```

## 設定したい（`pyrightconfig.json`）

```json
{
    "include": ["src"],
    "exclude": ["tests/helpers"],
    "reportMissingImports": true,
    "reportUnusedImports": "warning",
    "typeCheckingMode": "strict"
}
```

`pyrightconfig.json`で設定を変更できます。
プロジェクトルートに配置します。

:::{note}

`Pylance`の場合は、その他のVS Code拡張と同様に`settings.json`で設定できます。

```json
{
    // Pylanceを有効にする
    "python.languageServer": "Pylance",

    // 型チェックのモード
    // "off" | "basic" | "strict"
    "python.analysis.typeCheckingMode": "basic",

    // 解析対象のパスを追加
    "python.analysis.extraPaths": [
        "./src",
        "./tests"
    ],

    // 型スタブ（関数の型定義）を配置するパス
    // C拡張モジュールをラップする場合に必要
    "python.analysis.stubPath": "./typings",

    // インポート解決の挙動
    "python.analysis.autoImportCompletions": true,
    "python.analysis.autoSearchPaths": true,

    // 未使用コードの警告
    "python.analysis.diagnosticSeverityOverrides": {
        "reportUnusedImport": "warning",
        "reportUnusedVariable": "information"
    }
}
```

:::

## リファレンス

- [Pyright](https://microsoft.github.io/pyright/#/)
