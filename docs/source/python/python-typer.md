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

[Typer](https://typer.tiangolo.com/)を使うと、サブコマンド付きのCLIをすぐに作ることができました。

CLIを作るときは、引数／オプション解析が必要です。
定番はPython標準の``argparse``パッケージがありますが、サブコマンドを作るのはちょっと大変な印象です。
（やってみようと思って調べたことはありますが実際に作ったことはない・・・）

それに比べて、``Typer``は公式ドキュメントにある[An example with two subcommands](https://typer.tiangolo.com/#an-example-with-two-subcommands)のサンプルコードをコピペするだけで動作できました。
また、引数とオプション、コマンドの説明も、いつもの関数を作る作業の延長ででき、非常に簡単でした。

## PoetryでCLIしたい

```toml
# pyproject.toml

[tool.poetry.scripts]
CLI名 = "パッケージ.cli:app"
```

``Poetry``を使ってCLIを作成する場合、上記のように{file}``pyproject.toml``に追記します。
