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
Zed 1.16.1 – /Applications/Zed.app
```

`zed`はHomebrewでインストールできます。

## エディターを開きたい

```console
$ zed <ファイル名/ディレクトリ名>

// 現在のウィンドウに追加
$ zed --add <ファイル名/ディレクトリ名>

// 新規ウィンドウで開く
$ zed --new <ファイル名/ディレクトリ名>
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

`--diff`オプションで、2つのファイルの差分をZed上で比較表示できます。
ディレクトリを指定すると、配下の変更されたファイルをまとめて比較表示できます。

## シェル補完したい（`--completions`）

```console
$ zed --completions fish > ~/.config/fish/completions/zed.fish
```

`--completions`オプションで、指定したシェル用の補完スクリプトを生成できます。
`bash`、`elvish`、`fish`、`nushell`、`powershell`、`zsh`に対応しています。
生成したスクリプトをシェルの補完ディレクトリに保存すると、オプション名をタブ補完できるようになります。

## 設定したい（`settings.json`）

```json
// Zed settings
//
// For information on how to configure Zed, see the Zed
// documentation: https://zed.dev/docs/configuring-zed
//
// To see all of Zed's default settings without changing your
// custom settings, run `zed: open default settings` from the
// command palette (cmd-shift-p / ctrl-shift-p)
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

`.config/zed/settings.json`でZedの設定を変更できます。
初回設定時にキーバインド設定などをUIで選択した結果も保存されます。
キーマップは`Emacs`に変更しました。

## コマンドパレットしたい（`Shift-Command-P`）

モダンなエディターと同じように`Shift-Command-P`でコマンドパレットを開くことができます。

## Gitしたい（`git:`）

ZedにはGitコマンドが組み込まれています。
コマンドパレットを起動し、`git:`コマンドを入力するとGitコマンドを実行できます。

## リファレンス

- [Zed](https://zed.dev/)
- [Getting Started - Zed](https://zed.dev/docs/getting-started)
- [Configuring Zed](https://zed.dev/docs/configuring-zed)
