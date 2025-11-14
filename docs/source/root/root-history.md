# ROOTの歴史

ROOTは1994年にRene BrunとFons Rademakerによってスイス・CERNで開発がスタートしました。
Fortranを使った解析ツール（PAW）の知見を活かして、C++によるオブジェクト指向のデータ解析ツールとして設計されました。
今日まで高エネルギー物理学の標準的なフレームワークとして使用されています。

## PAWからROOTへ

PAW（Physics Analysis Workstation）はFortranで書かれた対話型データ解析ツールです。
CERNLIB（CERN Program Library）を基盤として構築され、HBOOK等の複数の解析ツールを統合していました。

PAWは1986年にCERNで開発が始まり、高エネルギー物理学分野で何十年も標準的なツールとして使用されてきました。
しかし2003年にCERNLIBのサポートが終了し、2014年にはPAWの開発・サポートも終了しました。

ROOTはPAWの実質的な後継ツールです。
TTreeの設計（PAW/HBOOKのNTuple概念を継承）、メソッド命名規則（`SetXxx()`, `GetXxx()`）、対話型開発環境など、PAWの思想を多く受け継いでいます。
ただしFortran（手続き型）からC++（オブジェクト指向）へ進化し、モダンなプログラミング環境を実現しています。

## CINTからClingへ

ROOTは対話型のC++開発環境を備えています。
長年、CINTと呼ばれるCERNが独自開発したC++インタープリターが使用されてきました。
ROOT 6からはCINTの後継であるClingに置き換わりました。

ClingはClang/LLVMコンパイラーをベースにしており、より標準的なC++に準拠しています。
CINTより高速で動き、C++11以降のモダンなC++機能（ラムダ式、auto、std::tupleなど）をサポートしています。

:::{note}

`cling`はスタンドアロンでも利用可能です。Homebrewでインストールできます。

```console
$ brew install cling
$ cling
```

:::

## TTreeとRDataFrame

`TTree`はROOTのもっとも基本的で重要な設計思想です。
ROOTの開発当初から変わらず、TAF/HBOOKのNTuple概念を継承した階層的データ構造として設計されています。
`branch`（ブランチ／枝）と`leaf`（リーフ／葉）の概念により、複雑な実験データを効率的に保存・読み込み・解析できます。
`TTree`のブランチ指定や`GetEntry()`ループはとても強力で、さまざまな実験の複雑な要求にも柔軟に対応できます。

しかし、ROOTが数十年使われ続ける中で
「TTreeへのアクセスをもっと簡潔に書きたい」
という要望も増えました。
そこで2018年のROOT 6.14から導入されたのが`RDataFrame`です。
`RDataFrame`は関数型プログラミングのパラダイムを採用し、`TTree`の上に高レベルなAPIを提供しています。

`RDataFrame`は、`TTree`に置き換わる機能ではなく、`TTree`という堅牢な基礎の上に、より使いやすいインターフェイスを追加した進化形です。
そのため、内部的には`TTree`を活用しながら、Pythonの`pandas`などの近代的なデータ解析ツールに近い使い方を実現しています。
