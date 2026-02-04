# キーバインドを表示したい（``command+k`` + ``command+s``）

- {kbd}`command+k` + {kbd}`command+s`: `Preferences: Open Keyboard Shortcuts`
- {kbd}`command+k` + {kbd}`command+r`: `Help: Keyboard Shortcuts Reference`

## キーバインドを追加したい

```json
[
    {
        "key": "...",
        "command": "...",
        "when": "..."
    },
]
```

キーバインド設定は`keybindings.json`に上記のJSON形式で追加できます。
`key`フィールドにショートカットキー、
`command`フィールドに実行するコマンド、
`when`フィールドには実行時の条件（＝コンテクスト）を記述します。

:::{note}

`when`フィールドの設定はオプションですが、
カスタムのキーバインドを設定する場合には、
なるべくコンテクストを制限しておくほうが安全です。

:::

## キーバインドを上書きしたい

## キーバインドを無効にしたい

```json
{
    {
        "key": "cmd+b",
        "command": "-markdown.extension.editing.toggleBold",
        "when": "editorTextFocus && !editorReadonly && editorLangId =~ /^markdown$|^rmd$|^quarto$/"
    },
}
```

特定のキーバインドを削除したい場合は、{file}`keybindings.json`を直接編集します。
削除したいコマンドの先頭に``-``をつけます。

上記のサンプルでは、``.md``ファイル編集時の{kbd}`command + b`の動作を無効にしています。

{kbd}`command + b`はデフォルトではサイドバー表示のON/OFFをトグル（``workbench.action.toggleSidebarVisibility``）するキーバインドです。
しかし、``Markdown All in One``拡張を使っていたため、**太字**のトグル（``markdown.extension.editing.toggleBold``）に上書きされていました。
``.md``ファイルを編集するときにだけ挙動が変わるのが不便だったので削除しました。
