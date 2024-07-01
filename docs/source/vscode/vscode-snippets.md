# スニペットしたい

コマンドパレット -> ``Snippets: Insert Snippets``で、スニペットを検索して挿入できます。
ファイル全体をスニペットで置き換える場合は``Snippets: Fill File with Snippets``を使います。
スニペットは拡張パッケージなどで用意されていることもあります。

## 自作したい

- コマンドパレット -> ``Snippets: Configure User Snippets``
- スニペットの種類・言語を選択
  - ``New Global Snippets sile ...`` -> ファイル名を入力（``$VSCODE/User/snippets/ファイル名.code-snippets``）
  - ``New Snippets file for "ワークスペース名"`` -> ファイル名を入力（``.vscode/ファイル名.code-snippets``）
  - 言語名（``cpp`` / ``python`` / ...） -> ``$VSCODE/User/snippets/言語名.json``

:::{note}

``$VSCODE`` = ``$HOME/Library/Application Support/Code/``です

:::

## スニペットの形式

```json
{
    "スニペット名": {
        "scope": "言語モード",
        "prefix": "トリガー文字列",
        "body": [
            スニペットの内容
        ],
        "description": "簡単な説明"
    },
    // --------------------------------------------------
    // User Snippets for Geant4
    // --------------------------------------------------
    "G4cout": {
        "scope": "cpp, markdown",
        "prefix": "g4cout",
        "body": [
            "G4cout << ${1:var} << G4endl;",
        ],
        "description": "G4cout ... G4endl"
    },
    // 複数のスニペット
    "G4debug": {
        "scope": "cpp, markdown",
        "prefix": "g4debug",
        "body": [
            "G4debug << ${1:var} << G4endl;",
        ],
        "description": "G4debug ... G4endl",
    },
    "G4Box": {
        "scope": "cpp, markdown",
        "prefix": "g4box",
        "body": [
            "auto *solid = G4Box{",
            "\t\"${1:pName}\",",
            "\t${2:halfX},",
            "\t${3:halfY},",
            "\t${4:halfZ},",
            "};"
        ],
        "description": "G4Box",
    },
}
```

スニペットは（コメント付き）JSON形式で作成します。
1つのファイルに複数のスニペットを定義できます。

``scope``には言語モードを指定します。言語別スニペットの場合は不要です（たぶん）。
``prefix``にはトリガー文字列を指定します。
``description``には簡単な説明を設定します。
コード補完の候補としてスニペットが表示されるときには、この説明が表示されます。

``body``にはスニペットの内容を記述します。
カーソル位置は``$1``や``$2``で指定できます。
また``${1:変数名}``で名前付きのプレースホルダーにできます。
