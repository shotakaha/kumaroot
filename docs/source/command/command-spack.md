# パッケージ管理したい（`spack`）

```console
$ spack install スペック名
```

`spack`は、主にスパコンなどのHPCでパッケージ管理ができるコマンドです。
コンパイラーを変えたり、オプションを変えたりしたパッケージを、それぞれ独立した環境に構築できます。

## インストールしたい（`spack`）

```console
$ brew install spack
$ spack --version
1.2.2
```

`spack`はHomebrewでインストールできます。
クロスプラットフォーム対応で、LinuxやmacOSでも利用できます。

`gnupg`など他に必要なパッケージがあります。
公式ドキュメントの
[System Prerequisites](https://spack.readthedocs.io/en/latest/getting_started.html#system-prerequisites)
を参照してください。

## 利用可能なパッケージを確認したい（`spack list`）

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

`list`コマンドで利用可能なパッケージ一覧を確認できます。
数が多いので`grep`や`ripgrep`などの検索コマンドでパッケージ名を指定するとよいです。

:::{note}

僕もまず、Geant4に関係したパッケージ名を確認するところからはじめました。
関連しそうなパッケージとして`geant4`、`geant4-data`、`geant4-vmc`が見つかりました。
それぞれのパッケージ詳細は`info`コマンドを使って確認ました。

`geant4`パッケージが本体です。これをインストールします。

`geant4-data`パッケージはGeant4本体の依存パッケージのひとつなので、直接インストールする必要はありません。

`geant4-vmc`パッケージは今回は必要なさそうなのでスキップしました。
今後、必要になったときにインストールします。

:::

## パッケージの詳細を確認したい（`spack info`）

```console
$ spack info パッケージ名
$ spack info geant4
$ spack info --by-name geant4
```

`info`コマンドでパッケージ情報の詳細を確認できます。
ウェブサイトのURL（`Homepage`）、
利用可能なバージョン（`Preferred version`／`Safe versions`）、
ビルド時のオプション（`Variants`）、
依存パッケージ（`Build Dependencies`／`Link Dependencies`／`Run Dependencies`）
など確認できます。

ビルド時のオプションは、デフォルトで条件ごと（`when 条件`）で表示されます。
`--by-name`オプションをつけると、オプション名で表示されます。

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
$ spack info --by-name geant4
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

:::{note}

`--variants-by-name`は旧オプション名です。
現行バージョンでは非推奨（deprecated）になっており、実行すると`--by-name`への切り替えを促す警告が表示されます。

:::

## パッケージをインストールしたい（`spack install`）

```console
$ spack install パッケージ名
$ spack install パッケージ名@バージョン
$ spack install パッケージ名 %gcc@パージョン
```

```console
$ spack install geant4
```

`install`コマンドでパッケージをインストールできます。
基本的にすべての関連パッケージでコンパイル作業が必要なので、時間がかかります。

他にも`@バージョン`でバージョン、`%コンパイラー`でコンパイラーを指定できます。

:::{note}

今回は、HPC環境ではなく、手元のMacBook ProにGeant4をインストールするために使ってみました。
ただし、Geant4のインストールはうまくいきませんでした。

:::

## ビルドオプションしたい

```console
$ spack install パッケージ名 オプション="値"
$ spack install パッケージ名 +オプション
```

```console
$ spack install geant4 opengl=True
$ spack install geant4 +opengl
```

`info`コマンドで確認した`Variants`名で、ビルドオプションを追加できます。
パッケージ名のあとに`オプション名=値`を追加します。
オプションの値がブーリアン（`True | False`）の場合は`+オプション名`のように書くこともできます。

:::{note}

```console
$ spack spec geant4 opengl=True
```

`spec`コマンドでインストールされるパッケージ一覧を事前に確認できます。

:::

## ローカルのパッケージを確認したい（`spack find`）

```console
$ spack find -l geant4
-- darwin-sonoma-skylake / apple-clang@15.0.0 -------------------
pzvk6rx geant4@11.1.2  # spack install geant4
t26aalv geant4@11.1.2  # spack install geant4 opengl=True
==> 2 installed packages
```

`find`コマンドでインストール済みのパッケージ情報を確認できます。

ビルドオプションごとにハッシュ値的なものが付与されます。
Homebrewでインストールした`spack`を使った場合、それぞれ次のパスにインストールされていました。

```console
$ spack find -p geant4
-- darwin-sonoma-skylake / apple-clang@15.0.0 -------------------
geant4@11.1.2  /usr/local/Cellar/spack/0.21.1/opt/spack/darwin-sonoma-skylake/apple-clang-15.0.0/geant4-11.1.2-pzvk6rxocxpeauwnlfvwxk6wx3b67wrr
geant4@11.1.2  /usr/local/Cellar/spack/0.21.1/opt/spack/darwin-sonoma-skylake/apple-clang-15.0.0/geant4-11.1.2-t26aalvrzmo2u5jyhj3nvv6gihtty7cv
==> 2 installed packages
```

`-v`オプションでビルドオプションの詳細を確認できます。
有効なオプションは`+オプション名`、
無効なオプションは`~オプション名`で表示されます。

```console
$ spack find -lv geant4
-- darwin-sonoma-skylake / apple-clang@15.0.0 -------------------
pzvk6rx geant4@11.1.2~ipo~motif~opengl~qt~tbb+threads~vecgeom~vtk~x11 build_system=cmake build_type=Release cxxstd=17 generator=make patches=2979cb7
t26aalv geant4@11.1.2~ipo~motif+opengl~qt~tbb+threads~vecgeom~vtk~x11 build_system=cmake build_type=Release cxxstd=17 generator=make patches=2979cb7
```

## パッケージをロードしたい（`spack load`）

```console
# Fish
$ source /opt/homebrew/Cellar/spack/0.21.1/share/spack/setup-env.fish
$ spack load パッケージ名/ハッシュ値
$ spack load geant4

$ spack unload geant4
```

`load`コマンドで、パッケージをロードできます。
その時は、シェルごどの設定を有効にする必要があります。

:::{note}

シェル設定をしていない状態で`spack load`すると、エラーが表示されたあと、シェルごとの対処方法を表示してくれます。

```console
$ spack load geant4
==> Error: `spack load` requires Spack's shell support.

For fish:
    source /opt/homebrew/Cellar/spack/0.21.1/share/spack/setup-env.fish
```

:::

## アンインストールしたい（`spack uninstall`）

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

`uninstall`コマンドでパッケージをアンインストールできます。
同じパッケージ名で複数インストールされている場合は、`パッケージ名/ハッシュ値`で指定します。
確認のプロンプトが表示されるので`y`を入力します。
削除はあっという間です。

## 一時パッケージをアンインストールしたい（`spack gc`）

```console
$ spack gc パッケージ名
$ spack gc geant4
```

`gc`コマンドで、一時的にインストールされたパッケージをアンインストール（ガベージコレクト）できます。

## コンパイラーしたい（`spack compilers`）

```console
$ spack compilers
apple-clang@17.0.0
gcc@16.2.0
```

`compilers`コマンドで利用可能なコンパイラーを確認できます。

```console
$ spack compiler info apple-clang
[e]  apple-clang@=17.0.0 build_system=bundle platform=darwin os=tahoe target=aarch64

  prefix: /usr
  compilers:
    cc: /usr/bin/clang
    cxx: /usr/bin/clang++
    fortran: None
```

`compiler info`でコンパイラーの詳細を確認できます。
`[e]`は外部（external）ツールとして検出されたことを示すマーカーです。
コンパイラーの詳細は`~/.spack/darwin/compilers.yaml`にも書いてありました。

:::{note}

`spack compilers`／`spack compiler info`の出力形式はバージョンによってたびたび変わっています。
古いバージョンでは`-- apple-clang ventura-aarch64 --------`のようなセクション区切り表示でしたが、
現行バージョンではよりシンプルな一覧・キーバリュー形式になっています。

:::
