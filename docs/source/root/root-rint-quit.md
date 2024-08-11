# 終了したい（``.q``）

```console
$ root
// RINTが起動

root [0] .q
root [0] .qqq      # ROOTを終了
root [0] .qqqqq    # プロセスをすぐに終了
root [0] .qqqqqqq  # プロセスをアボート
```

``.q``でRINTを終了します。
プロセスがハングしてしまったような場合は、
`qq`の数を増やしてみるとよいです。

:::{seealso}

RINTをどうしても終了できない場合は、
ターミナルのタブを強制的に閉じるか、
システムから`kill`します。

- [](../command/command-ps.md)

:::
