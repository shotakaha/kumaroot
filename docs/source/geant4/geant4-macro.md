# マクロしたい（``/control/execute``）

[前のページ](./geant4-command.md)で紹介したコマンド操作を、
ひとつのファイルにまとめてマクロを作成できます。

```cfg
/control/execute ファイル名
/control/execute マクロ名.mac
```

``/control/execute``で対話モードの途中にマクロを読み込むことができます。
引数にはファイル名（の相対パス）を指定します。

Geant4では、慣習的にマクロの拡張子に``.mac``を使っていますが、
テキストファイルであればOKです。

## 表示レベルを変更したい（``/*/verbose``）

```cfg
# verbose levelの設定
# 0: 非表示
/run/verbose 1       # RunManager
/control/verbose 1
/event/verbose 1     # EventManager
/tracking/verbose 1  # TrackingManager
/process/verbose 1
/particle/verbose 1
/cuts/verbose 1
/material/verbose 1
/vis/verbose 1
```

ほとんどのコマンドで出力時の表示レベル（``verbose level``）を設定できます。
設定できるレベルはコマンドによって異なります。
``0``が非表示で、数字が大きいほど詳しく表示されます。
各コマンドで指定できる値は、アプリケーションの対話モードで``help``コマンドを使うと確認できます。

初期のデバッグ時には
``/tracking/verbose 1``、
``/hits/verbose 2``あたりを有効にしておくとよいかもしれません。

:::{hint}

入射粒子のエネルギーを大きくして、トラック数が多くなると、
ターミナル出力が使わない情報でいっぱいになってしまいます。
そのときは非表示にしたほうがいいかもしれません。

:::

## エイリアスしたい（``/control/alias``）

```cfg
/control/alias エイリアス名 "値"

# AnaEx03.in
/analysis/setDefaultFileType {defaultFileType}

# AnaEx03-csv.in
/control/alias defaultFileType "csv"
```

コマンドの一部をエイリアス化して、あとから値を代入できます。
``{エイリアス名}``の形で使い、値は``/control/alias``で先に定義しておく必要があります。
詳細は``AnaEx03``のマクロを参照してください。

## コマンド履歴したい（``/control/saveHistory``）

```cfg
/control/saveHistory ファイル名
/control/saveHistory [G4history.macro]  # [] 内は省略可能
```

実行したコマンドのリストをファイルに保存できます。
ファイル名を省略すると、デフォルトの``G4history.macro``に保存されます。

## データを保存したい（``/analysis/``）

```cfg
/analysis/setDefaultFileType "csv"
/analysis/open ファイル名

# 入射粒子の設定
/gun/particle mu-

# Run1: 10 events
/gun/energy 1.0 GeV
/run/beamOn 10
/analysis/write
/analysis/reset

# Run2: 50 events
/gun/energy 500. MeV
/run/beamOn 50
/analysis/write
/analysis/reset

/analysis/closeFile
```

``/analysis/``コマンドで、測定したデータを保存できます。
``/analysis/closeFile``でファイルを閉じる前ならば、
条件を変更して複数のランを実行できます。

:::{seealso}

``/analysis/``コマンドを使うために、``G4AnalysisManager``を有効にする必要があります。

- [](./geant4-analysismanager.md)

:::

## 起動時にマクロしたい（``G4UImanager``）

```cpp
int main(int argc, char** argv)
{
    // 第一引数がマクロの場合
    if (argc > 1) {
        G4String fileName = argv[1];
        G4String command = "/control/execute ";
        G4UImanager* um = G4UImanager::GetUIpointer();
        um->ApplyCommand(command+fileName);
    }
}
```

``main()``関数で``G4UImanager``を設定すると
アプリケーション起動時に、マクロを読み込むことができます。
引数がないときは、マクロを読み込まずに終了します。

:::{seealso}

起動時に読み込むマクロの作成例は、[](./geant4-macro-setup.md)を参照してください。

:::

:::{hint}

僕は、セットアップ用のマクロ（``setup.mac``）を作成し、
その中で用途別マクロを読み込ませることにしています。

可視化に関するマクロ、ランに関するマクロなど、
適度なサイズに分割することで、マクロの編集が簡単になります。

:::
