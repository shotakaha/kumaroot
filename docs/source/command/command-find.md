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

## ファイルの種類で探したい（``-type``）

```bash
find ディレクトリ -type f  # ファイルを探す
find ディレクトリ -type d  # ディレクトリを探す
```

## 拡張子で探したい（``-name``）

```bash
find ディレクトリ -name "*.html"    # HTMLファイルを探す
find ディレクトリ ! -name "*.html"  # HTML以外のファイルを探す
find ディレクトリ -name "*.zip"     # ZIPファイルを探す
find ディレクトリ -iname "*.zip"    # case insensitive
```

## 修正した時刻で探したい（``-mtime``）

```bash
find ディレクトリ -mtime 5
find ディレクトリ -mmin +10 -mmin -60  # 10分以上、60分以内に変更したファイル
```

## サイズで探したい（``-size``）

```bash
find ディレクトリ -size +100k  # 100kB以上のファイル
find ディレクトリ -size +10M   # 10MB以上のファイル
find ディレクトリ -size +10M -size -50M  # 10MB - 50MBのファイル
```

## 深さを指定したい（``-depth``）

```bash
find ディレクトリ -depth 2 -name "*.html"  # 2階層目まで探す
find ディレクトリ -d 4 -name "*.html"      # 4階層目まで探す
```

## 所有者不明のファイルを探したい（``-nouser``）

```bash
find ディレクトリ -type f -nouser -name "*.html"   # 所有者不明
find ディレクトリ -type f -nogroup -name "*.html"  # グループ不明
```
