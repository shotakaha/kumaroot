# B2したい（`examples/basic/B2`）

![](./fig/exampleB2.png)

`examples/basic/B2`は、固定標的と複数のチェンバーを並べた飛跡検出器です。
外部磁場を与え、粒子が曲がる様子を観察できます。
`Sensitive Detector`と`Hit`の扱いを学ぶことができます。

## ビルドしたい（`cmake`）

```console
$ cd examples/basic/B2/B2a
(B2a) $ mkdir build
(B2a) $ cd build
(B2a/build) $ cmake ..
(B2a/build) $ make -j8
(B2a/build) $ ./exampleB2a
```

`examples/basic/B2/`の中には
`B2a`と`B2b`のディレクトリがあります。
シミュレーションできることは同じなので、どちらをビルドしてもOKです。
マクロファイルが用意されているので、適当に実行して遊んでみます。

## メイン（`exampleB2a.cc`）

## 検出器したい（`DetectorConstruction`）

`B2a`の検出器は、固定標的と複数の円筒型トラッカーで構成されています。
固定標的は入射粒子が最初に衝突する部分で、その材質はマクロで変更できます。

円筒型トラッカーは、ターゲットと同軸に複数枚配置されています。
それぞれ`Sensitive Detector`に割り当てられ、ヒット情報やエネルギー損失を記録できるようになっています。
トラッカーの材質もマクロで変更できます。

## 物理リストしたい（`FTFP_BERT`）

`basic/B1`では、Geant4標準のモジュール型物理リストにある`FTFP_BERT`モデルを使っています。
`FTFP_BERT`は、高エネルギー側で`FTFP`、低エネルギー側で`BERT`に自動で切り替わるようになっている物理モデルです。

## 入射粒子したい（`PrimaryGeneratorAction`）

入射粒子は`PrimaryGeneratorAction`で`G4ParticleGun`を使って生成されます。
この粒子はマクロで変更できます。

## 一様磁場したい（`G4GlobalMagFieldMessenger`）

`B2a`サンプルでは、飛跡検出器全体に一様な磁場を設定できます。
磁場は`G4GlobalMagFieldMessenger`で定義され、値を非ゼロにすると、全体に磁場が作用し、荷電粒子の飛跡が曲がるようになります。

## ``run1.mac``

``run1.mac``では4つの条件で粒子を入射しているようです。

```cfg
# 入射粒子: デフォルト値（種類: 陽子、エネルギー: 3 GeV、方向: (0, 0, 1)）
# 表示レベル: 変更あり
/tracking/verbose 1
/run/beamOn 1
```

```cfg
# 入射粒子: デフォルト値
# 表示レベル: 変更あり
/tracking/verbose 0
/hits/verbose 2
/run/beamOn 1
```

```cfg
# 入射粒子: デフォルト値
# 表示レベル: 変更なし
## /tracking/verbose 0
## /hits/verbose 2
# ターゲットの材料を変更
/B2/det/setTargetMaterial G4_WATER
/B2/det/setChamberMaterial G4_Ar
/run/beamOn 3
```

```cfg
# 入射粒子: 陽子、エネルギー: 0.3GeVに変更
# 表示レベル: 変更なし
## /tracking/verbose 0
## /hits/verbose 2
# 磁場を印加
/globalField/verbose 1
/globalField/setValue 0.2 0 0 tesla
/B2/det/stepMax 1.0 mm
/gun/energy 0.3 GeV
/run/beamOn 3
```



## 外部磁場はどうなってるの？

```cfg
# run1.mac
/globalField/verbose 1
/globalField/setValue 0.2 0 0 tesla
```

マクロで外部磁場の強さを変更しています。
どうやってるんだろう？


## ビルド時のログ

```console
$ cd examples/basic/B2/B2a
(B2a) $ mkdir build

(B2a) $ cd build

(B2a/build) $ cmake ..
-- The C compiler identification is AppleClang 15.0.0.15000309
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found EXPAT: /Library/Developer/CommandLineTools/SDKs/MacOSX14.4.sdk/usr/lib/libexpat.tbd (found suitable version "2.5.0", minimum required is "2.5.0")
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Found OpenGL: /Library/Developer/CommandLineTools/SDKs/MacOSX14.4.sdk/System/Library/Frameworks/OpenGL.framework
-- Found X11: /opt/homebrew/include
-- Looking for XOpenDisplay in /opt/homebrew/lib/libX11.dylib;/opt/homebrew/lib/libXext.dylib
-- Looking for XOpenDisplay in /opt/homebrew/lib/libX11.dylib;/opt/homebrew/lib/libXext.dylib - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Looking for IceConnectionNumber in ICE
-- Looking for IceConnectionNumber in ICE - not found
-- Found XQuartzGL: /usr/X11R6/include
-- Found Geant4: /Users/shotakaha/geant4/11.2.1/lib/cmake/Geant4/Geant4Config.cmake (found version "11.2.1")
-- Configuring done (1.2s)
-- Generating done (0.0s)
-- Build files have been written to: /Users/shotakaha/repos/sandbox/g4work/examples/basic/B2/B2a/build3

(B2a/build) $ make -j8
[ 10%] Building CXX object CMakeFiles/exampleB2a.dir/exampleB2a.cc.o
[ 20%] Building CXX object CMakeFiles/exampleB2a.dir/src/DetectorConstruction.cc.o
[ 40%] Building CXX object CMakeFiles/exampleB2a.dir/src/EventAction.cc.o
[ 40%] Building CXX object CMakeFiles/exampleB2a.dir/src/DetectorMessenger.cc.o
[ 50%] Building CXX object CMakeFiles/exampleB2a.dir/src/TrackerHit.cc.o
[ 60%] Building CXX object CMakeFiles/exampleB2a.dir/src/RunAction.cc.o
[ 70%] Building CXX object CMakeFiles/exampleB2a.dir/src/ActionInitialization.cc.o
[ 80%] Building CXX object CMakeFiles/exampleB2a.dir/src/PrimaryGeneratorAction.cc.o
[ 90%] Building CXX object CMakeFiles/exampleB2a.dir/src/TrackerSD.cc.o
[100%] Linking CXX executable exampleB2a
[100%] Built target exampleB2a

(B2a/build) $ ./exampleB2a
```

## リファレンス

- [Example B2](https://geant4-userdoc.web.cern.ch/Doxygen/examples_doc/html/ExampleB2.html)
