# シェルを変更したい（`SHELL`）

```dockerfile
# sh -> bash
SHELL ["/bin/bash", "-c"]

# cmd -> powershell
SHELL ["powershell", "--command"]
```

[SHELL](https://docs.docker.com/reference/dockerfile/#shell)コマンドで、
[RUN](./docker-dockerfile-run.md)コマンドを実行するシェルを変更できます。

デフォルトは、Linuxイメージだと`["/bin/sh", "-c"]`、
Windowsイメージだと``["cmd", "/S", "/C"]``です。

## リファレンス

- [SHELL - docs.docker.com](https://docs.docker.com/reference/dockerfile/#shell)
