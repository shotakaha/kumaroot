# nkf

```bash
brew install nkf
```

ファイルのエンコーディングや改行コードを変換するコマンドです。

最近は使うことが少なくなってきましたが、昔のファイルを開く際に役に立つことがあります。
また、Windowsのメモ帳で作成されたテキストファイルは、
Shift JIS になっていることがあるので、
macOSで読むにはUTF-8への変換が必要です。

## エンコーディングを調べる

```bash
$ nkf -g path/to/file.txt
UTF-8
```

## UTF-8に変換して標準出力する

```bash
$ nkf -w path/to/file.txt
```

変換した結果は標準出力に表示されます。

## UTF-8に変換してファイルに保存する

```bash
$ nkf -w path/to/file.txt > path/to/file_utf8.txt
```

標準出力に表示された結果をリダイレクトしてファイルに保存します。

## UTF-8に変換して上書き保存する

```bash
nkf -w --overwrite path/to/file.txt
```

変換した結果を元のファイルに上書きすることもできます。
