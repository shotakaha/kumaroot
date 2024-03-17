# ファイル出力したい（``G4VAnalysisManager``）

Geant4は独自のデータベース形式を持っていません。
その代わりに、ユーザー自身がいろいろなフォーマットに出力できるように[G4VAnalysisManager](https://geant4.kek.jp/Reference/11.2.0/classG4VAnalysisManager.html)というインターフェース的なクラスが用意されています。

## CSV形式にしたい

一般的なユーザーであればCSV形式で出力するとよいと思います。
CSV形式であれば、ユーザーが使い慣れているツールで解析できます。

## ROOT形式にしたい

HEP業界のユーザーであればROOT形式のほうが使いやすいと思います。
付属サンプルROOTファイルで出力されるようになっています。

## AnalysisManagerを使いたくない

ユーザーのお好みで
``std::tuple``、
``std::map``、
``std::vector``などを使って、
ファイルに出力すればOKだそうです。
