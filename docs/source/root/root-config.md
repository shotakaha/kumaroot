# 設定を確認したい（`root-config`）

```console
$ root-config --help
```

`root-config`でインストールしたROOTの設定を確認できます。

## パスを確認したい（`--prefix`）

```console
$ root-config --prefix
```

`root-config --prefix`で、ROOTがインストールされているパスを確認できます。
シェルスクリプトやC++アプリなどでのROOTのパス設定を汎用化できます。

## バージョンを確認したい（`--version`）

```console
$ root-config --version
6.40.00

$ root-config --git-revision
6-40-00
```

`--version`でバージョン番号を確認できます。

## Pythonを確認したい（`--python-version`）

```console
$ root-config --python-version
3.14.5

$ root-config --python3-version
3.14.5
```

`--python-version`（もしくは`--python3-version`）で、
PyROOTがビルドされたPythonのバージョンを確認できます。

[PyROOT](./root-pyroot.md)を使う場合は
この`--python-version`のバージョンと
Pythonの実行環境のバージョンを合わせる必要があります。

## 機能を一覧したい（`--features`）

```console
$ root-config --features
cxx17
asimage
asimage_tiff
builtin_clang
builtin_cling
builtin_civetweb
builtin_llvm
builtin_openui5
builtin_vdt
check_connection
clad
cocoa
curl
dataframe
davix
fftw3
fitsio
fortran
gdml
geom
gnuinstall
http
imt
libcxx
mathmore
opengl
pyroot
roofit
root7
runtime_cxxmodules
shared
spectrum
sqlite
ssl
thisroot_scripts
tmva
tmva-cpu
tmva-cudnn
tpython
vdt
webgui
xml
xrootd
```

`--features`で、有効になっている機能を確認できます。
