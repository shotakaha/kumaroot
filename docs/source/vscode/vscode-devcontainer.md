# 開発コンテナしたい（`devcontainer`）

`devcontainer`（Dev Container）はVS Codeからコンテナ環境に接続し、
ローカル環境と同じように開発できる機能です。
バックエンドに[Docker](./../docker/docker-usage.md)を利用します。

プロジェクトごとの設定は
`.devcontainer/devcontainer.json`に記述し、
開発メンバーで共有できます。

## コンテナレジストリ

| レジストリ名 | 提供元 | ホスト名 |
|---|---|---|
| Docker Hub | Docker | `docker.io` |
| GitHub Container Registry | GitHub | `ghcr.io` |
| Microsoft Container Registry | Microsoft | `mcr.microsoft.com` |

コンテナレジストリの一覧を作ってみました。
この他にもAWSやGoogle Cloudがホストしているレジストリもあります。

## Python環境したい

```text
test-devcontainer-python
|-- .devcontainer/devcontainer.json
|-- requirements.txt
```

Python環境を構築するときのディレクトリ構造の例です。
プロジェクトのルートにパッケージの依存関係を記述した`requirements.txt`を作成します。

```json
{
    "name": "Python Dev Container",
    "image": "mcr.microsoft.com/devcontainers/python:3.11",
    "features": {
        "ghcr.io/devcontainers/features/python:1": {}
    },
    "postCreateCommand": "pip install -r requirements.txt",
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance"
            ]
        }
    }
}
```

Python3.11環境を構築するための`.devcontainer/devcontainer.json`の設定例です。
それぞれの設定キーは以下の通りです。

`name`
: 開発コンテナの名前です。VS CodeのUIで表示されます（Dockerのコンテナ名ではありません）。

`image`
: 使用するコンテナイメージです。
ここでは[Microsoftのコンテナレジストリ](https://mcr.microsoft.com/en-us/artifact/mar/devcontainers/python/tags)を指定していますが、
Docker Hubなど他のコンテナレジストリにあるイメージも指定できます。

`features`
: プロジェクトに追加したい機能を指定します。

`postCreateCommand`
: 開発コンテナを作成したあとに実行するコマンドを設定します。
ここでは`pip install -r requirements.txt`しています。

`customizations`
: VS Codeの拡張機能を指定しています。
ここではPython拡張とPylance拡張を追加しています。
