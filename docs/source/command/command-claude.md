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

$ brew upgrade --cask claude-code
```

Homebrewで`claude-code`をインストールします。

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
      "Edit",
      "Write",
      "Read",
      "MultiEdit",
      "Glob",
      "Grep",
      "LS",
      "Task",
      "TodoWrite"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./**/.env)",
      "Read(./**/.env.*)",
      "Read(./secrets/**)",
      "Bash(rm -rf:*)",
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

### 操作権限を管理したい（`permissions`）

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

```json
"allow": [
  "Bash",                    // 全てのBashコマンド
  "Bash(git:*)",            // git関連コマンドのみ
  "Edit",                   // ファイル編集
  "Write",                  // ファイル作成
  "Read",                   // ファイル読み取り
  "MultiEdit",              // 複数ファイル編集
  "Glob",                   // パターン検索
  "Grep",                   // 文字列検索
  "LS",                     // ディレクトリ一覧
  "Task",                   // タスク実行
  "WebFetch",               // Web取得
  "WebSearch",              // Web検索
  "TodoWrite"               // TODO作成
]
```

`allow`セクションには許可する操作をリスト形式で指定できます。
`Bash`はすべてのbashコマンドを許可してしまうので、
`Bash(git:*)`のようにコマンドを限定するほうがよいです。

:::{note}

`Bash(uv:*)`、`Bash(glab:*)`、`Bash(task:*)`のように、
プロジェクトごとに利用するコマンドを追加します。

:::

```json
"deny": [
  "Bash(curl:*)",           // curl系コマンド拒否
  "Bash(rm -rf:*)",         // 危険な削除コマンド拒否
  "Read(./.env)",           // ルートの環境変数ファイル読み取り拒否
  "Read(./.env.*)",         // ルートの環境変数系ファイル拒否
  "Read(./**/.env)",        // サブディレクトリの環境変数ファイル読み取り拒否
  "Read(./**/.env.*)",      // サブディレクトリの環境変数系ファイル拒否
  "Read(./secrets/**)",     // secretsディレクトリ拒否
  "Read(./config/credentials.json)", // 認証情報拒否
  "WebFetch"                // Web機能全体拒否
]
```

`deny`には拒否する操作をリスト形式で設定できます。
`.env`に機密情報が含まれる場合はRead権限を付与しないようにします。
また、`rm -rf`のように危険なコマンドも実行できないようにしておくと安心です。

```json
"defaultMode": "default"     // 標準モード（初回確認）
"defaultMode": "acceptEdits" // 編集自動承認
"defaultMode": "plan"        // 読み取り専用モード
```

`defaultMode`セクションでClaudeの確認頻度を変更できます。
`default`にしておけばよいです。

```json
"additionalDirectories": [
  "./docs/",               // ドキュメントディレクトリ
  "~/shared/libraries/",   // 共有ライブラリ
  "/usr/local/bin/"        // システムディレクトリ
]
```

`additionalDirectories`セクションで、参照するディレクトリを追加できます。
プロジェクトルートからの相対パス、もしくは絶対パスで指定します。

```json
"disableBypassPermissionsMode": "disable" // バイパスモード無効化
```

`disableBypassPermissionsMode`セクションでバイパスモードを変更できます。
デフォルト値の`disable`にしておくのがよいです。
