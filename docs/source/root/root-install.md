# インストール

Macユーザーの場合、``Homebrew``を使ってインストールできます。
インストールには``Xcode``が必要です。

```console
$ brew install root

$ which root
/opt/homebrew/bin/root

$ root --version
ROOT Version: 6.32.02
Built for macosxarm64 on Jun 18 2024, 03:44:55
From heads/master@tags/v6-32-02
```

:::{note}

```console
$ brew info root
...
> ==> Caveats
As of ROOT 6.22, you should not need the thisroot scripts; but if you depend on the custom variables set by them, you can still run them:
...
```

以前は ``thisroot.sh``（や ``thisroot.fish``など）のシェルスクリプトを読み込む必要がありましたが、ROOT 6.22以降は必要がなくなったようです。

:::

```{toctree}
---
maxdepth: 1
---
root-install-macports
```

## PyROOTしたい

```python
import ROOT
```

HomebrewでインストールするとPyROOTも標準で使えます（たぶん）
