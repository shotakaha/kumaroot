# find

```bash
find ディレクトリ 検索文字列
```

- ディレクトリ名の末尾の``/ (trailing-slash)``はつけなくてOK

## ファイルの種類を指定したい（``-type``）

```bash
find ディレクトリ -type f  # ファイルを探す
find ディレクトリ -type d  # ディレクトリを探す
```

## 拡張子を指定したい（``-name``）

```bash
find ディレクトリ -name "*.html"  # HTMLファイルを探す
find ディレクトリ -name "*.zip"   # ZIPファイルを探す
```

## 深さを指定したい（``-depth``）

```bash
find ディレクトリ -depth 2 -name "*.html"  # 2階層目まで探す
find ディレクトリ -d 4 -name "*.html"      # 4階層目まで探す
```

## 所有者不明のファイルを探したい（``-nouser``）

```bash
find ディレクトリ -type f -nouser -name "*.html"
```
