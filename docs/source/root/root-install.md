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

## 環境変数の設定（``$ROOTSYS``）

```console
// for bash/zsh
. /opt/homebrew/bin/thisroot.sh

// for fish
. /opt/homebrew/bin/thisroot.fish
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

``/opt/homebrew/bin/thisroot.sh``を読み込むと、以下のROOT関係の環境変数が設定されます。

```bash
export ROOTSYS=$(root-config --prefix)
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib/root:$LD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$ROOTSYS/lib/root:$DYLD_LIBRARY_PATH
export SHLIB_PATH=$ROOTSYS/lib/root:$SHLIB_PATH
export LIBPATH=$ROOTSYS/lib/root:$LIBPATH
export PYTHONPATH=$ROOTSYS/lib/root:$PYTHONPATH
export MANPATH=$ROOTSYS/share/man:$MANPATH
export CMAKE_PREFIX_PATH=$ROOTSYS:$CMAKE_PREFIX_PATH
export JUPYTER_PATH=$ROOTSYS/etc/notebook:$JUPYTER_PATH
export JUPYTER_CONFIG_DIR=$ROOTSYS/etc/notebook:$JUPYTER_CONFIG_DIR
```

``ROOTSYS=/opt/homebrew``と設定された場合は、
`export ROOTSYS=$(root-config --prefix)`で設定しなおしたほうがよいと思います。

:::{seealso}

僕はMacPortsを使わなくなって久しいですが、
そのときの内容を以下に移動しておきました。

- [](./root-install-macports.md)

:::
