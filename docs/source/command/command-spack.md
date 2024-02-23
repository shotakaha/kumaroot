# パッケージ管理したい（``spack``）

```console
$ brew install spack
$ spack install スペック名  # パッケージ名のこと
```

[spack](https://spack.io/)は主にスパコンなどのHPCでパッケージ管理ができるコマンドです。
コンパイラーを変えたり、オプションを変えたりしたパッケージを、それぞれ独立した環境に構築できます。

クロスプラットフォーム対応で、LinuxやmacOSでも利用でき、Homebrewでインストールできます。
``gnupg``など他に必要なパッケージがあるので、公式ドキュメントの[System Prerequisites](https://spack.readthedocs.io/en/latest/getting_started.html#system-prerequisites)を参照してください。

今回は、Geant4をインストールするためだけに導入しました。
以下はGeant4を例にコマンドの使い方を確認しています。

:::{note}

基本的なコマンドの使い方とオプションは``spack help``もしくは``spack help コマンド名``で確認できるようになっていました。
より詳細は公式ドキュメントで確認できます。

:::

## インストールしたい（``spack install``）

```console
$ spack install パッケージ名
$ spack install パッケージ名@バージョン
$ spack install パッケージ名 %gcc@パージョン
```

```console
$ spack install geant4
```

``install``コマンドでパッケージをインストールできます。
基本的にすべての関連パッケージでコンパイル作業が必要なので、時間がかかります。

他にも``@バージョン``でバージョン、``%コンパイラー``でコンパイラーを指定できます。

## ビルドオプションしたい

```console
$ spack install パッケージ名 オプション="値"
$ spack install パッケージ名 +オプション
```

```console
$ spack install geant4 opengl=True
$ spack install geant4 +opengl
```

``info``コマンドで確認した``Variants``名で、ビルドオプションを追加できます。
パッケージ名のあとに``オプション名=値``を追加します。
オプションの値がブーリアン（``True | False``）の場合は``+オプション名``のように書くこともできます。

:::{note}

```console
$ spack spec geant4 opengl=True
```

``spec``コマンドでインストールされるパッケージ一覧を事前に確認できます。

:::

## ローカルのパッケージを確認したい（``spack find``）

```console
$ spack find -l geant4
-- darwin-sonoma-skylake / apple-clang@15.0.0 -------------------
pzvk6rx geant4@11.1.2  # spack install geant4
t26aalv geant4@11.1.2  # spack install geant4 opengl=True
==> 2 installed packages
```

``find``コマンドでインストール済みのパッケージ情報を確認できます。

ビルドオプションごとにハッシュ値的なものが付与されます。
Homebrewでインストールした``spack``を使った場合、それぞれ次のパスにインストールされていました。

```console
$ spack find -p geant4
-- darwin-sonoma-skylake / apple-clang@15.0.0 -------------------
geant4@11.1.2  /usr/local/Cellar/spack/0.21.1/opt/spack/darwin-sonoma-skylake/apple-clang-15.0.0/geant4-11.1.2-pzvk6rxocxpeauwnlfvwxk6wx3b67wrr
geant4@11.1.2  /usr/local/Cellar/spack/0.21.1/opt/spack/darwin-sonoma-skylake/apple-clang-15.0.0/geant4-11.1.2-t26aalvrzmo2u5jyhj3nvv6gihtty7cv
==> 2 installed packages
```

``-v``オプションでビルドオプションの詳細を確認できます。
有効なオプションは``+オプション名``、
無効なオプションは``~オプション名``で表示されます。

```console
$ spack find -lv geant4
-- darwin-sonoma-skylake / apple-clang@15.0.0 -------------------
pzvk6rx geant4@11.1.2~ipo~motif~opengl~qt~tbb+threads~vecgeom~vtk~x11 build_system=cmake build_type=Release cxxstd=17 generator=make patches=2979cb7
t26aalv geant4@11.1.2~ipo~motif+opengl~qt~tbb+threads~vecgeom~vtk~x11 build_system=cmake build_type=Release cxxstd=17 generator=make patches=2979cb7
```

## パッケージをロードしたい（``spack load``）

```console
# Fish
$ source /opt/homebrew/Cellar/spack/0.21.1/share/spack/setup-env.fish
$ spack load パッケージ名/ハッシュ値
$ spack load geant4

$ spack unload geant4
```

``load``コマンドで、パッケージをロードできます。
その時は、シェルごどの設定を有効にする必要があります。

:::{note}

シェル設定をしていない状態で``spack load``すると、エラーが表示されたあと、シェルごとの対処方法を表示してくれます。

```console
$ spack load geant4
==> Error: `spack load` requires Spack's shell support.

For fish:
    source /opt/homebrew/Cellar/spack/0.21.1/share/spack/setup-env.fish
```

:::

## パッケージの詳細を確認したい（``spack info``）

```console
$ spack info パッケージ名
$ spack info geant4
$ spack info --variants-by-name geant4
```

``info``コマンドでパッケージ情報の詳細を確認できます。
ウェブサイトのURL（``Homepage``）、
利用可能なバージョン（``Preferred version``／``Safe versions``）、
ビルド時のオプション（``Variants``）、
依存パッケージ（``Build Dependencies``／``Link Dependencies``／``Run Dependencies``）
など確認できます。

ビルド時のオプションは、デフォルトで条件ごと（``when 条件``）で表示されます。
``--variants-by-name``オプションをつけると、オプション名で表示されます。

:::{note}

具体的な表示の違いは以下のようになります。

```console
$ spack info geant4
...
Variants:
    ...
    when build_system=cmake
      build_type [Release]      Debug, MinSizeRel, RelWithDebInfo, Release
          CMake build type
      generator [make]          none
          the build system generator to use
...
```

```console
$ spack info --variants-by-name geant4
...
Variants:
    ...
     build_system [cmake]        cmake
        Build systems supported by the package

    build_type [Release]        Debug, MinSizeRel, RelWithDebInfo, Release
      when build_system=cmake
        CMake build type

    generator [make]            none
      when build_system=cmake
        the build system generator to use
...
```

:::

## 利用可能なパッケージを確認したい（``spack list``）

```console
$ spack list
$ spack list | grep パッケージ名（の一部）
```

```console
$ spack list | grep geant4
geant4
geant4-data
geant4-vmc
```

``list``コマンドで利用可能なパッケージ一覧を確認できます。
数が多いので``grep``や``ripgrep``などの検索コマンドでパッケージ名を指定するとよいです。

:::{note}

ページ構成の都合で順番が後回しになってしまってますが、おそらく一番最初に使うコマンドはこれです。

僕もまず、Geant4に関係したパッケージ名を確認するところからはじめました。
関連しそうなパッケージとして``geant4``、``geant4-data``、``geant4-vmc``が見つかりました。
それぞれのパッケージ詳細は``info``コマンドを使って確認ました。

``geant4``パッケージが本体です。これをインストールします。

``geant4-data``パッケージはGeant4本体の依存パッケージのひとつなので、直接インストールする必要はありません。

``geant4-vmc``パッケージは今回は必要なさそうなのでスキップしました。
今後、必要になったときにインストールします。

:::

## アンインストールしたい（``spack uninstall``）

```console
$ spack uninstall パッケージ名
$ spack uninstall パッケージ名/ハッシュ値
```

```console
$ spack uninstall geant4
$ spack uninstall geant4/pzvk6rx

Do you want to proceed? [y/N] y
==> Successfully uninstalled geant4@11.1.2%apple-clang@15.0.0~ipo~motif~opengl~qt~tbb+threads~vecgeom~vtk~x11 build_system=cmake build_type=Release cxxstd=17 generator=make patches=2979cb7 arch=darwin-sonoma-skylake/pzvk6rx
```

``uninstall``コマンドでパッケージをアンインストールできます。
同じパッケージ名で複数インストールされている場合は、``パッケージ名/ハッシュ値``で指定します。
確認のプロンプトが表示されるので``y``を入力します。
削除はあっという間です。

## 一時パッケージをアンインストールしたい（``gc``）

```console
$ spack gc パッケージ名
$ spack gc geant4
```

``gc``コマンドで、一時的にインストールされたパッケージをアンインストール（ガベージコレクト）できます。

## コンパイラーしたい（``spack compilers``）

```console
$ spack compilers
==> Available compilers
-- apple-clang ventura-aarch64 ----------------------------------
apple-clang@15.0.0

-- gcc ventura-aarch64 ------------------------------------------
gcc@13.2.0
```

``compilers``コマンドで利用可能なコンパイラーを確認できます。

```console
$ spack compiler info apple-clang
apple-clang@15.0.0:
	paths:
		cc = /usr/bin/clang
		cxx = /usr/bin/clang++
		f77 = None
		fc = None
	modules  = []
	operating system  = ventura
```

``compiler info``でコンパイラーの詳細を確認できます。
コンパイラーの詳細は``~/.spack/darwin/compilers.yaml``にも書いてありました。


