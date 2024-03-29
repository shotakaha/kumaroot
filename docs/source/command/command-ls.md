```{eval-rst}
.. index::
    single: CLI; ls
    single: List directory contents; ls
```

# ファイル一覧したい（``ls``）

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

## ファイルを1行ごとに表示したい

```bash
$ ls -1
```

``xargs``にファイル名を渡したい場合など、``ls -l``で表示される詳細情報が必要ない場合に使います。

:::{note}

最近はRust製の代替コマンドが流行りの兆しがあります。
[lsd](./command-lsd.md)や[exa](./command-exa.md)というコマンドがあります。

:::

:::{seealso}

- [](./command-exa.md)
- [](./command-lsd.md)

:::
