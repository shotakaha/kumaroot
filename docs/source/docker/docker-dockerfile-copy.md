# ファイルをコピーしたい（`COPY`）

```dockerfile
COPY . .
```

`COPY`でホストPCのファイルやディレクトリを、Dockerイメージ内にコピーできます。
ビルドコンテキスト内のファイルのみがコピー対象です。

## 単一ファイルをコピーしたい

```dockerfile
COPY requirements.txt /app/requirements.txt
COPY package.json .
```

`COPY <src> <dest>`の形式で、ホスト上のファイルをイメージ内にコピーします。
`<dest>`が相対パスの場合は`WORKDIR`からの相対位置になります。

## 複数ファイルをコピーしたい

```dockerfile
COPY package.json package-lock.json ./
COPY *.py /app/scripts/
```

ワイルドカード（`*`）を使って複数ファイルを一度にコピーできます。

## ディレクトリをコピーしたい

```dockerfile
# srcディレクトリの内容をappにコピー
COPY src/ /app/

# srcディレクトリ自体をappにコピー
COPY src /app/
```

末尾のスラッシュ（`/`）でコピー動作が変わります。

- `src/` - ディレクトリの内容をコピー
- `src` - ディレクトリ自体をコピー

## 所有者を変更したい（`--chown`）

```dockerfile
# ユーザー名とグループ名で指定
COPY --chown=node:node package.json .

# UID/GIDで指定
COPY --chown=1000:1000 . /app/
```

`--chown`オプションで、コピーしたファイルの所有者を指定できます。
マルチステージビルドで別のユーザーが作成したファイルを使用する場合に有効です。

## 別のステージからコピーしたい（`--from`）

```dockerfile
# ビルドステージ
FROM python:3.12 as builder
WORKDIR /build
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

# 実行ステージ
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /build/.venv /app/.venv
COPY src/ ./src/
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "-m", "src.main"]
```

`--from=<ステージ名>`で、マルチステージビルド内の別のステージからファイルをコピーできます。
ビルド成果物のみを最終イメージに含める際に活用されます。

## レイヤーキャッシュを活用したい

```dockerfile
FROM python:3.12-slim
WORKDIR /app

# 良い例：依存関係ファイルを先にコピー
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 悪い例：すべてを一度にコピー
# COPY . .
# RUN pip install -r requirements.txt
```

依存関係ファイルを先にコピーすることで、
ソースコード変更時にレイヤーキャッシュが活用され、ビルドが高速になります。

## 不要なファイルを除外したい（`.dockerignore`）

```text
# .dockerignore
node_modules/
.git/
.gitignore
*.log
.env
.DS_Store
__pycache__/
*.pyc
```

`.dockerignore`ファイルで、コピー対象から除外するファイルを指定できます。
`.dockerignore`はビルドコンテキストのルートに配置します。

`COPY . .`を使用する場合、`.dockerignore`に指定したファイルはコピー対象から除外されます。
これにより、イメージサイズを削減し、ビルド時間を短縮できます。

## ADDとの違い

```dockerfile
# COPY: 単純なファイルコピーのみ
COPY requirements.txt .

# ADD: 圧縮ファイルの自動展開、URLからのダウンロードが可能
ADD archive.tar.gz .
ADD https://example.com/file.tar.gz .
```

単純なファイルのコピーには`COPY`が推奨されています。
圧縮ファイル展開、URLダウンロードなど`ADD`の特殊機能が必要な場合のみ`ADD`を使用することがベストプラクティスです。

## 注意事項

:::{note}

`COPY`でコピーできるのは、ビルドコンテキスト内のファイルのみです。
親ディレクトリ（`../`）などのコンテキスト外のファイルはコピーできません。

:::

:::{warning}

`COPY . .`は便利ですが、`.dockerignore`を適切に設定しないと、
不要なファイル（`.git`、ログファイル、キャッシュなど）もコピーされてしまいます。
必ず`.dockerignore`を確認してください。

:::

## リファレンス

- [COPY - Docker docs](https://docs.docker.com/reference/dockerfile/#copy)
- [.dockerignore file - Docker docs](https://docs.docker.com/build/building/context/#dockerignore-files)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
