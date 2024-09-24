# ビルドを確認する（``ccmake``）

```console
// ビルド用ディレクトリで作業する
// CMakeLists.txtがあるディレクトリを指定する
(~/geant4/build/) $ ccmake ../geant4-v11.2.1/
```

``ccmake``でビルドオプションをターミナル上で視覚的に変更できます。
インストール先となる``CMAKE_INSTALL_PREFIX``の設定が正しいことを確認します。
Qtを使う場合は、``QT_DIR``（と``Qt5``系）のパスが設定されていることを確認してください。

``GEANT4_USE``系の設定フラグは、この画面でトグルして変更できます。
変更を加えた場合は``[c] Configure``を実行し、``CMakeLists.txt``を再生成します。

:::{figure-md}
![](./fig/ccmake01.png)

ビルドオプションの確認（ページ1）
:::

:::{figure-md}
![](./fig/ccmake02.png)

ビルドオプションの確認（ページ2）
:::
