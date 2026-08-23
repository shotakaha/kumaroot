# インストールしたい（`port install root6`）

```{caution}
現在は、Homebrewを使ったインストールをオススメします。

このページは、2011年から2013年ころに、MacPortsを使っていたころのメモを元に作成しています。
出力されている内容は、ちょっと異なるかもしれません。
もし、MacPortsを使ってインストールする場合は、公式ドキュメントをはじめとした、より新しい情報を参照してください。
```

Macユーザの場合、`MacPorts`を使ってROOTをインストールする方法が楽ちんでオススメです。
環境変数（`$ROOTSYS`、`$LD_LIBRARY_PATH`、`$DYLD_LIBRARY_PATH`など）の設定も不要です。

ポート名（パッケージ名）には`root5`と`root6`があります。
両方をインストールすることはできますが、同時に使うことはできません。
簡単に切り替える方法は後述します。

## ROOT6したい（`root6`）

```console
$ sudo port install root6
$ port installed root6
The following ports are currently installed:
root6 @6.04.02.99_0+cocoa+gcc48+graphviz+gsl
        +http+minuit2+opengl+python27+roofit
        +soversion+ssl+tmva+xml
```

`variants`なしで`root6`をインストールしてみました。
`python27`がデフォルトで有効になっていることが確認できました。

## ROOT6 + python34したい（`root6 +python34`）

```console
$ sudo port install root6 +python34
$ port installed root6
The following ports are currently installed:
root6 @6.04.02.99_0+cocoa+gcc48+graphviz+gsl
        +http+minuit2+opengl+python27+roofit
        +soversion+ssl+tmva+xml
root6 @6.04.02.99_0+cocoa+gcc5+graphviz+gsl
        +http+minuit2+opengl+python34+roofit
        +soversion+ssl+tmva+xml (active)
```

`variants`に`+python34`を指定して`root6`をインストールしてみました。
`python34`が有効になっていることが確認できました。
また、前回のインストールから時間が経っていたため、`gcc5`がデフォルトになっていることも確認できました。

## ROOT5したい（`root5`）

```console
$ sudo port install root5
$ port installed root5
The following ports are currently installed:
root5 @5.34.34_0+cocoa+gcc48+graphviz+gsl
        +http+minuit2+opengl+roofit
        +soversion+ssl+tmva+xml (active)
```

`variants`なしで`root5`をインストールしてみました。
`python27`はデフォルトで無効になっていました。
`PyROOT`を使う場合は`root5 +python27`でインストールする必要があります。

## バージョンを切り替えたい（`port select`）

```console
$ sudo port select --list root
Available versions for root:
    none
    root5
    root6
$ sudo port select --set root root6
$ port select --list root
Available versions for root:
    none
    root5
    root6 (active)
```

`port select`で、インストール済みの`root5`と`root6`のバージョンを切り替えることができます。
