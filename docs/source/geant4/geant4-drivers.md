# 可視化ドライバー

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

| 利用目的 | オススメのドライバー | ``/vis/open`` |
|---|---|---|
| 実行／描画ウィンドウをまとめたい | Qt | |
| リアルタイムでグリグリしたい | Qt, OpenGL| OGLSX |
| 描画した要素をピッキングしたい | Qt、HepRep | |
| 複雑な構造体を描画したい | RayTracer | |
| ブラウザでグリグリ表示したい | VRML | VRML |
| 高解像度のポスター印刷したい | DAWN | DAWNFILE |
| 放射線治療などで使いたい | gMocren | |
| 素早く構造体を点検したい | ASCIITree | |

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
