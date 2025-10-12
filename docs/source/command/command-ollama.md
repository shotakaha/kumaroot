# Ollamaしたい（`ollama`）

```console
$ ollama run <モデル名>
```

`ollama`はローカルで大規模言語モデル（LLM）実行できるツールです。
Mistral、
LlaMA、
CodeLlama、
Gemma
などのモデルが簡単に使えるように設計されています。

## インストールしたい

```console
$ brew install --cask ollama-app
$ ollama --version
ollama version is 0.12.5
```

Homebrewで`ollama`をインストールできます。
アプリも使いたい場合は`ollama-app`をインストールします。

## モデルを取得したい（`ollama pull`）

```console
$ ollama pull <モデル名>
$ ollama pull gpt-oss:20b
```

`ollama pull`で利用したいモデルを取得します。

:::{note}

`gpt-oss:20b`は13GBありました。

:::

## モデルを一覧したい（`ollama list`）

```console
$ ollama list
$ ollama ls
```

`ollama list`（もしくは `ollama ls`）で取得済みのモデル一覧を表示できます。

## モデルを削除したい（`ollama rm`）

```console
$ ollama rm <モデル名>
```

`ollama rm`でモデルを削除できます。

## モデルと対話したい（`ollama run`）

```console
$ ollama run <モデル名>
```

`ollama run`でモデルと対話できます。

## APIサーバーしたい（`ollama serve`）

```console
$ ollama serve <モデル名>
```

`ollama serve`（もしくは `ollama start`）でモデルのAPIサーバーを起動できます。
