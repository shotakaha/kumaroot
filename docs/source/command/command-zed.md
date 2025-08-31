# Zedしたい（``zed``）

```console
$ brew install --cask zed

$ zed --version
Zed 0.201.8 – /Applications/Zed.app
```

## エディターを開きたい

```console
$ zed <ファイル名/ディレクトリ名>

// 現在のウィンドウに追加
$ zed --add <ファイル名/ディレクトリ名>

// 新規ウィンドウで開く
$ zed --new <ファイル名/ディレクトリ名>
```

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
