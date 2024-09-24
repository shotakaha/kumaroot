# AnaEx03したい（``extended/analysis/AnaEx03/``）

Geant4.11.1で追加された``/analysis``コマンドのデモになっています。
[G4AnalyticsManager](./geant4-analysismanager.md)をマクロで操作する参考になると思います。

測定器の構成は、[B4](./geant4-examples-b4.md)と同じようなカロリメータです。

## ビルドしたい

```console
$ cd examples/extended/analysis/AnaEx03/
(AnaEx03/) $ mkdir build
(AnaEx03/) $ cd build
(AnaEx03/build/) $ cmake ..
(AnaEx03/build/) $ make -j8
(AnaEx03/build/) $ ./AnaEx03 AnaEx03.in
... write file : e-.root - done
... close file : e-.root - done
... write file : proton.root - done
... close file : proton.root - done
```

``AnaEx03.in``がメインのマクロでした。
``e-``というファイル名に、
100MeVの電子を10ラン、
200MeVの電子を20ラン、
300MeVの電子を30ランを保存、
``proton``というファイル名に
400MeVの陽子を40ラン、
500MeVの陽子を50ラン、を保存するようになっています。

```console
$ ./AnaEx03 AnaEx03.in
// ROOT形式（デフォルト）
$ ./AnaEx03 AnaEx03-root.in
e-.root
proton.root

// XML形式
$ ./AnaEx03 AnaEx03-xml.in
e-_nt*.xml
proton-_nt*.xml

// CSV形式
$ ./AnaEx03 AnaEx03-csv.in
./histo/e-_*.csv
./histo/proton_*.csv
./ntuple/e-_*.csv
./ntuple/proton_*.csv

// HDF5形式（→失敗する）
$ ./AnaEx03 AnaEx03-xml.in
```

保存形式ごとに``AnaEx03.in``をラップしたマクロも用意されています。
ROOT形式とXML形式はカレントディレクトリにファイルが作成されました。
CSV形式は、サブディレクトリにファイルが作成されました。
Geant4をビルドするときにHDF5オプションを有効にしていないため、
HDF5形式の出力は失敗しました。

## リファレンス

- [examples/extended/analysys/AnaEx03](https://geant4-userdoc.web.cern.ch/Doxygen/examples_doc/html/ExampleAnaEx03.html)
