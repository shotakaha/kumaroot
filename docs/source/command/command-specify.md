# スペック駆動開発したい（`specify`）

```console
$ specify init --here

$ ls .specify
```

`specify`は「スペック駆動開発」をサポートするためのツールです。
GitHubが開発したツールで、リポジトリ名は`spec-kit`となっています。

**スペック駆動開発**とは、仕様書（スペック）と要件定義を基準にコード実装を進める開発スタイルです。
`specify`（`spec-kit`）は、AIエージェントを活用して、仕様書と実装を橋渡しする役割を担います。
専用コマンドを使うことで、仕様から外れた実装を防ぎ、正しい開発を進めやすくやります。

:::{note}

「バグは夜更けすぎに、仕様へと変わるだろう」

ふつうの開発でも、コードを書き始める前には「こういった機能が欲しい」という仕様書を作成します。
しかし、実際にはコードを書きながら仕様が変わってしまったり、
実装されたコードがそのまま「正しい仕様」とみなされてしまうことがよく起こります。

このようなことを繰り返すと「技術負債」が増えていき、最終的に自分たちを苦しめることになります。

:::

## 導入したい（`specify init`）

```console
// 新規導入
$ specify init プロジェクト名

// 既存のプロジェクトに導入
$ specify init --here

// Choose your AI assistant
// Choose script type
```

`specify init`でスペック駆動開発を導入したプロジェクトを作成できます。
既存のプロジェクトに追加したい場合は、プロジェクトルートで`specify init --here`を実行してください。

```console
// 初期化した直後
$ ls -1a
.claude/    // 選択したAIエージェント名
.git/
.specify/
```

初期化した直後のディレクトリ構造です。
プロジェクトは自動でGitリポジトリとなり、
選択したエージェントと`specify`用の設定ディレクトリが追加されました。

```console
tree .specify/ .claude
.specify/
├── memory
│   └── constitution.md
├── scripts
│   └── bash
│       ├── check-prerequisites.sh
│       ├── common.sh
│       ├── create-new-feature.sh
│       ├── setup-plan.sh
│       └── update-agent-context.sh
└── templates
    ├── agent-file-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
.claude
└── commands
    ├── analyze.md
    ├── clarify.md
    ├── constitution.md
    ├── implement.md
    ├── plan.md
    ├── specify.md
    └── tasks.md
```

`.specify`と`.claude`の構造です。
スペック駆動開発をサポートするシェルスクリプトと、
AIエージェント専用のコマンドが導入されています。

:::{note}

2025年10月ころのとあるバージョンのSpecKitから、
AIエージェント専用のコマンドの先頭に
`speckit.`の名前空間が付与されるようになりました。

:::

## 憲法したい（`/speckit.constitution`）

```console
> /speckit.constitution
```

`/speckit.constitution`で、プロジェクトの「憲法（constitution）」を定義できます。
開発時に絶対に守るべき原則や制約をAIエージェントに明示する重要なステップで、初回に一度だけ実行するのが基本です。

生成された内容は`.specify/memory/constitution.md`に保存されます。
このファイルを直接編集したり、
AIエージェントと相談しながら更新したりしてもOKです。

:::{note}

仕様や実装の前提となる「不変のルール」を定めることが重要です。
プロジェクトの目的や対象ユーザー、開発フロー、セキュリティ対策などを記述します。

```console
> /speckit.constitution
 Beginner-friendly project
 Educational docstrings
 Spec-Driven development
 Test-Driven development
 Skeleton-src-tests development
 src-tests symmetric patterns
 DRY, SRP, and YAGNI principles
 Semantic versioning
```

実装の詳細（使用する言語や依存パッケージなど）は、ここには記述せず、
`README.md`や、エージェントごとの設定（`CLAUDE.md`、`GEMINI.md`、`AGENTS.md`など）に記述します。

:::

## 仕様したい（`/speckit.specify`）

```console
$ claude    // AIエージェントを起動する
```

`specify`で導入したコマンドはすべてAIエージェントのスラッシュコマンドとして実行します。
今回は`Claude (Claude Code)`を前提としますが、他のエージェントでも同じです。

```console
> /specify 欲しい機能について説明する
```

`/specify`コマンドで、`spec.md`を作成します。
生成されたファイルの内容を確認し、この仕様でよいかを判断します。
修正が必要な場合は、追加で指示して修正してもらえばOKです。

:::{hint}

スペック駆動開発をはじめるためには、仕様を明確にする必要があります。
何度も推敲して`spec.md`をきちんと練ることで、
このあとの開発がスムーズになります。

ちなみに`/specify`に渡す説明も、
AIエージェントに相談して作成するとよいです。

:::

:::{note}

完璧だと思った仕様も、実装してみたら不完全だったことはよくあります。
そのことに途中で気づいてしまった場合でも、
とりあえず、そのまま完遂させましょう。

`spec.md`を途中で修正してやり直すより、
修正した内容で新しく`spec.md`を作成して取り組むほうが簡単だと思います。

:::

## 明確にしたい（`/speckit.clarify`）

```console
> /clarify
```

`/clarify`で、生成された`spec.md`に不明瞭な点がないか確認できます。
`specify v2`で追加されました。

不明瞭な点がある場合は、どの意図と、解決オプションが提示されます。
内容を確認し、今回の使用にあったオプションを選択すればOKです。
オプションにない場合は、ここで相談すればOKです。

## 計画したい（`/speckit.plan`）

```console
// 通常開発
> /plan as simple as possible. readability counts. describe to beginners.

// 積極開発
> /plan as simple as possible. readability counts. breaking changes accepted. describe to beginners.
```

`/plan`コマンドで、実装計画を生成します。
このコマンドは引数に指示を追加できます。
`Claude`の場合、そのままだと小難しく実装しがちなので、上記の指示をおまじないのように書いています。

:::{note}

Claudeは、エラーハンドリングなどを細かいところまで実装してくれる印象です。
なので、`keep it simple`と指示しないと、僕自身が理解できなくなってしまいます。

:::

## タスク化したい（`/speckit.tasks`）

```consol
> /tasks simplify tasks as much as possible. readability counts. describe to beginners.
```

`/tasks`コマンドで、`plan.md`にしたがってタスクを分割します。
このコマンドの引数にも指示を追加できるので、ここでも`keep it simple`と伝えておきます。
このおなじないで、タスク数が半減（20以上 -> 10以下）したことがあるので、使い続けています。

## 実装したい（`/speckit.implement`）

```console
> /implement as simple as possible. readability counts. describe to beginners.
```

`/implement`コマンドで、`tasks.md`に分割されたタスクにしたがって実装を開始します。
`specify v2`で追加されました。

:::{note}

`v1`ではタスク番号（やフェーズ）を指定して、段階的に進める必要がありましたが、
`v2`からは一括実装できるようになりました。

:::

## リファレンス

- [speck-kit - GitHub](https://github.com/github/spec-kit)
