# Claudeしたい（`claude-code`）

```console
$ claude [options] [command] [prompt]
$ claude                   # セッションを開始
$ claude --continue        # 最近のセッションを再開
$ claude --resume <id>     # セッションIDを指定して再開
$ claude --print           # 結果をターミナルに表示して終了（パイプ利用）
$ claude config list       # 設定を確認
```

`claude`コマンドで、Claudeのセッションを開始できます。
セッションの内容は`~/.claude/`の中に保存されるようで、
`--resume`オプションで、過去のセッションから再開することもできます。

## インストールしたい（`claude-code`）

```console
$ brew install --cask claude-code
$ claude --version
1.0.98 (Claude Code)

// 自動更新をOFFにする
$ claude config set -g autoUpdates false
$ claude config get -g autoUpdates

// 手動で更新する
$ brew upgrade --cask claude-code
```

Homebrewで`claude-code`をインストールできます。
Homebrewで管理する場合は、Claudeの自動更新はOFFにして、手動で更新するほうがよいそうです。

:::{note}

`claude`はデスクトップアプリ用、
`claude-code`はCLI用のcaskのようです。

:::

## ターミナル入力で改行したい（`/terminal-setup`）

```console
> /terminal-setup
  ⎿  Configured Terminal.app settings:
     - Enabled "Use Option as Meta key"
     - Switched to visual bell
     Option+Enter will now enter a newline.
     You must restart Terminal.app for changes to take effect. dark-ansi
```

`/terminal-setup`でClaudeセッション内で
改行（`Option+Enter`）できるようになります。

## リポジトリの初期設定したい（`/init`）

```console
> /init
```

`/init`で、プロジェクト内のファイルを確認し、適切な`CLAUDE.md`を生成します。
既存のリポジトリで、すぐにClaudeによるサポート体制を組むことできます。

:::{note}

ある程度、形が整っているリポジトリだと非常にうまく移行できます。
まだ、整っていない場合でも `README.md` に、やりたいことなどを書きだしておくと、
それらを読み込み、より目的に近づいた設定ファイルを生成してくれます。

:::

## vimモードしたい（`/vim`）

```console
> /vim
```

`/vim`で、Claudeセッションをnormalモードとvimモードに変更できます。
vimモードにすると、vimエディターのようにモーダル（`NORMAL/INSERT`）切り替えが有効になります。

## 権限管理したい（`/permissions`）

```console
> /permissions
╭───────────────────────────────────────────────────────────────────────╮
│ Permissions:  Allow   Ask   Deny   Workspace                          │
│                                                                       │
│ Claude Code won't ask before using allowed tools.                     │
│                                                                       │
│ ❯ 1. Add a new rule…                                                  │
│                                                                       │
╰───────────────────────────────────────────────────────────────────────╯
   Tab to select tab · Enter to confirm · Esc to cancel
```

セッション内で`/permissions`コマンドを実行すると、Claudeの権限を設定できます。
`Allow`、`Ask`、`Deny`、`Workspace`をTABもしくは矢印キーで選択し、
表示されたダイアログにしたがって、操作対象を入力して設定します。

設定した内容は
プロジェクトのローカル設定（`.claude/settings.local.json`）、
プロジェクト設定（`.claude/settings.json`）、
ユーザー設定（`~/.claude/settings.json`）のいずれかに保存できます。

:::{note}

`.claude/settings.json`は、開発チーム全体で共有したいプロジェクト設定を記述するファイルです。
一方、`.claude/settings.local.json`は、チームには共有しない個人用設定です。

:::

## サブエージェントしたい（`/agents`）

```console
> /agents
╭───────────────────────────────────────────────────────────────────────╮
│ Agents                                                                │
│ No agents found                                                       │
│                                                                       │
│ ❯ Create new agent                                                    │
│                                                                       │
│ No agents found. Create specialized subagents that Claude can         │
│ delegate to.                                                          │
│ Each subagent has its own context window, custom system prompt, and   │
│ specific tools.                                                       │
│ Try creating: Code Reviewer, Code Simplifier, Security Reviewer, Tech │
│  Lead, or UX Reviewer.                                                │
│                                                                       │
│                                                                       │
│   Built-in (always available):                                        │
│   general-purpose · sonnet                                            │
│   statusline-setup · sonnet                                           │
│   output-style-setup · sonnet                                         │
│                                                                       │
╰───────────────────────────────────────────────────────────────────────╯
   Press ↑↓ to navigate · Enter to select · Esc to go back
```

