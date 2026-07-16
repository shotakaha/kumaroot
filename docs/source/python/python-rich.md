# 標準出力したい（`rich`）

```python
from rich import print
print("Hello, [bold magenta]Rich[/bold magenta]!")
```

`rich`は、Pythonの標準出力を装飾するためのライブラリです。

`rich.print`関数に置き換えるだけで、テキストの色やスタイルを指定して、見やすく、わかりやすい出力を実現できます。

:::{note}

``from rich import print``は、Pythonの組み込み関数``print``を
``rich.print``で上書き（シャドーイング）しています。
そのファイル内では以降``print(...)``と書くだけで、装飾された出力が使えるようになります。

:::

`[スタイル名]テキスト[/スタイル名]`のようなタグで、テキストにスタイルを指定できます。
`bold`（太字）、`red`・`green`・`magenta`などの色名、
`italic`（斜体）、`underline`（下線）などを組み合わせて使えます
（例：``[bold red]エラー[/bold red]``）。

## コンソール出力したい（`rich.console.Console`）

```python
import sys
from rich.console import Console
stdout = Console(file=sys.stdout)
stderr = Console(file=sys.stderr)

stdout.print("This is a message to standard output.", style="green")
stderr.print("This is a message to standard error.", style="red")
```

`rich.console.Console`を使って、標準出力や標準エラーに装飾されたテキストを出力できます。

`Console`オブジェクトを作成するときに、`file`引数で出力先を変更できます。
システムの標準出力（`sys.stdout`）や標準エラー出力（`sys.stderr`）を指定するのが最近の個人的なお気に入りです。

:::{note}

`rich`には、このほかにもテーブル（``rich.table.Table``）、
進捗バー（``rich.progress``）、
トレースバックの装飾（``rich.traceback``）、
標準の``logging``モジュールと連携する``RichHandler``（``rich.logging``）など、
数多くの機能があります。
くわしくは[公式ドキュメント](https://rich.readthedocs.io/en/stable/introduction.html)を参照してください。

:::

## テーブル表示したい（`rich.table.Table`）

```python
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="ユーザー一覧")

table.add_column("名前", style="cyan")
table.add_column("年齢", justify="right", style="magenta")
table.add_column("役職", style="green")

table.add_row("Alice", "30", "Engineer")
table.add_row("Bob", "25", "Designer")

console.print(table)
```

`rich.table.Table`で、装飾されたテーブルをコンソールに表示できます。
`add_column`で列を定義し、`add_row`で行を追加します。
`style`引数で列ごとに色を指定でき、`justify`で文字寄せ（`left`・`center`・`right`）を指定できます。

## 進捗バーしたい（`rich.progress`）

```python
import time
from rich.progress import track

for i in track(range(20), description="処理中..."):
    time.sleep(0.1)  # なんらかの処理
```

`rich.progress.track`で、`for`文をそのまま進捗バー付きのループに変換できます。
`range`や`list`などのイテラブルをラップするだけで使えます。

より細かく制御したい場合は`rich.progress.Progress`を使います。

```python
import time
from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("[cyan]ダウンロード中...", total=100)
    task2 = progress.add_task("[green]処理中...", total=50)

    while not progress.finished:
        progress.update(task1, advance=1)
        progress.update(task2, advance=0.5)
        time.sleep(0.05)
```

`Progress`オブジェクトで複数の進捗バーを同時に表示できます。
`add_task`で進捗バーを追加し、`update`で進捗を更新します。
