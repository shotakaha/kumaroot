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

ログするためのパッケージです。
標準モジュールの``logging``はいろいろ設定が必要ですが、この``Loguru``モジュールはノー設定で使うことができます。
デフォルトの出力先は``stderr``（標準エラー出力）です。

## ログレベルによって出力内容を変更したい

```python
logger.remove()
if args.debug:
    fmt = "{time:YYYY-MM-DDTHH:mm:ss} | <level>{level:8}</level> | <cyan>{name}.{function}:{line}</cyan> | <level>{message}</level>"
    logger.add(sys.stderr, format=fmt, level="DEBUG")
else:
    fmt = "{time:YYYY-MM-DDTHH:mm:ss} | <level>{level:8}</level> | <level>{message}</level>"
    logger.add(sys.stderr, format=fmt, level="SUCCESS")
```

デバッグモードの切り替えには``argparse``モジュールを使っています。
ノーマルモードとデバッグモードで出力内容を変更したいので、
最初に``logger.remove``でロガーを空っぽにしてから、
必要な設定をそれぞれに``logger.add``しています。

## リファレンス

- [Loguru - PyPI](https://pypi.org/project/loguru/)
- [Loguru - Read the Docs](https://loguru.readthedocs.io/)
- [Loguru - GitHub](https://github.com/Delgan/loguru/)
