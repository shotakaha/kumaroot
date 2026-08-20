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

## ディレクトリ構造

```text
project/
├── compose.yaml
├── main.tex
├── chapters/
│   ├── chapter1.tex
│   └── chapter2.tex
└── figures/
    └── image.png
```

`compose.yaml`と同じディレクトリが作業ディレクトリ（`/workdir`）としてマウントされます。
`main.tex`や関連ファイルはすべて
`compose.yaml`と同じ階層に配置してください。

```latex
% main.tex
\input{chapters/chapter1}
\input{chapters/chapter2}
\includegraphics{figures/image}
```

`\input{}`や`\include{}`で読み込むファイル、画像、`.bib`ファイルなどはサブディレクトリに整理しても構いません。

`compose.yaml`より外側（親ディレクトリなど）に置いたファイルはマウントできないため、コンテナ内からは参照できません。

## TeXLiveについて

TeXLiveはLaTeX環境のDockerイメージです。
サービス名を`tex`としており、イメージは最新版を指定しています。
ボリュームでホストディレクトリを`/workdir`にバインドマウントすることで、手元のファイルをコンテナ内で処理できるようにしています。
`docker compose up`すると`command`に設定した内容が実行され、LaTeX文書をPDFに変換できます。
コンテナー内で`latexmk`や`pdflatex`といったコマンドを使って文書を処理できます。
