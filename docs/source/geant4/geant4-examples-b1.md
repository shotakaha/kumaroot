# B1したい（``examples/basic/B1/``）

```console
$ tree B1 -L 2
B1
├── CMakeLists.txt
├── GNUmakefile
├── History
├── README
├── exampleB1.cc
├── include
│   ├── ActionInitialization.hh
│   ├── DetectorConstruction.hh
│   ├── EventAction.hh
│   ├── PrimaryGeneratorAction.hh
│   ├── RunAction.hh
│   └── SteppingAction.hh
├── src
│   ├── ActionInitialization.cc
│   ├── DetectorConstruction.cc
│   ├── EventAction.cc
│   ├── PrimaryGeneratorAction.cc
│   ├── RunAction.cc
│   └── SteppingAction.cc
├── init_vis.mac
├── vis.mac
├── exampleB1.in
├── exampleB1.out
├── run1.mac
├── run2.mac
└── tsg_offscreen.mac
```

B1のディレクトリ構造は上のようになっています。
メインのプログラムは``exampleB1.cc``で、``include/*.hh``と``src/*.cc``に関係するソースコードが格納されています。
``*.mac``は実行ファイルの引数に指定できるマクロファイルです。

``exampleB1.in``もマクロファイルです。
これを読み込んだときの出力が``exampleB1.out``です。

## ビルドした（``cmake``）

```console
$ cd B1
(B1) $ mkdir build
(B1) $ cd build
(B1/build) $ cmake ..
(B1/build) $ make
(B1/build) $ ./exampleB1 run1.mac
(B1/build) $ ./exampleB1 run2.mac
```

``exampleB1``アプリケーションもGeant4本体と同じように``cmake``でビルドします。
``examples/basic/B1/``の中にビルド用ディレクトリを（``build``）を作成します。
その中で、``cmake ..``と``make``して実行ファイルを生成します。

## メインンプログラム

```cpp
//////////////////////////////////////////////////
// exampleB1.cc
//////////////////////////////////////////////////
auto *runManager = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default)
// Detector construction
runManager->SetUserInitialization(new DetectorConstruction());

// Physics list
G4VModularPhysicsList* physicsList = new QBBC;
physicsList->SetVerboseLevel(1);
runManager->SetUserInitialization(physicsList);

// User action initialization
runManager->SetUserInitialization(new ActionInitialization());

G4UIExecutive *ui = new G4UIExecutive(argc, argv);
G4VisManager *visManager = new G4VisExecutive;
G4UImanager *uiManager = G4UImanager::GetUIpointer();
```

メインプログラムは``exampleB1.cc``です。
その中のマネージャーの仕事を集めてみました。

``exampleB1.cc``で使われているマネージャーたちを集めてみました。
4種類のマネージャーがいました。ランの管理人が``G4RunManagerFactory``クラスで、その他はビジュアライズ関係の管理人たちです。

