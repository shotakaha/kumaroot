# 再利用可能にしたい

Geant4のインストール手順をタスク管理ツールを使って、再利用可能な形にしてみました。
タスク実行には`go-task`を使用し、
`CMakePresets.json`でビルドオプションを設定しました。

Geant4のバージョンを指定すればうまく動くはずです。

## タスクを分割したい

```yaml
# Taskfile.yml
#
# cd ~/geant4
#
# wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.2.1/geant4-v11.2.1.zip
# unzip geant4-v11.2.1.zip
#
# mkdir build
# cd build
# cmake -DCMAKE_INSTALL=~/geant4/11.2.1 ../geant4-v11.2.1
# make -j8
# make install

version: '3'

vars:
  G4VERSION: "11.2.1"
  G4STEM: "geant4-v{{.G4VERSION}}"
  G4ZIP: "{{.G4STEM}}.zip"
  G4URL: "https://gitlab.cern.ch/geant4/geant4/-/archive/v{{.G4VERSION}}/{{.G4ZIP}}"
  G4ROOT: "{{.HOME}}/geant4"
  G4BUILD: "{{.G4ROOT}}/build"
  G4PREFIX: "{{.G4ROOT}}/{{.G4VERSION}}"
  QT_PATH:
    sh: brew --prefix qt@5

tasks:
  deps:
    desc: Install required dependencies via Homebrew
    cmds:
      - brew install --cask cmake
      - brew install --cask xquartz
      - brew install qt@5
      - brew install ninja

  setup:
    desc: Create Geant4 working directory
    cmds:
      - mkdir -p {{.G4ROOT}}
      - mkdir -p {{.G4BUILD}}

  download:
    desc: Download and unzip Geant4 source code
    dir: "{{.G4ROOT}}"
    cmds:
      - wget {{.G4URL}}
      - unzip {{.G4ZIP}}

  configure-make:
    desc: Configure CMake with Unix Makefiles and installation options
    dir: "{{.G4BUILD}}"
    cmds:
      - cmake -DCMAKE_INSTALL_PREFIX={{.G4PREFIX}} \
              -DCMAKE_PREFIX_PATH={{.QT_PATH}} \
              -DGEANT4_INSTALL_DATA=ON \
              -DGEANT4_USE_OPENGL_X11=ON \
              -DGEANT4_USE_QT=ON \
              ../{{.G4STEM}}

  build-make:
    desc: Build Geant4 with make
    dir: "{{.G4BUILD}}"
    cmds:
      - make -j8

  install-make:
    desc: Install Geant4
    dir: "{{.G4BUILD}}"
    cmds:
      - make install

  configure-ninja:
    desc: Configure CMake with Ninja and installation options
    dir: "{{.G4BUILD}}"
    env:
      G4PREFIX: "{{.G4PREFIX}}"
      QT_PATH: "{{.QT_PATH}}"
    cmds:
      - cmake -G Ninja \
              -DCMAKE_INSTALL_PREFIX={{.G4PREFIX}} \
              -DCMAKE_PREFIX_PATH={{.QT_PATH}} \
              -DGEANT4_INSTALL_DATA=ON \
              -DGEANT4_USE_OPENGL_X11=ON \
              -DGEANT4_USE_QT=ON \
              ../{{.G4STEM}}

  build-ninja:
    desc: Build Geant4 with Ninja
    dir: "{{.G4BUILD}}"
    cmds:
      - ninja

  install-ninja:
    desc: Install Geant4
    dir: "{{.G4BUILD}}"
    cmds:
      - ninja install

  clean:
    desc: Remove build directory
    cmds:
      - rm -rf {{.G4BUILD}}

  tree:
    desc: Show installed directory structure
    cmds:
      - tree {{.G4PREFIX}} -L 1
  env:
    desc: Source environment setup script
    cmds:
      - echo "Run 'source {{.G4PREFIX/bin/geant4.sh}}' in your shell"
      - source {{.G4PREFIX}}/bin/geant4.sh
```

## ビルドオプションしたい

```json
{
    "version": 3,
    "cmakeMinimumRequired": {
        "major": 3,
        "minor": 21,
        "patch": 0
    },
    "configurePresets": [
        {
            "name": "default",
            "hidden": false,
            "generator": "Ninja",
            "cacheVariables": {
                "CMAKE_INSTALL_PREFIX": "${env.G4PREFIX}",
                "CMAKE_PREFIX_PATH": "${env.QT_PATH}",
                "GEANT4_INSTALL_DATA": "ON"
            }
        }
    ]
}
```

## ビルドしたい

```console
$ task deps
$ task setup
```

```console
$ task download
```

```console
$ task configure-make
$ task build-make
$ task install-make
```

```console
$ task configure-ninja
$ task build-ninja
$ task install-ninja
```

```console
$ task clean
```

```console
$ task tree
```
