# 再利用可能にしたい

Geant4のインストール手順をタスク管理ツールを使って、再利用可能な形にしてみました。
タスク実行には`go-task`を使用し、
`CMakePresets.json`でビルドオプションを設定しました。

Geant4のバージョンを指定すればうまく動くはずです。

## タスクを分割したい

```yaml
# Taskfile.yml
#
# 1. Workspace
# cd ~/geant4
#
# 2. Download source code from the repository
# wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.2.1/geant4-v11.2.1.zip
# unzip geant4-v11.2.1.zip
#
# 3. Configure
# mkdir build
# cmake -DCMAKE_INSTALL="$(pwd)/v11.2.1" -S "$(pwd)/geant4-v11.2.1" -B "$(pwd)/build"
# make -j8
# make install

version: '3'

vars:
  G4VERSION: "v11.2.1"
  G4ROOT: "{{.HOME}}/geant4"
  G4SOURCE: "{{.G4HOME}}/geant4-{{.G4VERSION}}"
  G4BUILD: "{{.G4HOME}}/build"
  G4PREFIX: "{{.G4HOME}}/{{.G4VERSION}}"
  G4ZIP: "geant4-{{.G4VERSION}}.zip"
  G4URL: "https://gitlab.cern.ch/geant4/geant4/-/archive/{{.G4VERSION}}/{{.G4ZIP}}"

  QT_PATH:
    sh: brew --prefix qt@5

tasks:
  deps:
    desc: Install required dependencies via Homebrew
    cmds:
      - brew install cmake
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
    dir: "{{.G4ROOT}}"
    env:
      G4PREFIX: "{{.G4PREFIX}}"
      QT_PATH: "{{.QT_PATH}}"
    cmds:
      - mkdir {{.G4BUILD}}
      - cmake -DCMAKE_INSTALL_PREFIX={{.G4PREFIX}} \
              -DCMAKE_PREFIX_PATH={{.QT_PATH}} \
              -DGEANT4_INSTALL_DATA=ON \
              -DGEANT4_USE_OPENGL_X11=ON \
              -DGEANT4_USE_QT=ON \
              -S {{.G4SOURCE}}
              -B {{.G4BUILD}}

  configure-ninja:
    desc: Configure CMake with Ninja and installation options
    dir: "{{.G4ROOT}}"
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
              -S {{.G4SOURCE}}
              -B {{.G4BUILD}}

  build:
    desc: Build Geant4
    dir: "{{.G4ROOT}}"
    cmds:
      - cmake --build "{{.G4BUILD}}" --parallel

  install:
    desc: Install Geant4
    dir: "{{.G4ROOT}}"
    cmds:
      - cmake --install "{{.G4BUILD}}"

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
