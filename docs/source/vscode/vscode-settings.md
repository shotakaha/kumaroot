# 設定したい（``settings.json``）

VS Codeでは
「ユーザー設定」
「フォルダー設定」
「ワークスペース設定」
のレベルで設定が変更できます。

コマンドパレットで``settings.json``と検索すると、
次の候補がヒットするので、カスタムしたい項目を選択します。
それぞれのファイル名は以下のように対応しています。

| 設定レベル | コマンド名 | ファイル名 |
|---|---|---|
| デフォルト設定 | ``Preferences: Open Default Settings`` | |
| ユーザー設定 | ``Preferences: Open User Settings`` | ``{$HOME}/Library/Application Support/Code/User/settings.json`` |
| フォルダー設定 | ``Preferences: Open Workspace Settings`` | ``フォルダー名/.vscode/settings.json`` |

「ユーザー設定」に記述した個人の設定は、``Settings Sync``機能により
GitHub（もしくはMS）アカウントを介して、異なるパソコン間で同期できます。

ソースコードをリポジトリで管理している場合、
「フォルダー設定」のファイルを追加しておくと、
プロジェクトメンバーで設定を共通化できます。

## フォントを変えたい

```json
{
    "editor.fontSize": 20,
    "editor.fontFamily": "Monaspace Krypton, PlemolJP, HackGen, Menlo, Consolas, monospace",
}
```

フォントを日本語に対応したプログラミングフォントに変更しておくとよいです。
先頭に書いたフォントが優先されます。

上記のサンプルでは、
フォントサイズは少し大きめに設定してあります。

英文フォントに``Monaspace Krypton``、
和文フォントに``PlemolJP``を適用しています。
また、フォントが見つからなかった場合に備えて、
``HackGen``やOSごとのデフォルト等幅フォント（``monospace``）にフォールバックするようにしてあります。

:::{seealso}

僕が使っている日本語に対応したプログラミングフォントの例です。
フォントはHomebrewで追加しました。

- 和文フォント
  - [白源（HackGen）](https://github.com/yuru7/HackGen)
  - [PlemolJP](https://github.com/yuru7/PlemolJP)
- 英文フォント
  - [Monaspace](https://monaspace.githubnext.com/)

Monaspaceには5種類のフォントがあります。
``Monaspace Krypton``はmechanical sansという形で、ロボットぽくてプログミング用にいいなと思いました。
リガチャ（合字）機能もありますが、有効にしていません。

:::

## テーマを変えたい

```json
{
    "workbench.colorTheme": "Iceberg Light",
}
```

VS Code全体のカラースキームを変更できます。
上記のサンプルでは[cocoponさんのIceberg](https://marketplace.visualstudio.com/items?itemName=cocopon.iceberg-theme)を使っています。

:::{seealso}

- [Iceberg - dark blue color scheme for Vim/NeoVim](https://cocopon.github.io/iceberg.vim/)
- [Iceberg Theme - VS Marketplace](https://marketplace.visualstudio.com/items?itemName=cocopon.iceberg-theme)
- [Philosophy of Iceberg](https://speakerdeck.com/cocopon/creating-your-lovely-color-scheme)

:::

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

## 対応する括弧（ブラケット）したい

```json
{
    "editor.barcketPairColorization.enabled": true,
    "editor.guides.bracketPairs": "active",
}
```

コード中の対応する括弧（ブラケット）を強調表示できます。
HTMLファイルを編集したり、JSONファイルを確認したりする場合に便利です。

## コード補完したい

```json
"editor.inlayHints.enabled": "offUnlessPressed",
```

関数のヒント表示の設定です。
デフォルトは``"on"``ですが、毎回表示されるのも
邪魔だったので``"offUnlessPressed"``にしました。
