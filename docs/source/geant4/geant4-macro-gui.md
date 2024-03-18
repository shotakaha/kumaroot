# メニューしたい（``/gui/``）

```cfg
/gui/addMenu [名前] [ラベル]
/gui/addButton [メニュー名] [ラベル] [コマンド]
```

``/gui/addMenu``と``/gui/addButton``のマクロを使って、簡易的なメニューを作成できます。
以下は付属サンプルB5の``gui.mac``を参考に、あるとよさそうなメニューを作ってみました。

## ファイル

```cfg
/gui/addMenu file File
/gui/addButton file Quit exit
```

## ラン

```cfg
/gui/addMenu run Run
/gui/addButton run "beamOn 1" "/run/beamOn 1"
/gui/addButton run run1 "/control/execute run1.mac"
/gui/addButton run run2 "/control/execute run2.mac"
```

## 入射粒子

```cfg
/gui/addMenu particle Particle
/gui/addButton particle "e-" "/gun/particle e-"
/gui/addButton particle "e+" "/gun/particle e+"
/gui/addButton particle "mu-" "/gun/particle mu-"
/gui/addButton particle "mu+" "/gun/particle mu+"
/gui/addButton particle "proton" "/gun/particle proton"
/gui/addButton particle "geantino" "/gun/particle geantino"
```

## エネルギー

```cfg
/gui/addMenu energy Energy
/gui/addButton energy "50 MeV" "/gun/energy 50 MeV"
/gui/addButton energy "100 MeV" "/gun/energy 100 MeV"
/gui/addButton energy "500 MeV" "/gun/energy 500 MeV"
/gui/addButton energy "1 GeV" "/gun/energy 1 GeV"
```

## ビューワー

```cfg
/gui/addMenu view Viewer
/gui/addButton view "List viewers" "/vis/viewer/list all 1"
/gui/addButton view "Set style surface" "/vis/viewer/set/style surface"
/gui/addButton view "Set style wireframe" "/vis/viewer/set/style wireframe"
/gui/addButton view "Refresh" "/vis/viewer/refresh"
/gui/addButton view "Update" "/vis/viewer/update"
/gui/addButton view "Flush (= refresh + update)" "/vis/viewer/flush"
/gui/addButton view "Update scene (= refresh + update)" "/vis/scene/notifyHandlers"

```
