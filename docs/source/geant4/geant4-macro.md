# マクロしたい（``/control/execute``）

[前のページ](./geant4-command.md)で紹介したコマンド操作を、
ひとつのファイルにまとめてマクロを作成できます。

```cfg
/control/execute ファイル名
/control/execute マクロ名.mac
```

``/control/execute``を使うと、対話モードの途中でマクロを読み込めます。
引数には、ファイル名（相対パス）を指定します。

Geant4では、慣習的にマクロの拡張子として``.mac``を使いますが、
テキストファイルであれば拡張子は何でも構いません。

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

多くのコマンドで、出力の詳しさを表す表示レベル（``verbose level``）を設定できます。
レベルの範囲はコマンドによって異なり、``0``は非表示です。数字が大きいほど詳しく表示されます。
指定できる値は、対話モードで``help``コマンドを使うと確認できます。

デバッグの初期段階では、
``/tracking/verbose 1``や``/hits/verbose 2``を設定しておくと便利です。

:::{hint}

入射粒子のエネルギーを大きくするとトラック数が増え、
ターミナルが不要な情報で埋まってしまいます。
そのようなときは、表示レベルを``0``にしてください。

:::

## エイリアスしたい（``/control/alias``）

```cfg
/control/alias エイリアス名 "値"

# AnaEx03.in
/analysis/setDefaultFileType {defaultFileType}

# AnaEx03-csv.in
/control/alias defaultFileType "csv"
```

コマンドの一部を``{エイリアス名}``で置き換えられます。
値は``/control/alias``で定義しておく必要があり、使う前に定義しておいてください。
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

``/analysis/``コマンドで、測定したデータをファイルに保存できます。
``/analysis/closeFile``でファイルを閉じるまでは、
条件を変えて複数のランを続けて実行できます。

:::{seealso}

``/analysis/``コマンドを使うには、``G4AnalysisManager``を有効にしておく必要があります。

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

``main()``関数で``G4UImanager``を使うと、
アプリケーションの起動時にマクロを読み込めます。
引数がない場合は、マクロを読み込まずに処理を終えます。

:::{seealso}

起動時に読み込むマクロの例は、[](./geant4-macro-setup.md)を参照してください。

:::

:::{hint}

僕は、セットアップ用のマクロ（``setup.mac``）を作成し、
その中で用途別マクロを読み込ませることにしています。

可視化に関するマクロ、ランに関するマクロなど、
適度なサイズに分割することで、マクロの編集が簡単になります。

:::
