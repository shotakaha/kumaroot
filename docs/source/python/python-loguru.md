# Loguru

```shell
pip3 install loguru
```

## 使い方

```python
from loguru import logger

logger.debug("デバッグ情報")
logger.error("エラー情報")
```

標準の``logging``モジュールは使うときに設定が必要ですが、この``Loguru``モジュールはほぼ一行で使うことができます。

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
