# イメージを指定したい（`FROM`）

```dockerfile
FROM イメージ:タグ
```

`FROM`でベースとして使うイメージ名を指定します。
イメージ名とタグは[Docker Hub](https://hub.docker.com/)などの
コンテナレジストリから探します。

タグに具体的なバージョンを指定することで、コンテナ環境の安定性を確保できます。
指定しない場合は`latest`になります。

:::{note}
`latest`タグは常に最新版を指し、予告なく更新される可能性があります。
そのため予期しない動作変更が発生するリスクがあります。

本番環境では、必ず具体的なバージョンタグ（例：`python:3.12.0`）を指定することをお勧めします。
:::


## Pythonしたい

```docker
FROM python:3.12-slim
```

Docker Hubにある
[Pythonの公式レジストリ](https://hub.docker.com/_/python)
から必要なタグを指定します。

`bookworm`や`bullseye`がついたタグでDebianのバージョンを指定できます。
`slim`がついたタグは、不要なライブラリが省かれた軽量版です。
`alpine`がついたタグはAlpine Linuxベースの超軽量版です。

## BusyBoxしたい

```dockerfile
FROM busybox
```

BusyBoxは、一般的なLinuxコマンドを統合した超軽量イメージです。
イメージサイズが数MBと非常に小さいため、シンプルなコンテナやスクリプト実行に適しています。
フルOSが不要な場合や、イメージサイズを最小化したい場合に活用されます。

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
WORKDIR /build
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

# 実行用ステージ
FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /build/.venv /app/.venv
COPY src/ ./src/
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "src/main.py"]
```

複数の`FROM`を使うことで、ビルドのステップを複数のステージに分割できます。

ビルド用ステージで依存パッケージをインストールしてから、実行用ステージで必要なファイルだけをコピーすることで、最終的なイメージサイズを削減できます。

上記のサンプルでは、
**ビルド用ステージbuilder**（`builder`）で、ビルド環境を準備し、Poetryで依存パッケージをインストールし、
**実行用ステージ**で、`builder`ステージから
`.venv` をコピーして、
必要なファイルだけを含めています。

このようにすることで、最終イメージにはビルドツールが含まれず、サイズも小さく、セキュリティリスクも低くなります。

### `as` キーワード

マルチステージビルドで複数の`FROM`を使う際、`as ステージ名`でステージに名前を付けます。
後の`COPY --from=ステージ名`で、指定したステージのファイルをコピーできます。

## FROM scratch

```dockerfile
FROM scratch
COPY app /app
CMD ["/app"]
```

`FROM scratch`は、最小限のベースイメージから始める指定です。
空のイメージから開始するため、バイナリファイルのみのコンテナを作成でき、最小限のセキュリティ脅威面積を実現できます。
ただし、デバッグやシェルアクセスがないため、単純な実行ファイルのみのコンテナ向けです。

## リファレンス

- [FROM - Docker docs](https://docs.docker.com/reference/dockerfile/#from)
- [Multi-stage builds - Docker docs](https://docs.docker.com/build/building/multi-stage/)
- [Docker Hub](https://hub.docker.com/)
