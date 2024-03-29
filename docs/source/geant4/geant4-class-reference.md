# クラスリファレンスの使い方

Geant4のアプリケーションを開発するときにお世話になるのが[Class Reference Guide](https://geant4.kek.jp/Reference/)です。
ここから自分が使っているバージョンを選択し、該当するクラス名やメソッドなどを探します。
あまり使い勝手はよくないですが、右上の検索窓やブランザの検索機能を使って、頑張って探します。

:::{note}

検索窓はあいまい検索（fuzzy match）に対応していないようです。
``V``があったりなかったり、``User``があったりなかったりする長いGeant4のクラス名を、前方から正しく入力しないと検索候補がヒットしないのは、ちょっと不便です。

クラス名が分かっているならば、実装の詳細は、
ソースコード本体を手元に用意して、コマンドライン検索（[fd](../command/command-fd.md)など）で
アタリをつけて、直接開いたほうが読みやすいかもしれません。

:::

## ステップ（``G4Step``）が基本

```cpp
// G4Step *aStep は事前に定義済み
G4double energy_deposit = aStep->GetTotalEnergyDeposit();
```

トラッキングの基本単位はステップ（``G4Step``）です。
[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)や
[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)に
目を通し、できること（得られる物理量など）を把握しておくと、
自分のアプリケーション作成に役立つはずです。

## ファイル名

ファイル名は``PascalCase``が使われています。
ヘッダーファイルは``include/クラス名.hh``、
ソースファイルは``src/クラス名.cc``にあります。

## クラス名

クラス名は``PascalCase``が使われています。
Geant4が提供するクラスの接頭辞は``G4*``が使われています。
さらに抽象クラスは``G4V*``、
ユーザー設定のためのフック用クラスは``G4User*``もしくは``G4VUser*``が使われています。

## 関数名

関数名は``PascalCase``が使われています。
セッターは``Set*``、ゲッターは``Get*``が接頭辞に使われています。

## 変数名

変数名は``PascalCase``が使われています。
また、ゆるめのシステムハンガリアン記法が使われている気がします。

プライベートなメンバー変数の接頭辞には``f*``を使っていることが多く、
変数がポインターの場合は``p*``や``fp*``、
引数の場合は``aValue``や``&aValue``、``&apValue``を使っていることが多いです。

```cpp
// G4Trackのメソッドを抜粋
G4Track::SetTrackID(const G4int aValue)
G4Track::SetPosition(const G4ThreeVector &aValue)
G4Track::SetTouchableHandle(const G4TouchableHandle &apValue)
```

ただし、20年近くの開発の歴史があるためなのか、命名規則が混在している印象です。
なので、関数名／変数名でやっていることがよく分からない場合は
結局ソースコードを眺めてみるのが一番です。

:::{note}

おそらく、ごそっとリファクターするのが難しく、
新しく追加したり、書き直す必要があった部分が、
上記のような書き方になっているのかなと思います。

:::

## 定数

定数（``const``な変数）や``enum``数は``k*``を接頭辞にした``PascalCase``が使われています。

