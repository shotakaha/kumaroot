# MacPortsを使う方法

```{caution}
2013年ころの情報です。
より新しい情報を検索することをオススメします。
```

Macユーザの場合``MacPorts``を使ってインストールする方法が楽ちんでオススメです。
環境変数（``$ROOTSYS``、``$LD_LIBRARY_PATH``、``$DYLD_LIBRARY_PATH``など）の設定も不要です。

``MacPorts`` に登録されているポート名（パッケージ名）には``root5``と``root6``があります。
両方をインストールすることはできますが、同時に使うことはできません。
簡単に切り替える方法は後述します。

## ROOT6

{command}`variants` なしでインストールした場合です。
``python27`` はデフォルトで **ON** です。

```bash
$ sudo port install root6
$ port installed root6
The following ports are currently installed:
root6 @6.04.02.99_0+cocoa+gcc48+graphviz+gsl
        +http+minuit2+opengl+python27+roofit
        +soversion+ssl+tmva+xml
```

## ROOT6 + python34

{command}`variants` に ``python34`` を指定した場合です。
最近インストールしてみたので ``gcc5`` がデフォルトになってます。

```bash
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

## ROOT5

{command}`variants` なしでインストールしました。
``python27`` はデフォルトで **OFF** です。
後述する ``PyROOT`` を使用する場合は **ON** にしてインストールする必要があります。

```bash
$ sudo port install root5
$ port installed root5
The following ports are currently installed:
root5 @5.34.34_0+cocoa+gcc48+graphviz+gsl
        +http+minuit2+opengl+roofit
        +soversion+ssl+tmva+xml (active)
```
