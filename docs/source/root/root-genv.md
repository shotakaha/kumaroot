# 環境変数したい（`gEnv`）

```cpp
gEnv->Print()
```

CINT内では`gEnv->Print()`で、
現在、設定されている環境変数を確認できます。

```python
import ROOT

ROOT.gEnv.Print()
```

Pythonでは`ROOT.gEnv.Print()`で確認できます。
