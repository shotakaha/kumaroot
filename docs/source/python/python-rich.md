# 標準出力したい（`rich`）

```python
from rich import print
print("Hello, [bold magenta]Rich[/bold magenta]!")
```

`rich`は、Pythonの標準出力を装飾するためのライブラリです。

`rich.print`関数に置き換えるだけで、テキストの色やスタイルを指定して、見やすく、わかりやすい出力を実現できます。

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
