# 可視化ドライバーの選び方

Geant4は9種類の可視化ドライバーに対応しています。
また、自作の可視化ツールも作れるように設計されています。
Pythonのライブラリ（``Altair``、``Plotly``、``Streamlit``など）で描画できたらおもしろそうです。

ただ、このドライバー選択は初心者にとっては鬼門のひとつだと思います。
理由はどれが自分が使いたいものかよく分からないのと、
OSなどの環境によって動いたり動かなかったりすることもあるからです。

:::{note}

大学院生当時は、オプションを順番に試して、うまくビルドできたものを使っていました。

:::

2022年の講習会スライドには、ドライバーごとのオススメ局面がまとめてありました。
その内容を参考に整理しておきます。

| 利用目的 | オススメのドライバー |
|---|---|
| 実行／描画ウィンドウをまとめたい | Qt |
| リアルタイムでグリグリしたい | Qt, OpenGL|
| 描画した要素をピッキングしたい | Qt、HepRep |
| 複雑な構造体を描画したい | RayTracer |
| ブラウザでグリグリ表示したい | VRML |
| 高解像度のポスター印刷したい | DAWN |
| 放射線治療などで使いたい | gMocren |
| 素早く構造体を点検したい | ASCIITree |

現状では``Qt``が一番モダンで使いやすいと思います。
``OpenGL``、``Qt``、``RayTracer``はビルド時のオプションで有効にする必要があります。
うまくビルドできない場合は Geant4 Forumで同じような状況で質問しているひとがいないか探してみるとよいでしょう。
（たとえば["Geant4 visualization on macOS"](https://geant4-forum.web.cern.ch/t/geant4-visualization-on-macos/11813)など）

```console
// 読みやすさのために改行しましたが、実際は一行にしてください
$ cmake
-DGEANT4_USE_OPENGL_X11=ON
-DGEANT4_USE_QT=ON
-DGEANT4_USE_RAYTRACER_X11=ON
-Dその他のオプション
```

``DAWN``、``VRML``、``HepRep``はデフォルト利用できますが、どういうビューワーで開けばいいのかよく分かりません。
``VRML``は、[オンラインビューワー（IMAGEtoSTL）](https://imagetostl.com/jp/view-vrml-online)を見つけました。


## 利用可能なドライバー

```console
$ ./exampleB1  # Geant4アプリケーションを実行
Available UI session types: [ Qt, tcsh, csh ]
**************************************************************
 Geant4 version Name: geant4-11-02-patch-01 [MT]   (16-February-2024)
...（省略）...
*************************************************************
...（省略）...
Registered graphics systems are:
  ASCIITree (ATree)
  DAWNFILE (DAWNFILE)
  G4HepRepFile (HepRepFile)
  RayTracer (RayTracer)
  VRML2FILE (VRML2FILE)
  gMocrenFile (gMocrenFile)
  TOOLSSG_OFFSCREEN (TSG_OFFSCREEN)
  TOOLSSG_OFFSCREEN (TSG_OFFSCREEN, TSG_FILE)
  OpenGLImmediateQt (OGLIQt, OGLI)
  OpenGLStoredQt (OGLSQt, OGL, OGLS)
  OpenGLImmediateX (OGLIX, OGLIQt_FALLBACK)
  OpenGLStoredX (OGLSX, OGLSQt_FALLBACK)
  RayTracerX (RayTracerX)
  Qt3D (Qt3D)
  TOOLSSG_X11_GLES (TSG_X11_GLES, TSGX11, TSG_QT_GLES_FALLBACK)
  TOOLSSG_QT_GLES (TSG_QT_GLES, TSGQt, TSG)
  TOOLSSG_QT_ZB (TSG_QT_ZB, TSGQtZB)
Default graphics system is: OGL (based on build flags).
Default window size hint is: 600x600-0+0 (based on G4VisManager initialisation).
...（省略）...
```

実行したあとの画面出力の最初のあたりで、現在の環境で利用できるドライバーの一覧を確認できます。
ドライバーの選択は、可視化用マクロ（通常は``vis.mac``）の``/vis/open``コマンドで変更できます。

``exampleB1``の場合、``/vis/open OGL 600x600-0+0``に設定されているため、``OpenGLStoredQt``が起動します。

## ドライバーの設定値

以下は表示設定（``/vis/open ドライバー名``）を変更して``exampleB1``を実行したログです。

| ドライバーの種類 | ``/vis/open``の設定値 | 実行結果 |
|---|---|---|
| デフォルト値 | ``OGL`` | Qtが起動した |
| OpenGLStoredQt | ``OGL`` / ``OGLS`` / ``OGLSQt`` | Qtが起動した |
| OpenGLImmediateQt | ``OGLI`` / ``OGLIQt`` | Qtが起動した |
| OpenGLStoredX | ``OGLSX`` | （起動しなかった） |
| OpenGLImmediateX | ``OGLIX`` | （起動しなかった） |
| Qt3D | ``Qt3D`` | Qtが起動した |
| HepRep | ``HepRepFile`` | ``G4Data{N}.heprep``が作成された |
| RayTracer | ``RayTracer`` | - |
| RayTracerX | ``RayTracerX`` | Xが起動した |
| VRML | ``VRML2FILE`` | ``g4_{NN}.wrl``が作成された|
| DAWN | ``DAWNFILE`` | ``g4_{NNNN}.prim``が作成された |
| gMocren | ``gMocrenFile`` | ``g4_{NN}.wrl``作成された |
| ASCIITree | ``ATree`` | - |

とりあえずデフォルトの``OGL``（=``OpenGLStoredQt``）を使っておけば大丈夫なことが確認できました。

``OpenGLStoredX``、``OpenGLImmediateX``はXが起動すると期待したのですが、``illegal parameter``という警告が表示されました。

``HepRep``、``DAWN``、``VRML``、``gMocren``ではQtインターフェイスが起動し、ランを実行（``/run/beamOn イベント数``）するたびにファイルが生成されました。