`/agents`コマンドで、サブエージェントを追加できます。

サブエージェントの設定は
プロジェクト設定（`.claude/agents/`）、
ユーザー設定（`~/.claude/agents/`）のいずれかの中に保存できます。

ビルトインのサブエージェントとして、
`general-purpose`、
`statusline-setup`、
`output-stype-setup`が用意されているようです。

新規サブエージェントもダイアログにしたがって進めると、Claude自身が生成してくれます。
生成された内容をカスタマイズするのが推奨されています。

## フックしたい（`/hooks`）

```console
> /hooks
╭───────────────────────────────────────────────────────────────────────╮
│ Hook Configuration                                                    │
│                                                                       │
│ Hooks are shell commands you can register to run during Claude Code   │
│ processing. Docs                                                      │
│                                                                       │
│ Select hook event:                                                    │
│ ❯ 1. PreToolUse - Before tool execution                               │
│   2. PostToolUse - After tool execution                               │
│   3. Notification - When notifications are sent                       │
│   4. UserPromptSubmit - When the user submits a prompt                │
│ ↓ 5. SessionStart - When a new session is started                     │
╰───────────────────────────────────────────────────────────────────────╯
   Enter to acknowledge risks and continue · Esc to exit
```

`/hooks`コマンドで、Claudeの処理に合わせたフックを設定できます。
`PreToolUse`、
`PostToolUse`、
`UserPromptSubmit`,
`Notification`、
`Stop`、
`SubagentStop`、
`PreCompact`、
`SessionStart`,
`SessionEnd`に対してフックを設定できます。

## 設定したい（`.claude/settings.json`）

```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(uv:*)",
      "Bash(task:*)",
      "Bash(pytest:*)",
      "Bash(ruff:*)",
      "Bash(mkdocs:*)",
      "Bash(glab:*)",
      "Read",
      "Glob",
      "Grep",
      "LS",
      "Task",
      "TodoWrite"
    ],
    "ask": [
      "Edit",
      "Write",
      "MultiEdit",
      "Bash(git commit:*)"
    ]
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./**/.env)",
      "Read(./**/.env.*)",
      "Read(./secrets/**)",
      "Bash(rm -rf:*)",
      "Bash(git push -f:*)",
      "Bash(git push --force:*)",
      "Bash(sudo:*)",
      "Bash(curl:*)"
    ],
    "defaultMode": "default",
    "additionalDirectories": [
      "./docs/",
      "./examples/"
    ]
  },
  "env": {
    "PYTHONPATH": "src"
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "task lint 2>/dev/null || true"
          }
        ]
      }
    ]
  },
  "includeCoAuthoredBy": false
}
```

Claudeの設定は
`~/.claude/settings.json`もしくは、
プロジェクトごとの`(project_root)/.claude/settings.json`で変更できます。

## 権限を管理したい（`permissions`）

```json
{
  "permissions": {
    "allow": ["..."],
    "deny": ["..."],
    "defaultMode": "...",
    "additionalDirectories": ["..."],
    "disableBypassPermissionsMode": "..."
  }
}
```

`permissions`キーでClaudeが操作できる権限を設定できます。
サブキーとして
`allow`、
`ask`、
`deny`、
`additionalDirectories`、
`defaultMode`、
`disableBypassPermissionsMode`を設定できます。

### 許可したい（`permissions.allow`）

```json
"allow": [
  "Bash",                    // 全てのBashコマンド
  "Bash(git:*)",            // git関連コマンドのみ
  "Read",                   // ファイル読み取り
  "Glob",                   // パターン検索
  "Grep",                   // 文字列検索
  "LS",                     // ディレクトリ一覧
  "Task",                   // タスク実行
  "WebSearch",              // Web検索
  "TodoWrite"               // TODO作成
]
```

