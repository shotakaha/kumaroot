# 設定を確認したい（`root-config`）

```console
$ root-config --help
```

`root-config`でインストールしたROOTの設定を確認できます。

## バージョンを確認したい（`--version`）

```console
$ root-config --version
6.32.08

$ root-config --git-revision
6-32-08
```

`--version`などでバージョン情報を細かく確認できます。

## パスを確認したい（`--prefix`）

```console
$ root-config --prefix
```

`root-config --prefix`で、ROOTがインストールされているパスを確認できます。
シェルスクリプトやC++アプリなどでのROOTのパス設定を汎用化できます。

## Pythonを確認したい（`--python-version`）

```console
$ root-config --python-version
3.13.0
```

`--python-version`（もしくは`--python3-version`）で、
PyROOTで使われているPythonのバージョンを確認できます。

[PyROOT](./root-pyroot.md)を使う場合は
`--python-version`のバージョンと
Pythonの実行環境のバージョンを合わせる必要があります。

## 機能を一覧したい（`--features`）

```console
$ root-config --features
cxx17
asimage
builtin_afterimage
builtin_clang
builtin_cling
builtin_freetype
builtin_llvm
builtin_openui5
builtin_vdt
clad
cocoa
dataframe
davix
fftw3
fitsio
fortran
gdml
gnuinstall
http
imt
libcxx
mathmore
mysql
opengl
pyroot
roofit
webgui
root7
rpath
runtime_cxxmodules
shared
sqlite
ssl
tmva
tmva-cpu
tmva-pymva
spectrum
vdt
xml
xrootd
```

`--features`で、有効になっている機能を確認できます。

```cpp
gEnv->Print()
```

CINT内では`gEnv->Print()`で確認できます。

```python
import ROOT

ROOT.gEnv.Print()
```

Pythonでは`ROOT.gEnv.Print()`で確認できます。
