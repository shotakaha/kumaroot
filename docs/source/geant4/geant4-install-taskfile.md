# タスク化したい

タスク管理ツール（`go-task`）と、CMakeのプリセット設定（`CMakePresets.json`）を使って、Geant4のインストール手順を再利用可能な形にしてみました。

Geant4のバージョンを指定すればうまく動くはずです。

## ディレクトリ構成

```console
~/geant4
  |-- Taskfile.yml
  |-- CMakePresets.json
  |-- archives/
  |    |-- geant4.v11.X.Y.tar.gz
  |-- v11.X.Y/
  |    |-- source
  |    |-- build
  |    |-- install
```

## タスクを分割したい

```yaml
# ~/geant4/Taskfile.yml
#
# Usage:
# vi Taskfile.yml  # Edit G4VERSION
# task download
# task configure
# task build
# task install

# Tasks:
# Preparation
# 1. Install Dependencies (once)
# 2. Create Workspaces (once)
#
# Main process
# 1. Download source code from Geant4 repository
# 2. Unzip source code
# 3. Configure
# 4. Build
# 5. Install
#
# Cleanup
# 1. Remove install directory
# 2. Remove build directory
# 3. Remove build and install directory


version: "3"

vars:
  # Edit the version
  G4VERSION: "v11.4.0"
  # Home
  G4HOME: "{{.HOME}}/geant4"
  G4WORK: "{{.G4HOME}}/{{.G4VERSION}}"
  # Download
  G4NAME: "geant4-{{.G4VERSION}}"
  G4ZIP: "{{.G4NAME}}.zip"
  G4URL: "https://gitlab.cern.ch/geant4/geant4/-/archive/{{.G4VERSION}}/{{.G4ZIP}}"
  # configure
  GENERATOR: "Ninja"
  QT_PATH:
    # sh: brew --prefix qt@5  # enable if G4VERSION < v11.4.0
    sh: brew --prefix qt      # enable if G4VERSION >= v11.4.0

env:
  G4SOURCE: "{{.G4WORK}}/source"
  G4BUILD: "{{.G4WORK}}/build"
  G4INSTALL: "{{.G4WORK}}/install"
  QT_PATH: "{{.QT_PATH}}"

tasks:
  deps:
    desc: Install required dependencies via Homebrew
    cmds:
      - brew install wget
      - brew install cmake
      - brew install --cask xquartz
      # - brew install qt@5  # enable if G4VERSION < v11.4.0
      - brew install qt      # enable if G4VERSION >= v11.4.0
      - brew install ninja

  setup:
    desc: Create Geant4 working directory
    status:
      - test -d {{.G4HOME}}/archives
    cmds:
      - mkdir -p {{.G4HOME}}/archives

  fetch:
    desc: Download Geant4 source code
    dir: "{{.G4HOME}}/archives"
    status:
      - test -f {{.G4ZIP}}
    cmds:
      - wget {{.G4URL}}

  unzip:
    desc: Unzip Geant4 source code
    dir: "{{.G4HOME}}"
    status:
      - test -d {{.G4WORK}}/source
    cmds:
      - mkdir -p {{.G4WORK}}
      - unzip ./archives/{{.G4ZIP}}
      - mv -n {{.G4NAME}} {{.G4WORK}}/source

  download:
    desc: Download and unzip Geant4 source code
    cmds:
      - task: fetch
      - task: unzip

  configure:
    desc: Configure with CMake
    dir: "{{.G4WORK}}"
    cmds:
      - cmake -G {{.GENERATOR}} -S source -B build -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH={{.QT_PATH}} -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON

  build:
    desc: Build Geant4 with CMake
    dir: "{{.G4WORK}}"
    cmds:
      - cmake --build build --parallel

  install:
    desc: Install Geant4 with CMake
    dir: "{{.G4WORK}}"
    cmds:
      - cmake --install build

  uninstall:
    desc: Remove installed Geant4 files
    dir: "{{.G4WORK}}"
    cmds:
      - rm -rf ./install

  clean:
    desc: Remove build directory
    dir: "{{.G4WORK}}"
    cmds:
      - rm -rf ./build

  reset:
    desc: Remove build and install directories
    cmds:
      - task: uninstall
      - task: clean

  env:
    desc: Show how to set up the Geant4 environment
    cmds:
      - echo "Run 'source {{.G4INSTALL}}/bin/geant4.sh' to set up Geant4 in your shell"

  main:
    desc: Run configure -> build -> install
    cmds:
      - task: configure
      - task: build
      - task: install

  default:
    desc: Show tasks to run
    cmds:
      - echo "task setup"
      - echo "task download"
      - echo "task configure"
      - echo "task build"
      - echo "task install"
```

## プリセットしたい

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
            "description": "Default build with Qt and OpenGL",
            "generator": "Ninja",
            "cacheVariables": {
                "CMAKE_INSTALL_PREFIX": "${env.G4INSTALL}",
                "CMAKE_PREFIX_PATH": "${env.QT_PATH}",
                "GEANT4_INSTALL_DATA": "ON",
                "GEANT4_USE_OPENGL_X11": "ON",
                "GEANT4_USE_QT": "ON"
            }
        }
    ],
    "buildPresets": [
        {
            "name": "default",
            "configurePreset": "default",
            "description": "Build using default preset",
            "jobs": 8
        }
    ],
    "testPresets": []
}
```

## ビルドしたい

```console
$ task deps
$ task setup
$ task download
```

```console
$ task configure
$ task build
$ task install
```

```console
$ task uninstall
$ task clean
$ task reset
```

```console
$ task tree
$ task env
```
