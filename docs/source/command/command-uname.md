# uname

現在のマシンとその上で動作していいるOSに関する詳細を表示するコマンドです

```bash
uname [-amnprsv]
```

## すべての情報を確認したい

```bash
uname -a
Darwin NODE 21.6.0 Darwin Kernel Version 21.6.0: Sat Jun 18 17:05:47 PDT 2022; root:xnu-8020.140.41~1/RELEASE_ARM64_T8101 arm64
```

## カーネルの情報を確認したい

```bash
uname -srv
```

## ホスト名を確認したい

```bash
uname -n
```
