# ディスク使用量したい（`df`）

```console
$ df -H
```

`df`でシステム全体のディスク使用量を確認できます。
`-H`オプションで、1000刻みで単位を自動選択し、
人間にわかりやすいサイズ形式で表示できます。

## 単位を揃えたい（`-B` / `--block-size`）

```console
$ df -b # 512-blocks
$ df -k # 1024-blocks
$ df -m # 1M-blocks
$ df -g # 1G-blocks
$ df --block-size=KB
$ df -B100MB
```

`--block-size`オプションで、集計する単位を変更できます。
`-h`による自動調整も便利ですが、ディスク容量をモニターする場合など、
単位が揃っているほうがよい場合もあります。

指定できる単位は、
1024倍刻みの場合、`K`、`M`、`T`、`P`、`E`、`Z`、`Y`
1000倍刻みの場合、`KB`、`MB`、`TB`、`PB`、`EB`、`ZB`、`YB`
です。
大文字でも小文字でも大丈夫です。
