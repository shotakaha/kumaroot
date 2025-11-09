# 実行したい（`RUN`）

```dockerfile
RUN コマンド
```

`RUN`でコマンドを実行し、コンテナイメージをカスタマイズできます。
`RUN`コマンドごとに新しいレイヤーが作成されます。

複数のコマンドは`&&`で連結して1つの`RUN`にまとめることで、
イメージサイズを削減し、ビルド効率を向上させます。

複数のコマンドをまとめる場合は、`\`で改行して読みやすく記述できます。

## コマンドを連結したい

```dockerfile
RUN apt-get update \
    && apt-get install -y curl git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

複数のコマンドを`&&`で連結することで、1つのレイヤーにまとめられます。
各コマンドは`\`で改行して、読みやすくできます。

## パッケージを追加したい（Debian/Ubuntu）

```dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

Debian/Ubuntuベースのイメージを使っている場合に、パッケージを追加するコマンドです。

**各オプションの説明：**

- `apt-get update`: パッケージリストを更新
- `-y`: すべてのプロンプトに自動で「yes」と答える
- `--no-install-recommends`: 推奨パッケージを除外し、最小限のみインストール
- `apt-get clean`: キャッシュをクリア
- `rm -rf /var/lib/apt/lists/*`: パッケージリストを削除（イメージサイズ削減）

複数のコマンドを1つの`RUN`でまとめることで、イメージサイズを削減できます。

## Python環境を構築したい（python + uv）

```dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY pyproject.toml uv.lock ./

# 依存関係をインストール
RUN pip install --no-cache-dir uv \
    && uv sync --frozen

# 環境変数を設定
ENV PATH="/app/.venv/bin:$PATH"
```

[uv](../python/python-uv.md) を使うことで、高速で信頼性の高いPython環境構築ができます。

**ポイント：**

- `--no-cache-dir`: pipのキャッシュを無効化してイメージサイズを削減
- `uv sync --frozen`: lockファイルから正確に依存関係をインストール
- `.venv`は`uv`が自動的に作成します

## Python環境を構築したい（python + poetry）

```dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY pyproject.toml poetry.lock ./

# poetryをインストール
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi

# 環境変数を設定
ENV PATH="/app/.venv/bin:$PATH"
```

[Poetry](../python/python-poetry.md) を使うことで、依存関係を厳密に管理できます。

**ポイント：**

- `--no-cache-dir`: pipのキャッシュを無効化してイメージサイズを削減
- `virtualenvs.in-project true`: 仮想環境をプロジェクト内に作成（`.venv`）
- `--no-interaction --no-ansi`: 対話的な入力を無効化し、ANSIカラーを無効化
- `poetry.lock`: Poetryのlockファイルから正確に依存関係をインストール

## Python環境を構築したい（python + venv）

```dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt ./

# 仮想環境を作成してパッケージをインストール
RUN python -m venv /app/.venv \
    && /app/.venv/bin/pip install --no-cache-dir --upgrade pip \
    && /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

# 環境変数を設定
ENV PATH="/app/.venv/bin:$PATH"
```

標準的な`venv`と`requirements.txt`を使うシンプルなPython環境構築です。

**ポイント：**

- `python -m venv /app/.venv`: 仮想環境を作成
- `/app/.venv/bin/pip install`: 仮想環境内のpipを使用してインストール
- `--no-cache-dir`: pipのキャッシュを無効化してイメージサイズを削減
- `--upgrade pip`: pipをアップグレードして最新版を使用

## シェル形式とexec形式の違い

```dockerfile
# シェル形式（シェルを経由して実行）
RUN apt-get update && apt-get install -y curl

# exec形式（シェルを経由さない）
RUN ["/bin/bash", "-c", "apt-get update && apt-get install -y curl"]
```

**シェル形式：**

- コマンドを文字列として記述
- パイプ（`|`）やリダイレクト（`>`）が使える
- シェル変数展開が可能

**exec形式：**

- コマンドを配列として記述
- シェルを経由しないため高速
- シェル変数が展開されない

通常はシェル形式を使い、パイプやリダイレクトが不要な場合のみexec形式を検討します。

## キャッシュをクリアしたい

```dockerfile
RUN pip install --no-cache-dir package-name
RUN npm install --no-save && npm cache clean --force
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
```

各パッケージマネージャーのキャッシュをクリアすることで、イメージサイズを削減できます。

- **pip**: `--no-cache-dir`オプション
- **npm**: `npm cache clean --force`
- **apt**: `apt-get clean`と `rm -rf /var/lib/apt/lists/*`

## 注意事項

:::{note}

`RUN . venv/bin/activate`のような仮想環境の「活性化」は、
別の`RUN`コマンドでは無効になります。
代わりに、PATHを`ENV`で設定するか、フルパスでコマンドを実行してください。

:::

:::{warning}

複数の`RUN`コマンドに分割するとレイヤー数が増加し、
イメージサイズが大きくなります。
できるだけ`&&`で連結して1つの`RUN`にまとめてください。

:::

## リファレンス

- [RUN - Docker docs](https://docs.docker.com/reference/dockerfile/#run)
- [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Layer caching](https://docs.docker.com/build/building/cache/)
