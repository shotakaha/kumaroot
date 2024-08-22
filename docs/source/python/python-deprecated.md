# deprecated

```console
$ pip3 install Deprecated
```

```python
from deprecated import deprecated

@deprecated(version="バージョン", reason="廃止理由。代替手順など")
def read_data(...):
    pass
```

``@deprecated``デコレーターで、特定の関数が廃止予定であることを通知できます。


## リファレンス

- [deprecated](https://pypi.org/project/Deprecated/)
- [tantale/deprecated](https://github.com/tantale/deprecated)
