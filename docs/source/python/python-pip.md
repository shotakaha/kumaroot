# パッケージ管理したい（``pip``）

```console
$ pip3 install パッケージ名
$ pip3 install -U パッケージ名
$ pip3 uninstall パッケージ名
```

`pip`（`pip3`）はPython標準のパッケージ管理ツールです。

:::{note}
`pip`と`pip3`は同じコマンドです。
Python2系から3系の移行期には、`pip`（＝2系）と`pip3`（＝3系）で使い分けられるようになっていました。
いまは3系がメインなので`pip` = `pip3`となっていますが、僕は習慣で`pip3`を使っています。
:::

:::{hint}

`pip`は、複数のパッケージ間の依存関係の管理があまり得意ではありません。
そのため、システム全体ではなく、プロジェクトごとの仮想環境にインストールするのが最近の定番です。

簡単に仮想環境で管理できるパッケージ管理ツールも多数あります。
[uv](./python-uv.md)、
[poetry](./python-poetry.md)、
[pipx](./python-pipx.md)
などを使ってみるのがよいと思います。

:::

## パッケージを更新したい（`--upgrade`）

```console
$ pip3 install -U パッケージ名
```

`-U / --upgrade`オプションでパッケージを更新できます。
初回インストール時にこのオプションをつけても問題ありません。

## パッケージを一括で更新したい

```console
$ pip3 list --outdated | awk 'NR>2{print $1}' | xargs pip3 install -U pip
```

`pip3`には、新しいバージョンがリリースされたパッケージを一括で更新するコマンドがありません。
そのため[awkコマンド](../command/command-awk.md)と[xargsコマンド](../command/command-xargs.md)と組み合わせてパイプ処理します。

1. `pip3 list --outdated`で更新が必要なパッケージをリストします
2. その出力結果に対して`awk`を使ってパッケージ名（＝2行目以降の1列目）を抽出します
3. その出力結果を`xargs`に渡して`pip3 install -U 更新が必要なパッケージ名たち`を実行します

## パッケージを一括で追加したい（`--requirements`）

```console
// 書式: pip3 install -r ファイル名
$ pip3 install -r requirements.txt

$ pip3 freeze > requirements.txt
```

パッケージの一覧は`requirements.txt`で管理するのが一般的です。
`pip3 install -r`オプションでファイルに書かれているパッケージを一括インストールできます。

また、`pip3 freeze`で現在使用しているパッケージを
`requirements.txt`に出力できます。

:::{note}

`requirements.txt`によるパッケージ管理は、長い間利用されてきた方法です。
最近では、2018年に導入されたよりモダンな`pyproject.toml`を使った方法が主流になっています。

:::

## Pythonの実行環境を指定したい

```console
$ python3.10 -m pip install パッケージ名
$ python3.11 -m pip install パッケージ名
$ python3.12 -m pip install パッケージ名
```

`pip3`は基本的にシステムで有効なPython実行環境と連動しています。
`python -m pip`で`pip`をモジュールとして呼ぶことで、
指定したPython環境にインストールできます。

```console
// python3の実行パスを確認
$ which -a python3
/opt/homebrew/bin/python3
/usr/bin/python3

// python3の実体を確認
$ ls -1 /opt/homebrew/bin/python*
/opt/homebrew/bin/python3
/opt/homebrew/bin/python3-config
/opt/homebrew/bin/python3.11
/opt/homebrew/bin/python3.11-config
/opt/homebrew/bin/python3.12
/opt/homebrew/bin/python3.12-config
/opt/homebrew/bin/python3.13
/opt/homebrew/bin/python3.13-config
```

:::{note}

HomebrewでPythonをインストールして更新していると、
気づかないうちに複数のPythonバージョンが溜まっていることがあります。
パッケージがうまくインストールできなかったり、`import`できなかったりする場合は、
自分がどのバージョンを使っているのか、確認するとよいです。

:::

## 仮想環境と組み合わせる

```console
// 仮想環境を作成する
$ python3 -m venv .venv

// 仮想環境を有効にする
$ source .venv/bin/activate

// パッケージを追加する
(.venv) $ pip install -r requirements.txt

// 仮想環境を無効化する
(.venv) $ deactivate
```

[venvパッケージ](./python-venv.md)と組み合わせて、仮想環境の中で使用できます。
仮想環境を有効化すると、`pip`などのコマンドはすべて`.venv`の中に限定されます。
インストールしたパッケージはグローバル（＝システム）に影響しないため、
複数のプロジェクトで異なる依存関係を安全に管理できます。

:::{note}

仮想環境は`.venv`というディレクトリに作成するのが一般的です。
VS Codeでも自動検出してくれます。

:::

## パッケージ管理ツール選択フローチャート

パッケージ管理ツールを選択するときのフローチャートを整理しました。
はじめての場合は、標準パッケージである`venv + pip`からはじめるのが無難です。
パッケージ開発に取り組みむ場合は`uv`を選択するのがオススメです。
CLIツールとしての利用であれば`pipx`が手軽です。

```text
スタート
  │
  ├── CLIツールだけをインストールしてすぐ使いたい？
  │     └─ はい → pipx
  │     └─ いいえ
  │
  ├── プロジェクトごとに環境を分けたい？
  │     └─ はい
  │         ├── 標準機能だけでよい？（シンプルで軽量が希望）
  │         │     └─ はい → venv + pip
  │         │     └─ いいえ
  │         │         ├── 依存の自動管理や公開もしたい？
  │         │         │     └─ はい → uv
  │         │         │     └─ poetry（GUIや柔軟な機能がほしい場合）
  │         │         └─ その他 → pipenv（古いが一体型）
  │         └─（補足：Pythonバージョンも自動で管理したい → uv / pyenv）
  │
  └── とりあえずライブラリを入れて試したい？
        └─ はい → pip
        └─ いいえ → プロジェクトで再利用したい → uv or poetry
```


:::{mermaid}
flowchart TD
    start([スタート])

    q1{CLIツールだけをインストールしてすぐ使いたい？}
    q2{プロジェクトごとに環境を分けたい？}
    q3{標準機能だけでよい？（シンプルで軽量）}
    q4{依存の自動管理や公開もしたい？}

    start --> q1
    q1 -- はい --> pipx[pipx を使う]
    q1 -- いいえ --> q2

    q2 -- いいえ --> pip[pip を使う]
    q2 -- はい --> q3

    q3 -- はい --> venv[venv + pip を使う]
    q3 -- いいえ --> q4

    q4 -- はい --> uv[uv を使う]
    q4 -- いいえ --> poetry[poetry を使う（GUI/柔軟な機能）]
    q4 -- その他 --> pipenv[pipenv（古いが一体型）]

    uv --> note1[Python バージョンも自動で管理したいなら uv または pyenv も検討]
    poetry --> note1
:::
