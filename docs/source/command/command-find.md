# find

ファイルやディレクトリを探すコマンドです。
ファイルの内容は検索できません。


```bash
find ディレクトリ 検索文字列
```

- ディレクトリ名の末尾の``/ (trailing-slash)``はつけなくてOK

## オプション

```bash
find -name パターン   # ファイル名で検索
find -regex 正規表現  # 完全な正規表現を使うことができる
find -print           # 一致した完全パス名を書きだす
find -size 数         # ファイル容量で検索
find -type タイプ     # ファイルの種類で検索
find -cmin 数         # 数分以内に変更されたファイルを検索
find -ctime 数        # 数時間以内に変更されたファイルを検索
find -ls              # 検索結果を ls -l に書きだす
```

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
