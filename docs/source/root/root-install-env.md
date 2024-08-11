# 環境変数したい（``thisroot.sh``）

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

```console
// for bash/zsh
$ . $(root-config --prefix)/bin/thisroot.sh

// for fish
$ . $(root-config --prefix)/bin/thisroot.fish
```

ROOTをインストールしたディレクトリの中にある
``bin/thisroot.sh``を読み込むと、環境変数を設定できます。
設定される環境変数は以下のとおりです。

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

:::{caution}

```console
// thisroot.sh のパスを検索
$ locate thisroot.sh
/opt/homebrew/Cellar/root/6.32.02_1/bin/thisroot.sh
/opt/homebrew/bin/thisroot.sh

// 片方はシンボリックリンクであることを確認
$ ls -l /opt/homebrew/bin/thisroot.sh
/opt/homebrew/bin/thisroot.sh@ -> ../Cellar/root/6.32.02_1/bin/thisroot.sh
```

``thisroot.sh``のパスを確認すると、2箇所がヒットしました。
読み込むスクリプトは``/opt/homebrew/Cellar/root/6.32.02_1/bin/`` のようのROOTのバージョンが明記されたパスを指定する必要があります。

``/opt/homebrew/bin/``のパスのほうがROOTのバージョンを含まず、汎用的に使えそうですが、``ROOTSYS=/opt/homebrew``と設定されてしまいます。
これは、シェルスクリプト内の処理で、現在のディレクトリの親ディレクトリをROOTSYSとして設定するためです。

なお、ROOTSYSがすでに定義されている場合は、そちらが優先されます。

```console
export ROOTSYS=$(root-config --prefix)
```

あらかじめROOTSYSを定義しておくのもよいかもしれません。


:::







