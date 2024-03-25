# APIを使いたい（``rp_Init``）

```python
import rp
rp.rp_Init()
```

``rp_Init``でAPIを使うことができます。
``rp_Release``すると、APIが無効になります。

## APIの状態を確認したい（``rp_IsApiInit``）

```python
# rp_IsApiInit
# [ 0 | 1 ]
# [無効|有効]
if not rp.rp_IsApiInit():
    rp.rp_Init()
```

``rp_IsApiInit``でAPIの状態を確認できます。
