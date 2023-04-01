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
    ...
    {
        "key": "cmd+b",
        "command": "-markdown.extension.editing.toggleBold",
        "when": "editorTextFocus && !editorReadonly && editorLangId =~ /^markdown$|^rmd$|^quarto$/"
    },
    ...
}
```

{kmd}`cmd + b`はデフォルトではサイドバー表示のON/OFFのトグルなのですが ``All in One Markdown`` プラグインによって、**太字**のトグルに上書きされていました。
``.md``ファイルを編集するときに、不便だったので、削除しました。
