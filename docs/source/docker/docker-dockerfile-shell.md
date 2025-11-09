# シェルを変更したい（`SHELL`）

```dockerfile
SHELL ["/bin/bash", "-c"]
```

`SHELL`コマンドで、Dockerfile内の`RUN`、`CMD`、`ENTRYPOINT`コマンドを実行するシェルを変更できます。

デフォルトは、Linuxイメージだと`["/bin/sh", "-c"]`、Windowsイメージだと`["cmd", "/S", "/C"]`です。

通常はデフォルトで問題ありませんが、Bashの高度な機能（配列、条件分岐など）が必要な場合や、Windowsコンテナでcmd.exeではなくPowerShellを使いたい場合に`SHELL`を指定します。

## Bashしたい

```dockerfile
FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y curl git
```

デフォルトの`sh`ではBashの高度な機能（配列、関数など）が使えません。
Bashが必要な場合は`SHELL`で明示的に指定します。

## PowerShellしたい

```dockerfile
FROM mcr.microsoft.com/windows/servercore:ltsc2022
SHELL ["powershell", "-Command"]

RUN Write-Host "Using PowerShell"
```

Windowsコンテナでcmd.exeではなくPowerShellを使いたい場合に指定します。

## シェル形式とexec形式

`SHELL`コマンドが影響するのは、**シェル形式**で書かれたコマンドのみです。

```dockerfile
# シェル形式（SHELLの影響を受ける）
RUN echo "test"
CMD echo "test"

# exec形式（SHELLの影響を受けない）
RUN ["/bin/echo", "test"]
CMD ["/bin/echo", "test"]
```

exec形式を使う場合、`SHELL`の設定に関わらず直接コマンドを実行します。

## リファレンス

- [SHELL - Docker docs](https://docs.docker.com/reference/dockerfile/#shell)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
