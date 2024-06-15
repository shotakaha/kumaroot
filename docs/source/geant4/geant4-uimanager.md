# 対話モードしたい（``G4UImanager``）

```cpp
G4UImanager *um = G4UImanager::GetUIpointer();
um->ApplyCommand("/control/execute vis.mac");
```

``G4UImanager``で対話モードを有効にできます。
``ApplyCommand``メソッドで起動時にコマンドを指定できます。
付属サンプルでは、デフォルトの可視化用マクロを読み込ませていました。



## ランを開始したい（``/run/beamOn``）

```cfg
/run/beamOn [回数]
```

``/run/beamOn``で粒子を入射し、ランを開始できます。

## 粒子を入射したい（``/gun/``）

```cfg
/gun/particle mu-
/gun/energy 200 MeV
/gun/momentum x方向 y方向 z方向
/gun/position x y z 単位
/gun/number 数
/gun/time t 単位
```

``/gun/``以下のコマンドで、入射粒子を操作できます。

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
レベルは``[0, 1, 2]``から選択でき、``0``が非表示です。

初期のデバッグ時には
``/tracking/verbose 1``、
``/hits/verbose 2``あたりを有効にしておくとよいかもしれません。

ただし、入射粒子のエネルギーを大きくしたしりて、
トラック数が多くなるときは非表示にしたほうがいいかもしれません。

## マクロを読み込みたい（``/control/execute``）

```cfg
/control/execute ファイル名
/control/execute マクロ名.mac
```

``/control/execute``で対話モードの途中にマクロを読み込むことができます。
引数にはファイル名（の相対パス）を指定します。

Geant4ではマクロファイルの拡張子に``.mac``を使っていますが、
ASCIIテキストファイルであればOKです。

:::{hint}

僕は、セットアップ用のマクロ（``setup.mac``）を作成し、
その中で用途別マクロを読み込ませることにしています。

可視化に関するマクロ、ランに関するマクロなど、
適度なサイズに分割することで、マクロの編集が簡単になります。

:::