`allow`キーにはClaudeによる使用を許可する操作をリスト形式で指定します。
`Bash`はすべてのbashコマンドを許可してしまうので、
`ask`キーや`deny`キーを適切に設定するか、
`Bash(git:*)`のようにコマンド名を限定するようにします。

:::{note}

`Bash(uv:*)`、`Bash(glab:*)`、`Bash(task:*)`のように、
プロジェクトごとに利用するコマンドを追加します。

:::

### 確認したい（`permissions.ask`）

```json
"ask": [
  "Edit",                   // ファイル編集
  "Write",                  // ファイル作成
  "MultiEdit",              // 複数ファイル編集
  "WebFetch",               // Web取得
]
```

`ask`キーには、Claudeによる使用に確認を求める操作をリスト形式で指定します。
`Edit`、`Write`、`MultiEdit`のようなファイルを編集する操作を追加しました
`WebFetch`も、意図しないサイトに勝手にアクセスしないように追加しています。

### 拒否したい（`permissions.deny`）

```json
"deny": [
  "Bash(curl:*)",           // curl系コマンド拒否
  "Bash(rm -rf:*)",         // 危険な削除コマンド拒否
  "Bash(git push -f:*)",         // 危険な削除コマンド拒否
  "Bash(git push --force:*)",         // 危険な削除コマンド拒否
  "Read(./.env)",           // ルートの環境変数ファイル読み取り拒否
  "Read(./.env.*)",         // ルートの環境変数系ファイル拒否
  "Read(./**/.env)",        // サブディレクトリの環境変数ファイル読み取り拒否
  "Read(./**/.env.*)",      // サブディレクトリの環境変数系ファイル拒否
  "Read(./secrets/**)",     // secretsディレクトリ拒否
  "Read(./config/credentials.json)", // 認証情報拒否
  "WebFetch"                // Web機能全体拒否
]
```

`deny`キーには、Claudeによる使用を拒否する操作をリスト形式で指定します。
`rm -rf`や`git push --force`のようにClaudeに実行されると困るコマンドを追加します。
また、`.env`にパスワードやAPIトークンなどの機密情報が含まれる場合は、Readできないようにしておきます。

:::{note}

Readできないようにすると、EditもWriteもできなくなります。

:::

### 初回モード（`permissions.defaultMode`）

```json
"defaultMode": "default"     // 標準モード（初回確認）
"defaultMode": "acceptEdits" // 編集自動承認
"defaultMode": "plan"        // 読み取り専用モード
```

`defaultMode`キーでClaudeを起動した時の権限モードを指定できます。
デフォルト値は`acceptEdits`になっているので、`default`を設定しておくとよいと思います。
読み取り専用で動作させたいプロジェクトでは`plan`にします。

### 追加ディレクトリ（`permissions.additionalDirectories`）

```json
"additionalDirectories": [
  "./docs/",               // ドキュメントディレクトリ
  "~/shared/libraries/",   // 共有ライブラリ
  "/usr/local/bin/"        // システムディレクトリ
]
```

`additionalDirectories`キーで、Claudeがアクセスできる場所を追加できます。
プロジェクトルートからの相対パス、もしくは絶対パスで指定します。

### バイパスモード（`permissions.disableBypassPermissionsMode`）

```json
"disableBypassPermissionsMode": "disable" // バイパスモード無効化
```

`disableBypassPermissionsMode`キーでバイパスモードを変更できます。
デフォルト値の`disable`のままにしておくのがよいです。


## フックしたい（`hooks`）

```json
{
    "hooks": {
        "PreToolUse": [...],    // ツール呼び出し前に実行
        "PostToolUse": [...],   // ツール呼び出し後に実行
        "UserPromptSubmit": [...],    // プロンプト送信後に実行（Claudeの処理前）
        "Notification": [...],    // Claudeの通知送信時に実行
        "Stop": [...],    // 応答終了時に実行
        "SubagentStop": [...],    // サブエージェントのタスク完了時に実行
        "PreCompact": [...],    // コンパクト操作する前に実行
        "SessionStart": [...],    // セッションを開始／再開するときに実行
        "SessionEnd": [...],    // セッション終了するときに実行
    }
}
```
