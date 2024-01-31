# OS情報をしりたい（``uname``）

```console
$ uname -a
Darwin NODE 21.6.0 Darwin Kernel Version 21.6.0: Sat Jun 18 17:05:47 PDT 2022; root:xnu-8020.140.41~1/RELEASE_ARM64_T8101 arm64
```

現在のマシンとその上で動作していいるOSに関する詳細を表示するコマンドです。

## カーネルの情報を確認したい

```console
$ uname -srv
Darwin 23.2.0 Darwin Kernel Version 23.2.0: Wed Nov 15 21:54:10 PST 2023; root:xnu-10002.61.3~2/RELEASE_X86_64

$ uname -v
Darwin Kernel Version 23.2.0: Wed Nov 15 21:54:10 PST 2023; root:xnu-10002.61.3~2/RELEASE_X86_64

$ uname -sr
Darwin 23.2.0
```

``-v``、``-s``、``-r``オプションを使ってカーネル情報を確認できます。
オプションは単独でも、組み合わせても使えます。

## ホスト名を確認したい

```console
$ uname -n
ホスト名.local
```

:::{seealso}

- neofetch

:::

## アーキテクチャを確認したい

```console
$ uname -m
x86_64

$ uname -p
i386
```

``-m``オプションや``-p``オプションで、ハードウェア情報を確認できます。
