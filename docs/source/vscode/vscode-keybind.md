# コマンドパレットしたい

- {kbd}`shift + cmd + p`
- {kbd}`SPC SPC`

VS Codeにおけるコマンドランチャーです。
Emacsの``smex``や``anything/helm``、``ivy``のような役割を担うものです。
VS Codeで唯一覚えるべきショートカットキーといっても過言ではないでしょう。

他のショートカットキーを忘れてしまっても、コマンドパレットを起動すれば、キーワードで検索できます。

## キーバインドを表示したい

- {kbd}`cmd - k` + {kbd}`cmd - s`
- {kbd}`cmd - k` + {kbd}`cmd - r`

## キーバインドを削除したい

```json
{
    {
        "key": "cmd+b",
        "command": "-markdown.extension.editing.toggleBold",
        "when": "editorTextFocus && !editorReadonly && editorLangId =~ /^markdown$|^rmd$|^quarto$/"
    },
}
```

{file}`keybindings.json`を直接編集して、コマンドの先頭に``-``をつけることで、特定のキーバインドを削除できます。

{kbd}`cmd + b`はデフォルトではサイドバー表示のON/OFFのトグル（``workbench.action.toggleSidebarVisibility``）なのですが ``Markdown All in One`` プラグインによって、**太字**のトグル（``markdown.extension.editing.toggleBold``）に上書きされていました。
``.md``ファイルを編集するときに、不便だったので削除しました。
