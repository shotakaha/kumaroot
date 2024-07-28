# ドキュメントの頼りかた

Geant4は目的別の公式ドキュメントがしっかりとしています。
困ったときは、まずドキュメントを読むとよいと思います。

## For Application Developers

アプリケーションを作成するときは、
[Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/index.html)が参考になると思います。
頭から読み込む必要はなく、自分が実装したい部分をつまみぐいすればよいです。

## For Toolkit Developers

[User's Guide for Toolkit Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForToolkitDeveloper/html/index.html)にはGeant4の設計思想が書いてあります。
それぞれのクラスがどのように設計されているかを知っていると、アプリケーション開発の役に立ちます。

## Reference Guide

[Geant4 Reference Guide](https://geant4.kek.jp/Reference/)は
Doxygenで生成されたクラスリファレンスです。
KEKでホストされているリファレンスは、右上の検索ボックスでクラス名を前方一致検索できます。
それぞれのクラスがどういうメソッドを持つか調べることができます。

ただし、メソッドで得られる内容については詳しく書かれていないため、
関連するヘッダーファイルを確認することをオススメします。
ヘッダーファイルのコメントに追加情報が書かれていることもよくあります。
