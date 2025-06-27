# オススメの可視化ドライバー

```console
$ cmake \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_QT=ON \
-DGEANT4_USE_RAYTRACER_X11=ON \
```

現状では、`OpenGL`と`Qt`は必須、
`RayTracer`はオプションで有効にしておけばOKです。

:::{note}

大学院生で使っていたときは、オプションの組み合わせをいくつか順番に試して、
うまくビルドできたものを使っていた気がします。

:::

:::{note}

自作の可視化ツールも作れるように設計されています。
Pythonのライブラリ（``Altair``、``Plotly``、``Streamlit``など）で
描画できたらおもしろそうです。

:::

## 可視化ドライバーの選び方

Geant4は9種類の可視化ドライバーに対応しています。
ただし、この可視化ドライバーの選択は初心者にとって鬼門のひとつです。
なぜなら、初見のドライバー名が多く、自分の用途に適したものがよく分からないのと、
OSなどの環境によって動いたり動かなかったりすることもあるからです。

2022年の講習会スライドに、ドライバーの選び方が整理されていました。

| 利用目的 | オススメのドライバー |
|---|---|
| 実行／描画ウィンドウをまとめたい | Qt |
| リアルタイムでグリグリしたい | Qt, OpenGL|
| 複雑な構造体を描画したい | RayTracer |
| 描画した要素をピッキングしたい | Qt、HepRep |
| ブラウザでグリグリ表示したい | VRML |
| 高解像度のポスター印刷したい | DAWN |
| 放射線治療などで使いたい | gMocren |
| 素早く構造体を点検したい | ASCIITree |

`DAWN`、`VRML`、`HepRep`は形式はGeant4のデフォルトで出力できるようなのですが、
それらの形式を開くことができる外部ビューワーが見つかりませんでした。
開発やメンテナンスも停滞しているようなので、積極的に選択する理由はないです。

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

ユーザーアプリを実行したあとの画面出力で、現在の環境で利用できるドライバーの一覧を確認できます。

```console
...（省略）...
Default graphics system is: OGL (based on build flags).
Default window size hint is: 600x600-0+0 (based on G4VisManager initialisation).
...（省略）...
```

`exampleB1`では、`/vis/open OGL 600x600-0+0`に設定されているため、`OpenGLStoredQt`が起動します。

## ドライバーを変更したい（`/vis/open`）

可視化ドライバーは、マクロの`/vis/open`コマンドで変更できます。

以下は表示設定（`/vis/open ドライバー名`）を変更して`exampleB1`を実行した記録です。

| ドライバーの種類 | `/vis/open`の設定値 | 実行結果 |
|---|---|---|
| デフォルト値 | `OGL` | Qtが起動した |
| OpenGLStoredQt | `OGL` / `OGLS` / `OGLSQt` | Qtが起動した |
| OpenGLImmediateQt | `OGLI` / `OGLIQt` | Qtが起動した |
| OpenGLStoredX | `OGLSX` | （起動しなかった） |
| OpenGLImmediateX | `OGLIX` | （起動しなかった） |
| Qt3D | `Qt3D` | Qtが起動した |
| HepRep | `HepRepFile` | `G4Data{N}.heprep`が作成された |
| RayTracer | `RayTracer` | - |
| RayTracerX | `RayTracerX` | Xが起動した |
| VRML | `VRML2FILE` | `g4_{NN}.wrl`が作成された|
| DAWN | `DAWNFILE` | `g4_{NNNN}.prim`が作成された |
| gMocren | `gMocrenFile` | `g4_{NN}.wrl`作成された |
| ASCIITree | `ATree` | - |

とりあえずデフォルトの`OGL`（=`OpenGLStoredQt`）を使っておけば大丈夫なことが確認できました。

`OpenGLStoredX`、
`OpenGLImmediateX`
はXが起動すると期待したのですが、`illegal parameter`という警告が表示されました。

`HepRep`、`DAWN`、`VRML`、`gMocren`ではQtインターフェイスが起動し、
ランを実行（``/run/beamOn イベント数``）するたびにファイルが生成されました。
