# find -- walk a file hierarchy

```shell
find ディレクトリ 検索文字列
```

- ディレクトリ名の末尾の``/ (trailing-slash)``はつけなくてOK

## ファイルの種類を指定して検索したい

```shell
find ディレクトリ -type f  # ファイルを探す
find ディレクトリ -type d  # ディレクトリを探す
```

## 拡張子を指定して検索したい

```shell
find ディレクトリ -name "*.html"  # HTMLファイルを探す
find ディレクトリ -name "*.zip"   # ZIPファイルを探す
```
