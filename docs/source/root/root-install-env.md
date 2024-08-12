# 環境変数したい（``thisroot.sh``）

```console
// for bash/zsh
$ . $(root-config --prefix)/bin/thisroot.sh

// for fish
$ . $(root-config --prefix)/bin/thisroot.fish
```

ROOTをインストールしたディレクトリの中にある
``bin/thisroot.sh``を読み込むと、環境変数を設定できます。
スクリプトはシェルごとに用意されています。

ROOT 6.22以降は、この設定が原則不要となりました。
ただし、[PyROOT](./root-pyroot.md)を使う場合は、``PYTHONPATH``の設定が必要なため、このファイルを読み込む必要があります。

:::{seealso}

``brew info root``のCaveatsに
ROOT 6.22以降では、原則読み込み不要になったことが書いてあります。

```console
$ brew info root
...
> ==> Caveats
As of ROOT 6.22, you should not need the thisroot scripts;
but if you depend on the custom variables set by them, you can still run them:
...
```

:::

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

環境変数を設定する場合、ROOTのバージョン番号が明記された本体パスを指定する必要があります。

```console
// thisroot.sh のパスを検索
$ locate thisroot.sh
/opt/homebrew/Cellar/root/6.32.02_1/bin/thisroot.sh
/opt/homebrew/bin/thisroot.sh

// 片方はシンボリックリンクであることを確認
$ ls -l /opt/homebrew/bin/thisroot.sh
/opt/homebrew/bin/thisroot.sh@ -> ../Cellar/root/6.32.02_1/bin/thisroot.sh
```

``locate thisroot.sh``で確認すると、2種類のパスが見つかりました。
本体は``/opt/homebrew/Cellar/root/6.32.02_1/bin/thisroot.sh``のようにROOTのバージョンを含んだパスで、
``/opt/homebrew/bin/thisroot.sh``はそこへのシンボリックリンクになっていました。

``/opt/homebrew/bin/``のパスのほうがROOTのバージョンを含まず、汎用的に使えそうですが、``ROOTSYS=/opt/homebrew``と設定されてしまいました。
これは、シェルスクリプト内の処理で、現在のディレクトリの親ディレクトリをROOTSYSとして設定するためです。

なお、ROOTSYSがすでに定義されている場合は、そちらが優先されます。
`ROOTSYS`をあらかじめ定義しておくのもよいかもしれません。

```bash
export ROOTSYS=$(root-config --prefix)
```

:::
