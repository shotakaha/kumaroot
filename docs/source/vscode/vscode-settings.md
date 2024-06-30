# 設定したい（``settings.json``）

VS Codeでは
「ユーザー設定」
「フォルダー設定」
「ワークスペース設定」
のレベルで設定が変更できます。
それぞれのファイル名は以下のようになっています。

| 設定レベル | ファイル名 |
|---|---|
| ユーザー設定 | ``{$HOME}/Library/Application Support/Code/User/settings.json`` |
| フォルダー設定 | ``フォルダー名/.vscode/settings.json`` |

「ユーザー設定」に記述した個人の設定は、``Settings Sync``機能により
GitHub（もしくはMS）アカウントを介して、異なるパソコン間で同期できます。

ソースコードをリポジトリで管理している場合、
「フォルダー設定」のファイルを追加しておくと、
プロジェクトメンバーで設定を共通化できます。

コマンドパレットで``settings.json``と検索すると、
次の候補がヒットするので、カスタムしたい項目を選択します。

1. ``Preferences: Open User Settings (JSON)``
2. ``Preferences: Open Workspace Settings (JSON)``

## フォントを変えたい

```json
{
    "editor.fontSize": 15,
    "editor.fontFamily": "HackGen, Menlo, Monaco, 'Courier New', monospace",
}
```

## 編集タブの色を変えたい

```json
{
    "workbench.colorCustomizations": {
        "tab.activeBackground": "#e2a478",
        "tab.activeForeground": "#161821",
        "tab.inactiveBackground": "#c6c8d1",
        "tab.inactiveForeground": "#161821",
    },
}
```

エディター領域に表示される色を変更できます。
上のサンプルでは、編集中のタブが目立つように背景色を変えています。
