# echo

```bash
$ echo hello world
hello world
```

引数を表示する関数です。
シェルで設定されている変数を確認したり、スクリプトのデバッグに使ったりします。
リダイレクトと組み合わせて、ファイルにテキストを書き込むこともできます。

``fish``と``bash/zsh``の``echo``コマンドはちょっと異なるかもしれない。

## 改行しない

```bash
$ echo -n hello world
hello world⏎
```

## 空白で分割しない

```bash
$ echo -s hello world
helloworld
```
