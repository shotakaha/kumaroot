# 型チェックしたい（`pyright`）

```console
$ pyright --version
pyright 1.1.411

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
$ poetry add pyright --group test
```

- `uv`でインストール

```console
$ uv tool install pyright
```

## 設定したい（`[tool.pyright]`）

```toml
[tool.pyright]
include = ["src"]
exclude = ["tests/helpers"]
reportMissingImports = true
reportUnusedImport = "warning"
typeCheckingMode = "strict"
```

`pyright`の設定は、`pyproject.toml`の`[tool.pyright]`セクションで変更できます。
キー名はJSON版の`pyrightconfig.json`と同じですが、TOMLの書式（`キー = 値`）で書きます。

:::{note}

独立した`pyrightconfig.json`ファイルでも同じ内容を設定できます。
`pyrightconfig.json`が存在する場合は、そちらが優先されます。

:::

## VS Codeで使いたい（`Pylance`）

`Pylance`は、内部で`pyright`を使っているVS Code拡張です。
CLIやCIでは`pyrightconfig.json`を使いますが、
VS Code上でリアルタイムに解析させる場合は、
その他のVS Code拡張と同様に`settings.json`で設定します。

```json
{
    // Pylanceを有効にする
    "python.languageServer": "Pylance",

    // 型チェックのモード
    // "off" | "basic" | "standard" | "strict"
    "python.analysis.typeCheckingMode": "standard",

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

:::{note}

`pyrightconfig.json`と`settings.json`は、どちらも同じ`pyright`エンジンを設定するものですが、
キー名の書式が異なります（例：`typeCheckingMode`と`python.analysis.typeCheckingMode`）。
両方を用意している場合、`pyrightconfig.json`（や`pyproject.toml`の`[tool.pyright]`）の設定が優先されます。
`pyrightconfig.json`が存在するフォルダーは、開発者ごとに設定がバラつかず、
誰が開いても同じエラーセットになることを意図した設計です。

:::

## リファレンス

- [Pyright](https://microsoft.github.io/pyright/#/)
- [Pylance - VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
