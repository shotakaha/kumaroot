# CLIしたい（``typer``）

```console
$ pip3 install typer[all]
```

```python
# パッケージ/cli.py
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

if __name__ == "__main__":
    app()
```

[Typer](https://typer.tiangolo.com/)を使うと、サブコマンド付きのCLIをすぐに作ることができます。
上記のサンプルは、公式ドキュメントの[An example with two subcommands - Typer](https://typer.tiangolo.com/#an-example-with-two-subcommands)にあるコードです。
とりあえずこのサンプルコードを{file}`cli.py`のようなファイルにコピペして動かしてみるだけで、使い方がわかると思います。

これまで、CLIを作るときの引数／オプション解析は、定番のPython標準``argparse``パッケージを使っていましたが、サブコマンドを作るのはちょっと大変な印象でした。
（やってみようと思って調べたことはありますが実際に作ったことはない・・・）
``Typer``は、引数とオプション、コマンドの説明も、いつもの関数を作る作業の延長ででき、非常に簡単だと感じました。

## 位置引数したい（``typer.Argument``）

```python
# 簡単設定
ch: int  # 位置引数（required）

# 詳細設定
ch: Annotated[int, typer.Argument(help="チャンネル番号を指定")]     # 位置引数（required）
ch: Annotated[int, typer.Argument(help="チャンネル番号を指定")] = 0 # 位置引数（optional）
```

コマンドの引数に型ヒントを指定します。
引数のヘルプなど詳細設定したい場合は``typing_extensions.Annotated``を利用します。

簡単設定では required な位置引数のみ設定できます。
詳細設定では optional な位置引数も設定できます。

```python
import typer
from typing_extensions import Annotated

def command(
    ch: int,
    ):
    pass

def vth(
    ch: Annotated[int, typer.Argument(help="チャンネル番号を指定")]
    ):
    pass
```

## オプション引数したい（``typer.Option``）

```python
# 簡単設定
ch: int = 0  # オプション引数（optional）

# 詳細設定
ch: Annotated[int, typer.Option(help="チャンネル番号を指定")] = 0 # オプション引数（optional）
ch: Annotated[int, typer.Option(help="チャンネル番号を指定")] = 0 # オプション引数（required）
```

デフォルト値を与えると、オプション引数になります。
引数のヘルプなど詳細設定したい場合は``typing_extensions.Annotated``を利用します。

簡単設定では optional なオプション引数のみ設定できます。
詳細設定では required なオプション引数も設定できます。


```python
def vth(
    ch: int
    ):
    pass

def vth(
    ch: Annotated[int, typer.Argument(help="チャンネル番号を指定")]
    ):
    pass
```

## コマンドしたい（``typer.Argument`` / ``typer.Option``）

```python
import typer
from typing_extensions import Annotated

def vth(
    """
    コマンドの説明
    """
    ch Annotated[int, typer.Argument(help="チャンネル番号")],
    vth: Annotated[int, typer.Argument(help="スレッショルド値")],
    max_retry: Annotated[int, typer.Option(help="リトライ数")] = 3,
    load_from: Annotated[str, typer.Option(help="設定ファイル名")] = "daq.toml"
    ):
    pass

if __name__ == "__main__":
    typer.run(vth)
```

コマンドとして実行したい関数名を``typer.run``に渡します。
関数の``docstring``がコマンドの説明になります。

``typer.Argument``で引数を設定できます。
``typer.Option``でオプション引数を設定できます。

``typing_extensions.Annotated``で引数の説明を追加できます。
追加方法などは、ドキュメントを参照してください。

:::{hint}

``typer.Argument`` / ``typer.Option``と
デフォルト値のあり / なしを考えると
以下の表のような引数名のパターンが考えられます。

| | デフォルト値なし | デフォルト値あり |
|---|---|---
| ``typer.Argument`` | **CLI arguments** | optional CLI arguments |
| ``typer.Option`` | required CLI options | **CLI options** |

通常は、
CLI arguments（必須の位置引数）、
CLI options（オプション引数）
のみのコマンドを設計するとよいと思います。

ただし、
optional CLI arguments（位置引数なのにオプション）、
required CLI options（オプション引数なのに必須）
も、名前がちょっとおかしい気がしますが、定義できるようになっています。

:::


## サブコマンドしたい（``@app.command``）

```python
import typer

app = typer.Typer()

@app.command()
def vth(
    """
    コマンドの説明
    """
    ch Annotated[int, typer.Argument(help="チャンネル番号")],
    vth: Annotated[int, typer.argument(help="スレッショルド値")],
    max_retry: Annotated[int, typer.argument(help="リトライ数")] = 3,
    load_from: Annotated[str, typer.argument(help="設定ファイル名")] = "daq.toml"
    ):
    pass

if __name__ == "__main__":
    app()
```

``@app.command``デコレーターでサブコマンドを定義できます。

:::{note}

``app``の部分は任意のオブジェクト名を使用できます。
上記のサンプルでは``app = typer.Typer()``を作成しているため、デコレーターは``@app.command``になります。

:::


## 出力に色をつけたい（``from rich import print``）

```python
import typer
from rich import print

...（省略）...
```

``rich``パッケージの``print``を使うと、出力を色付けできます。
色付けの詳細や、その他の表示形式はドキュメントを参照してください。

## 中断／終了したい（``typer.Exit``）

```python
@app.command()
def コマンド名(引数):
    if 引数がおかしい条件:
        logger.error(f"値が正しくないです : {引数}")
        typer.Exit()
```

``Typer``を使うと、引数のバリデーションを柔軟に書くことができます。
引数の値が正しくない場合に終了する場合、``typer.Exit``が使えます。
わざわざ``import sys``して``sys.exit``する必要がないので便利です。

## PoetryでCLIしたい

```toml
# pyproject.toml

[tool.poetry.scripts]
CLI名 = "パッケージ.cli:app"
```

``Poetry``を使って自作CLIを作成する場合は、{file}``pyproject.toml``の`[tool.poetry.scripts]`セクションに記述します。
詳しくは公式ドキュメントの[Building a package - Typer](https://typer.tiangolo.com/tutorial/package/)を参照してください。
