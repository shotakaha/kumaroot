# TeXLiveしたい（`texlive`）

```{literalinclude} ../../examples/docker/texlive.yaml
---
language: yaml
---
```

## コンテナーを起動したい

```console
$ docker compose up
```

## コンテナーで操作したい

```console
$ docker compose exec tex bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## TeXLiveについて

TeXLiveはLaTeX環境のDockerイメージです。
サービス名を`tex`としており、イメージは最新版を指定しています。
ボリュームでホストディレクトリを`/workdir`にバインドマウントすることで、手元のファイルをコンテナ内で処理できるようにしています。
`docker compose up`すると`command`に設定した内容が実行され、LaTeX文書をPDFに変換できます。
コンテナー内で`latexmk`や`pdflatex`といったコマンドを使って文書を処理できます。
