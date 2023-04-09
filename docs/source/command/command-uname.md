# OS情報をしりたい（``uname``）

```console
$ uname -a
Darwin NODE 21.6.0 Darwin Kernel Version 21.6.0: Sat Jun 18 17:05:47 PDT 2022; root:xnu-8020.140.41~1/RELEASE_ARM64_T8101 arm64
```

現在のマシンとその上で動作していいるOSに関する詳細を表示するコマンドです。

## カーネルの情報を確認したい

```console
$ uname -srv
Darwin 21.6.0 Darwin Kernel Version 21.6.0: Mon Dec 19 20:44:01 PST 2022; root:xnu-8020.240.18~2/RELEASE_X86_64
```

## ホスト名を確認したい

```console
$ uname -n
ホスト名.local
```

:::{seealso}

- neofetch

:::
