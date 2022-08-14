# Pythonの使い方

[Homebrew](https://brew.sh)を使って``Python``をインストールします。
そして、プロジェクトごとの環境構築には[poetry](https://python-poetry.org/)を使います。


## Pythonのインストール

```bash
$ brew install python3
```

## Poetryのインストール

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

- RTD設定に必要な``requirements.txt``を作成する


```bash
$ poetry export -f requirements.txt --output requirements.txt
```

## 便利なパッケージ


```{toctree}
python-pathlib
python-altair
python-loguru
python-pandas
python-plotly
python-poetry
```
