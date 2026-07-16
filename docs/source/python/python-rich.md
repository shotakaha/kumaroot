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
