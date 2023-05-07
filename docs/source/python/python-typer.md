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
