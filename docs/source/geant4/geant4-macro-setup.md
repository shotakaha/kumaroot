# 起動マクロしたい（``setup.mac``）

```cfg
# Setup interactive session
#
# 表示レベルを設定
/control/verbose 0
/control/saveHistory
/run/verbose 0
#
# スレッド数を変更（デフォルト：2）
#/run/numberOfThreads 4
#
# カーネルを初期化する
/run/initialize
#
# 追加マクロを設定する
/control/execute vis.mac    ## 描画設定まとめたマクロ
/control/execute gui.mac    ## メニューボタンをまとめたマクロ
```

起動用のマクロを用意しました。
ファイル名はなんでもよいですが``setup.mac``としました。
このマクロでは、表示レベルの設定、カーネルの初期化、そして追加マクロを読み込みます。

## 起動時にメイン関数で読み込みたい

```cpp
int main()
{
    G4UImanager *um = G4UImanager::GetUIpointer();
    um->ApplyCommand("/control/execute setup.mac");
}
```

アプリケーションを実行したときに``setup.mac``を読み込むようにします。
