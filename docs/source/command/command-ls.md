# ls

```bash
$ ls
```

## 最新ファイルを確認したい

```bash
$ ls -ltr
$ ls -ltra
```

最後に更新されたファイルを確認したいときに、手癖となっているコマンドです。
時間（``-t``）の逆順（``-r``）に並べることで、
一番新しいファイルが出力の末尾に表示されるので、
わざわざコマンドを実行した画面までスクロールする必要がなくなります。

``-l``や``-a``は状況によって使い分けます。

## 代替コマンド

最近はRust製の代替コマンドが流行りの兆しがあります。
``lsd``や``exa``というコマンドがあります。

## リファレンス

- [lsd - LSDeluxe](https://github.com/Peltoche/lsd)
- [exa - A modern replacement for ls](https://the.exa.website/)
