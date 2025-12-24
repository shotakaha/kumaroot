# ログしたい（``Loguru``）

```bash
$ pip3 install loguru
```

```python
from loguru import logger

logger.debug("Debug情報")
logger.info("Info情報")
logger.warning("Warning情報")
logger.error("Error情報")
```

`loguru`はロギングを簡単にするパッケージです。
標準の`logging`モジュールは初期設定がいろいろ必要ですが、この`loguru`パッケージは設定なしで使いはじめることができます。
デフォルトの出力先は``stderr``（標準エラー出力）です。

:::{note}

ログ表示をカスタマイズする場合は、
`logger.remove()`でデフォルトのハンドラーを
削除するとよいです。

:::

## フォーマットしたい

```python
from loguru import logger

# 詳細なフォーマット
fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} | {message}"
logger.add("app.log", format=fmt)

logger.info("カスタムフォーマットで保存")
```

`format`オプションで、ログメッセージのフォーマットを変更できます。

### よく使うフォーマットオプション

| オプション | 説明 |
|-----------|------|
| `{time}` | ログの発生時刻 |
| `{time:YYYY-MM-DD}` | 時刻フォーマット指定 |
| `{level}` | ログレベル（DEBUG, INFO など） |
| `{name}` | モジュール名 |
| `{function}` | 関数名 |
| `{line}` | 行番号 |
| `{message}` | ログメッセージ本体 |

## ログレベルしたい

```python
from loguru import logger

# デフォルトのログハンドラーを削除
logger.remove()

# DEBUG
fmt = "{time:YYYY-MM-DDTHH:mm:ss} | <level>{level:8}</level> | <cyan>{name}.{function}:{line}</cyan> | <level>{message}</level>"
logger.add(sys.stderr, format=fmt, level="DEBUG")

# SUCCESS
fmt = "{time:YYYY-MM-DDTHH:mm:ss} | <level>{level:8}</level> | <level>{message}</level>"
logger.add(sys.stderr, format=fmt, level="SUCCESS")
```

`logger.add`の`level`オプションで、
ログレベルごとに表示内容や出力先を変更できます。

:::{note}

ログレベルは`argparse`や`typer`などを使ってCLIオプションで変更できるようにしてください。

:::

## ファイルに保存したい

```python
from loguru import logger

# デフォルトのハンドラーを削除（＝stderr出力を無効化）
logger.remove()

# ファイルに保存する
logger.add("app.log")
logger.info("ファイルに保存されます")
```

`logger.add`の第一引数にファイルパスを指定することで、ログをファイルに保存できます。
デフォルトでは、`stderr`の出力に加えてファイルに保存されます。

## ログローテーションしたい

```python
from loguru import logger

# 日ごとにファイルを分割する
logger.add("app.log", rotation="00:00")

# サイズが10MBを超えたら分割
logger.add("app.log", rotation="10 MB")

# ファイル数を制限する（古いファイルを削除）
logger.add("app.log", rotation="00:00", retention="7 days")
```

ローテーション機能を使うことで、ログファイルが大きくなり続けるのを防ぐことができます。

`rotation`オプションで、ログファイルを分割するタイミングを指定できます。
時刻や曜日、ファイルサイズなどを指定できます。

`retention`オプションで、ログファイルを削除するタイミングを指定できます。
日数やファイル数を指定できます。

## ロガーの初期化

```python
# src/packagename/log.py
from loguru import logger
import sys
from pathlib import Path
import platformdirs

def setup_logger(debug: bool = False):
    logger.remove()

    # XDG準拠のログディレクトリを取得
    log_dir = Path(platformdirs.user_log_dir("PACKAGE_NAME"))
    log_dir.mkdir(parents=True, exist_ok=True)

    fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}"

    if debug:
        logger.add(sys.stderr, format=fmt, level="DEBUG")

    # ログファイルを保存
    logger.add(
        log_dir / "app.log",
        format=fmt,
        level="INFO",
        rotation="00:00",
        retention="7 days"
    )

# 使用方法
setup_logger(debug=True)
logger.info("ログが保存されました")
```

実用的なロガーのサンプルです。
`platformdirs`を使うことで、OSに応じた標準的なログディレクトリに保存できます。

## リファレンス

- [Loguru - PyPI](https://pypi.org/project/loguru/)
- [Loguru - Read the Docs](https://loguru.readthedocs.io/)
- [Loguru - GitHub](https://github.com/Delgan/loguru/)
