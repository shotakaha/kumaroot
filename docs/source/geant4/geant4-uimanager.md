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

## マクロを読み込む（``/control/execute/``）

```cfg
/control/execute マクロ名
```

``/control/execute``で対話モード中に既存のマクロを読み込むことができます。

## 可視化オプションしたい（``/vis/``）

```cfg
# ビューワを設定
/vis/open [graphics-system-name] [window-size-hint]
/vis/open OGL 600x600-0+0

# 表示レベルの設定
# 0: quiet          // 表示なし
# 1: startup        // +起動/終了メッセージ
# 2: errors         // +エラーメッセージ
# 3: warnings       // +警告メッセージ
# 4: confirmations  // +確認メッセージ
# 5: parameters     // +パラメータ
# 6: all            // +残り全部
/vis/verbose [verbosity]

# ジオメトリを描画
/vis/drawVolume

# アングルを設定
/vis/viewer/set/viewpointVector -1 0 0
/vis/viewer/set/lightsVector -1 0 0

# フレームを設定
# w[ireframe]
# s[urface]
# c[loud]
/vis/viewer/set/style [style]

# テキスト設定
/vis/set/color [red] [green] [blue] [alpha]
/vis/set/textColor [red] [green] [blue] [alpha]
/vis/set/textLayout [layout]
/vis/set/textSize [size]
/vis/set/lineWidth [width]

# その他の表示
/vis/scene/add/scale   # スケールを表示
/vis/scene/add/axes    # 軸を表示（x=red, y=green, z=blue）
/vis/scene/add/date    # 日付のタイムスタンプ
/vis/scene/add/eventID # イベントID

# リフレッシュ
/vis/viewer/set/autoRefresh true
```

