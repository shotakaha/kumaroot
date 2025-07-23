# タスクランナーしたい（`task`）

```cpp
$ task タスク名
```

`Task`は **タスクランナー** と呼ばれるコマンド実行を自動化するツールです。
GNU Makeと同じような役割ですが、
YAML形式の設定ファイル（`Taskfile.yml`）により、
簡潔かつ柔軟にタスクを記述できます。

## インストールしたい（`go-task`）

```console
$ brew install go-task

// 初期化
$ task --init
Taskfile created: Taskfile.yml

// デフォルトのタスクを実行
$ task
Hello, World!
```

Homebrewで`go-task`フォーミュラをインストールします。
任意のディレクトリで`task --init`を実行して、`Taskfile.yml`のひな形を生成します。
ひな型はデフォルトで「Hello, World」を表示するようになっているので、
そのまま`task`コマンドを実行して動作確認できます。

:::{note}

TODO管理用のCLIツールにも同じ名前（`task`）のものがあります。
`task`フォーミュラというフォームラは

:::

## 設定ファイルしたい（`Taskfile.yml`）

```yaml
# https://taskfile.dev

version: '3'

vars:
  GREETING: Hello, World!

tasks:
  default:
    cmds:
      - echo "{{.GREETING}}"
    silent: true
```

タスクの設定は`Taskfile.yml`に記述します。
`Taskfile.yml`は **プロジェクトルート** に配置します。
まず`task --init`でひな形を生成し、編集する方法がオススメです。

`vars`セクションで変数を定義できます。
`tasks`セクションに、タスク名とその実行内容を定義します。

## タスクしたい（`tasks` / `cmds` / `desc`）

```yaml
tasks:
  <タスク名>:
    desc: タスクの説明（オプション）
    cmds:
      - 実行コマンド1
      - 実行コマンド2

  configure:
    desc: Configure with CMake
    cmds:
      - cmake -S source -B build

  build:
    desc: Build with CMake
    cmds:
      - cmake --build build --parallel
```

`tasks`セクションでは、1つ以上のタスクを定義できます。
それぞれのタスクには、`タスク名`と`cmds`が必須です。
`cmds`はリスト形式で複数のコマンドを順番に指定できます。
`desc`で簡単な説明をつけるとよいです。

## ディレクトリを指定したい（`dir`）

```yaml
tasks:
  html:
    desc: Hot-reload Sphinx docs
    dir: docs
    cmds:
      - poetry run make livehtml
```

`dir`オプションを使うと、指定したディレクトリ内でコマンドを実行できます。
パスは、プロジェクトルートからの相対パスを指定できます。
ディレクトリが存在しない場合はエラーになります。

## 条件分岐したい（`status` / `preconditions`）

```yaml
tasks:
  download:
    desc: Download file (skip if already downloaded)
    status:
      - test -f archives/archived.zip
    cmd:
      - wget https://example.com/download.zip
      - mv download.zip archives/archived.zip
```

`status`オプションを使うと、条件を満たしている場合にタスクの実行をスキップできます。
通常は`test`コマンドを使って、ファイル（やディレクトリ）の存在を確認します。
上記のサンプルでは、`archives/archived.zip`が存在する場合、ダウンロードをスキップします。

```yaml
tasks:
  clean:
    desc: Remove build files
    preconditions:
      - sh: test -d build
        msg: "[Error] Build directory does not exist"
    cmds:
      - rm -rf build
```

`preconditions`を使うと、タスクを実行する前に必要は条件をチェックできます。
条件が満たされない場合は、タスクは中断され、指定した`msg`が表示されます。
上記のサンプルでは`build`ディレクトリが存在しない場合に
エラーメッセージが表示されます。

## 変数したい（`vars`）

```yaml
vars:
  G4VERSION: "v11.3.2"
  G4HOME: "{{.HOME}}/geant4"
  QT_PATH:
    sh: brew --prefix qt@5

tasks:
  setup:
    cmds:
      - echo "Installing Geant4 {{.G4VERSION}} to {{.G4HOME}}"
      - echo "Qt is located at {{.QT_PATH}}"
```

`vars`セクションでタスク全体で利用するグローバル変数を定義できます。
`{{.変数名}}`の形式で、Goテンプレート構文による変数展開ができます。
`sh`オプションを使うと、シェルコマンドの出力を変数として使用できます。

```console
$ task setup G4VERSION=v11.2.1
```

`vars`で定義した変数は、`task`コマンドの引数として上書きできます。

## サンプルしたい

実際に設定してみて、便利だと思ったタスクを紹介します。

### Sphinxでライブビューしたい（`task livehtml`）

```yaml
tasks:
  livehtml:
    desc: Start Sphinx livehtml
    dir: docs
    cmds:
      - poetry run make livehtml
```

`sphinx-autobuild`を使ってSphinxドキュメントをライブプレビューする設定です。

通常は、ドキュメントのあるディレクトリ（`docs`）に移動してから`make livehtml`コマンドを実行する必要があります。
このタスクを設定すると、どのディレクトリからでも`task livehtml`で確認できるようになります。

### Poetryで更新したい（`task update`）

```yaml
tasks:
  export:
    desc: Export requirements.txt
    cmds:
      - poetry export --output requirements.txt

  update:
    desc: Update dependencies
    cmds:
      - poetry update
      - task: export
```

Pythonパッケージを更新する設定です。
最近は`pyproject.toml`で依存関係を管理するのが主流ですが、`requirements.txt`が必要な場合もまだまだあります（例：Read the Docs）。
このタスクを設定すると、パッケージ更新と`requirements.txt`生成を一括で実行できるようになります。

### VS Codeしたい（`task code`）

```yaml
tasks:
  code:
    desc: Start VS Code
    cmds:
      - code .
```

プロジェクトルートでVS Codeを開く設定です。
`code .`をサブディレクトリで実行すると、親ディレクトリの構造にアクセスできません。
このタスクの設定すると、プロジェクト内のどこからでも、常にプロジェクトルートで開くことができます。
地味な設定ですが、かなり便利だと思っています。
