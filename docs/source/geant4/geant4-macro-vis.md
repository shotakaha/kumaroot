# 描画設定したい（``/vis/``）

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

``/vis/``以下のコマンドを使って、可視化ツールの設定ができます。
付属サンプルB1の可視化マクロを参考にしました。
