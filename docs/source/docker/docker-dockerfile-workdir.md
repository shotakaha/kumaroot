# 作業ディレクトリしたい（`WORKDIR`）

```dockerfile
WORKDIR /app
```

`WORKDIR`で作業ディレクトリを変更できます。
Dockerfile内で実行されるコマンドの起点になります。
指定したディレクトリは自動で作成されます。

## 絶対パスで指定する

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

`/app`や`/work`、`/workspace`などが一般的に使われます。

作業ディレクトリは基本的に絶対パスで指定します。
複数の`WORKDIR`指定があっても各ステージで独立した
作業ディレクトリが設定されます。

マウントポイント（`VOLUME`）とは別のディレクトリを使うことをオススメします。

## 相対パスで指定する

```dockerfile
WORKDIR /app
WORKDIR subdir
# 作業ディレクトリは /app/subdir になる
```

相対パスは親ディレクトリに依存します。
複数の`WORKDIR`を指定するとパスが連結されます。
コンテナ構築の過程で作業ディレクトリが意図せず変わる可能性があるので、
明確性を保つため、**絶対パスの使用を推奨します**。

## 避けるべきディレクトリ名

以下のディレクトリを `WORKDIR` として使用することは避けてください。

- **システムディレクトリ**: `/`（ルート）、`/bin`、`/dev`、`/run`、`/sys` など
  - 理由：Linuxシステムの正常動作に必要なディレクトリを汚染する恐れ

- **ユーザーホームディレクトリ**: `/root`、`/home` など
  - 理由：権限やセキュリティの問題が生じる可能性がある

- **一時ディレクトリ**: `/tmp`、`/var/tmp` など
  - 理由：コンテナ再起動時にファイルが削除される可能性がある

## WORKDIRの影響範囲

`WORKDIR` を設定すると、その後の `COPY`、`RUN`、`CMD`、`ENTRYPOINT`、`ADD` など全てのコマンドがそのディレクトリで実行されます。
マルチステージビルドでも、各ステージで独立して `WORKDIR` を設定できます。

## リファレンス

- [WORKDIR - Docker docs](https://docs.docker.com/reference/dockerfile/#workdir)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
