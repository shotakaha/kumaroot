# 設定を確認したい（`root-config`）

```console
$ root-config --help
```

`root-config`でROOTのインストール設定などを確認できます。
シェルスクリプトやC++アプリなどでROOTのパスを設定する場合に、
`root-config --prefix`などで呼び出すことで、パス設定を汎用化できます。

```cpp
gEnv->Print()
```

CINT内では`gEnv->Print()`で確認できます。

```python
import ROOT

ROOT.gEnv.Print()
```

Pythonでは`ROOT.gEnv.Print()`で確認できます。
