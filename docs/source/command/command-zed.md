# Zedしたい（`zed`）

```console
$ zed ファイル名
$ zed ディレクトリ名
```

`zed`は、Rust製のモダンなエディターです。

## インストールしたい（`zed`）

```console
$ brew search zed
$ brew install --cask zed
$ brew upgrade zed

$ zed --version
Zed 1.23.2 – /Applications/Zed.app
```

`zed`はHomebrewでインストールできます。

## エディターを開きたい

```console
$ zed <ファイル名/ディレクトリ名>

// 現在のウィンドウに追加
$ zed --add <ファイル名/ディレクトリ名>
$ zed -a <ファイル名/ディレクトリ名>

// 新規ウィンドウで開く
$ zed --new <ファイル名/ディレクトリ名>
$ zed -n <ファイル名/ディレクトリ名>
```

## 特定の行を開きたい（`path:line:column`）

```console
$ zed ファイル名:行番号
$ zed ファイル名:行番号:列番号
```

`ファイル名:行番号`の書式で、指定した行にカーソルを合わせた状態でファイルを開けます。
`grep`や`rg`の検索結果からジャンプしたいときに便利です。

## 保存されるまで待ちたい（`-w` / `--wait`）

```console
$ zed --wait ファイル名
$ zed -w ファイル名
```

`-w`オプションで、開いたファイルが閉じられるまでコマンドの終了を待たせることができます。
`git commit`のエディターに`zed --wait`を設定しておくと、コミットメッセージの編集にZedを使えます。

```console
$ git config --global core.editor "zed --wait"
```

## 既存ウィンドウで開きたい（`-e` / `--existing`）

```console
$ zed --existing ファイル名
$ zed -e ファイル名
```

`-e`オプションで、新規ウィンドウを作らずに既存のZedウィンドウでファイルを開けます。

## 2つのファイルを比較したい（`--diff`）

```console
$ zed --diff ファイル名1 ファイル名2
```

`--diff`オプションで、2つのファイルの差分を表示できます。
ディレクトリを指定すると、変更されたファイルをまとめて比較表示できます。

## シェル補完したい（`--completions`）

```console
$ zed --completions fish > ~/.config/fish/completions/zed.fish
```

`--completions`オプションで、指定したシェル用の補完スクリプトを生成できます。
`bash`、`elvish`、`fish`、`nushell`、`powershell`、`zsh`をサポートしています。
生成したスクリプトをシェルの補完ディレクトリに保存すると、オプション名をタブ補完できるようになります。

## 設定したい（`settings.json`）

```json
{
  "base_keymap": "Emacs",
  "ui_font_size": 16,
  "buffer_font_size": 15,
  "theme": {
    "mode": "system",
    "light": "One Light",
    "dark": "One Dark"
  }
}
```

Zedの設定は`.config/zed/settings.json`で変更できます。
初回起動時に選択したキーマップなども、ここに保存されます。
上記サンプルではキーマップを`Emacs`に変更しました。

## コマンドパレットしたい（`Shift-Command-P`）

`Shift-Command-P`でコマンドパレットを開きます。

## Gitしたい（`git:`）

コマンドパレットに`git:`と入力すると、Gitの操作を実行できます。

```console
// 状態を確認する
git panel: toggle focus

// ステージする
git: stage all
git: unstage all

// コミットする
git: commit

// 差分を確認する
git: diff

// リモートと同期する
git: pull
git: push

// ブランチを操作する
git: branch
git: switch
```

`git panel: toggle focus`でGitパネルを開くと、変更されたファイルとステージ状態を一覧できます。
`git: diff`では、プロジェクト全体の差分をまとめて確認できます。

## Claude Codeしたい（`agent:`）

```console
// ACP Registryを開く（Claude Agentをインストールする）
zed: acp registry

// スレッドを新規作成する
agent: new thread

// エージェントの設定を開く
agent: open settings
```

Zedでは、Claude Codeを外部エージェント（Claude Agent）として利用できます。

1. `zed: acp registry`を実行し、ACP RegistryからClaude Agentをインストールする
2. Agentパネルの新規スレッドのメニューから、Claude Agentを選ぶ
3. スレッド内で`/login`を実行し、課金方法を選ぶ

:::{note}
Claude Agentは、認証と課金をZedのエージェントとは別に管理します。
Zedのエージェント用に設定したAnthropic APIキーは引き継がれません。
:::

## GitHub Copilotしたい（`editor:`）

```json
{
  "edit_predictions": {
    "provider": "copilot"
  }
}
```

Zedでは、GitHub Copilotをエディター内の補完（Edit Prediction）として利用できます。
`settings.json`で、補完のプロバイダーを`copilot`にします。

サインインはステータスバーのCopilotアイコンから行います。
表示されたデバイスコードを、GitHubの認証ページに入力します。

```console
// 補完を手動で表示する
editor: show edit prediction

// 次の候補に切り替える
editor: next edit prediction

// 前の候補に切り替える
editor: previous edit prediction
```

表示された補完は`alt-tab`で採用できます。

## リファレンス

- [Zed](https://zed.dev/)
- [Git - Zed](https://zed.dev/docs/git)
- [External Agents - Zed](https://zed.dev/docs/ai/external-agents)
- [Edit Prediction - Zed](https://zed.dev/docs/ai/edit-prediction)
- [Getting Started - Zed](https://zed.dev/docs/getting-started)
- [Configuring Zed](https://zed.dev/docs/configuring-zed)
