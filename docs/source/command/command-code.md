# VS Codeしたい（`code`）

```console
$ code ファイル名
$ code ディレクトリ名
```

`code`は、Visual Studio Code（VS Code）をコマンドラインから起動するコマンドです。

## インストールしたい（`code`）

```console
$ brew info visual-studio-code
$ brew install --cask visual-studio-code
$ brew upgrade visual-studio-code

$ code --version
1.134.0
110a328ea54b42367b803ec53ee0bf52ef26b419
arm64
```

`code`はHomebrewでインストールできます。
カスク名は`visual-studio-code`です。

## ディレクトリを開きたい

```console
$ code ディレクトリ名
$ code .
```

ディレクトリ名を指定して、そのディレクトリ関連のファイルを開くことができます。
Gitリポジトリを開いた場合、`.gitignore`に記載したファイルは選択できなくなるなど、よしなに処理してくれます。

## 別のウィンドウで開きたい（`--new-window`）

```console
$ code --new-window ファイル名／ディレクトリ名
```

`--new-window`オプションで、複数のVS Codeウィンドウを開くことができます。

## 保存されるまで待ちたい（`-w` / `--wait`）

```console
$ code --wait ファイル名
$ code -w ファイル名
```

`-w`オプションで、開いたファイルが閉じられるまでコマンドの終了を待たせることができます。
`git commit`のエディターに`code --wait`を設定しておくと、コミットメッセージの編集にVS Codeを使えます。

```console
$ git config --global core.editor "code --wait"
```

## 特定の行を開きたい（`-g` / `--goto`）

```console
$ code --goto ファイル名:行番号
$ code -g ファイル名:行番号
```

`-g`オプションで、指定した行にカーソルを合わせた状態でファイルを開けます。
`grep`や`rg`の検索結果（`ファイル名:行番号:内容`）から、該当箇所にそのままジャンプしたいときに便利です。

## 拡張パッケージを管理したい

```console
$ code --list-extensions
$ code --list-extensions --show-versions
$ code --update-extensions
```

VS Codeに追加した拡張パッケージは、コマンドラインでも確認＆更新できます。
`--show-versions`を組み合わせると、インストール済みのバージョンも一緒に確認できます。

```console
$ code --install-extension 拡張機能のID
```

`--install-extension`で、拡張機能をコマンドラインからインストールできます。
拡張機能のID（`${publisher}.${name}`の形式）は、VS Codeの拡張機能ページで確認できます。

## 2つのファイルを比較したい（`-d` / `--diff`）

```console
$ code --diff ファイル名1 ファイル名2
$ code -d ファイル名1 ファイル名2
```

`-d`オプションで、2つのファイルの差分をVS Code上で比較表示できます。

## リファレンス

- [Command Line Interface - Visual Studio Code](https://code.visualstudio.com/docs/configure/command-line)
