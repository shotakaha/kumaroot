# イメージを指定したい（`FROM`）

```docker
FROM イメージ:タグ
```

`FROM`でベースとして使うイメージ名を指定します。
イメージ名とタグは[Docker Hub](https://hub.docker.com/)などの
コンテナレジストリから探します。

タグに具体的なバージョンを指定することで、コンテナ環境の安定性を確保できます。
指定しない場合は`latest`になります。


## Pythonしたい

```docker
FROM python:3.12-slim
```

Docker Hubにある
[Pythonの公式レジストリ](https://hub.docker.com/_/python)
から必要なタグを指定します。

`bookworm`や`bullesye`がついたタグでDebianのバージョンを指定できます。
`slim`がついたタグは、不要なライブラリが省かれた軽量版です。
`alpine`がついたタグはAlpine Linuxベースの超軽量版です。

## BusyBoxしたい

```dockerfile
FROM busybox
```

## プラットフォームしたい（`--platform`）

```dockerfile
# x86 64bit
# よくあるパソコン
FROM --platform=linux/amd64 python:3.12

# arm 64bit
# Appleシリコン、Raspberry PI
FROM --platform=linux/arm64 python:3.12
```

`--platform`オプションで、コンテナが動作するプラットフォームを変更できます。
デフォルトはホストPCと同じプラットフォームです。

## マルチステージしたい

```dockerfile
# ビルド用ステージ
FROM python:3.12-alpine as builder
WORKDIR /app
COPY . .
RUN poetry build

# 実行用ステージ
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/パッケージ名
CMD ["./パッケージ名"]
```

複数の`FROM`を使うことで、ビルドのステップを複数のステージに分割できます。
マルチステージをうまく使うと、最終的なイメージに不要なファイルやツールを含めずに済みます。

上記のサンプルは、
`python:3.12-alpine`を使ってビルドしていますが、
最終的には`alpine:latest`でイメージを作成しています。
