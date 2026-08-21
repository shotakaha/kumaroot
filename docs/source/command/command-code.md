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

## 拡張パッケージを管理したい

```console
$ code --list-extensions
$ code --update-extensions
```

VS Codeに追加した拡張パッケージは、コマンドラインでも確認＆更新できます。
