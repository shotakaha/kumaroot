# VS Codeしたい（``code``）

```console
$ brew install --cask visual-studio-code

$ code --version
1.91.0
```

## ディレクトリを開きたい

```console
$ code ディレクトリ名
$ code .
```

ディレクトリ名を指定して、そのディレクトリ関連のファイルを開くことができます。
Gitリポジトリを開いた場合、``.gitignore``に記載したファイルは選択できなくなるなど、よしなに処理してくれます。

## 別のウィンドウで開きたい（``--new-window``）

```console
$ code --new-window ファイル名／ディレクトリ名
```

``--new-window``オプションで、複数のVS Codeウィンドウを開くことができます。

## 拡張パッケージを管理したい

```console
$ code --list-extensions
$ code --update-extensions
```

VS Codeに追加した拡張パッケージは、コマンドラインでも確認＆更新できます。

