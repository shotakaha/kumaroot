# 作業ディレクトリしたい（`WORKDIR`）

```docker
WORKDIR ディレクトリ名

# /app 以下を作業ディレクトリにしたい
WORKDIR /app

# /work 以下を作業ディレクトリにしたい
WORKDIR /work

# /workspace 以下を作業ディレクトリにしたい
WORKDIR /workspace
```

`WORKDIR`で作業ディレクトリを変更できます。
Dockerfile内で実行されるコマンドの起点になります。
指定したディレクトリは自動で作成されます。

絶対パスで指定するのが一般的で、
`/app`や`/work`、`/workspace`などとする場合が多いようです。
