# KumaROOT

**くまのためのROOT入門 ／ ROOT for Bearginner**

ROOTなどの高エネルギー物理学分野で使っているツールの使い方をまとめているドキュメントです。
もともとは古巣の研究室に設置した[ShotakahaDokuWiki](https://www-he.scphys.kyoto-u.ac.jp/member/shotakaha/dokuwiki/doku.php)（アクセス不可）でまとめていた内容で、
現在は[KumaROOT - Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開&更新しています。

## 「くまROOT」：プロジェクト名の由来？

僕が研究室に入りROOTを使いはじめたときに、先輩から最初に渡されたのが「猿にも使えるROOT」（通称：さるROOT）でした。
そのタイトルを意識して「くま」にしました。
「さるROOT」の次は「くまROOT」を読んでもらえるように頑張りたいと思います。

想定している読者は、ちょっとだけROOTを使ったことがある学生／研究者です。
パッケージやクラスの網羅的な説明は公式ドキュメントに任せ、
ここでは「〇〇したい」という目的ベースで整理することで、
「逆引き辞典」として使えるものを目指したいと思います。

---

## 📖 ユーザー向け

このセクションはドキュメントを**読みたい方**向けです。

### オンラインでドキュメントを読む

以下のプラットフォームでドキュメントが公開されています：

- **[KumaROOT - Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)** （推奨：最新かつもっとも読みやすい）
- [HTML版ダウンロード](https://readthedocs.org/projects/kumaroot/downloads/)
- [PDF版ダウンロード](https://readthedocs.org/projects/kumaroot/downloads/)
- [GitHub Pages](https://shotakaha.github.io/kumaroot/)

Read the Docsは自動的に最新のドキュメントを反映しており、以下の機能が利用できます：
- バージョン選択（複数バージョン対応）
- テーマの切り替え（ダーク/ライトモード）
- 全文検索

### ドキュメントのビルド

プレビュー公開に際して、Read the Docsの[ダッシュボード](https://readthedocs.org/dashboard/)から手動でビルドすることもできます（通常は自動）。

---

## 🛠 開発者・協力者向け

このセクションはドキュメントを**編集・拡張したい方**、**ローカルでビルドしたい方**向けです。

### クイックスタート

```console
$ git clone git@github.com:shotakaha/kumaroot.git
$ cd kumaroot
$ uv sync --all-extras
$ source .venv/bin/activate
$ task docs:serve
```

ブラウザで[http://localhost:8000](http://localhost:8000)を開くと、ライブリロード機能付きでドキュメントをプレビューできます。

### セットアップの詳細

このドキュメントは[Sphinx](https://sphinx-users.jp)というドキュメント作成ソフトを使用しており、
文書本体には``reStructuredText（reST）``と``Markdown（md）``という軽量マークアップ言語を使用しています。

**必要な環境：**
- Git
- Python3.12以上
- `uv`（Pythonパッケージマネージャー）

**セットアップコマンド：**

1. リポジトリをクローン
   ```console
   $ git clone git@github.com:shotakaha/kumaroot.git
   ```

2. 依存パッケージをインストール
   ```console
   $ cd kumaroot
   $ uv sync --all-extras
   $ source .venv/bin/activate
   ```

### コンテンツの作成・編集

#### 新しいコンテンツを追加する流れ

```console
$ git switch main
$ git pull
$ git switch -c feature/add-new-guide  # 新規ブランチを作成
$ code .  # VS Codeを開く
```

1. ``docs/source/ツール名/ツール名-usage.md``にコンテンツの説明を追加
2. ``docs/source/ツール名/ツール名-<feature>.md``を新規作成
3. ``ツール名-usage.md``の``toctree``にファイル名を登録
4. 変更をコミット
   ```console
   $ git add .
   $ git commit
   ```
5. GitHubにプッシュしてプルリクエスト（PR）を作成
6. 自動テストがパスしたらマージ

#### ファイルの命名規則

コンテンツのファイル名は以下の規則に従います：

```text
docs/source/<category>/<category>-<content>.md
```

**例：**

- **インデックス（主要）**：`root/root-usage.md`, `python/python-usage.md`
- **インストール方法**：`root/root-install.md`, `python/python-install.md`
- **機能・使い方**：`root/root-th1-fill.md`, `python/python-pathlib.md`
- **画像・スクリーンショット**：`emacs/fig/mac-key01.png`, `git/fig/git-status.png`

### ドキュメントのプレビュー

#### ライブリロード付きプレビュー（推奨）

```bash
task docs:serve
```

自動的にdocsディレクトリに移動し、ライブリロード機能でドキュメントをプレビュー開始します。
http://localhost:8000 でアクセスできます。

#### VS Codeで開きながらプレビュー

```bash
task code
```

VS Code内でターミナルを開き（`command + j`）、`task docs:serve`を実行すればプレビューが開始されます。

#### ビルドコマンド

```bash
task docs:serve      # ライブリロード付きプレビュー
task docs:build      # 静的HTMLをビルド（docs/build/html/）
task docs:pdf        # PDFファイルをビルド（docs/build/latex/）
```

### バージョン管理

#### バージョン番号スキーム

バージョン番号は**YYYY.MM.PATCH**形式のカレンダーバージョニングを採用しています：

- `Major (YYYY)` : 年が変わった時に変更（例：2025.x.x → 2026.x.x）
- `Minor (MM)` : 月が変わった時に変更（例：2026.3.x → 2026.4.x）
- `Patch` : 各コミット（`feat`または`fix`）ごとに自動更新

**現在のバージョン：2026.4.0 (2026年4月)**

#### バージョンバンプのタイミング

```bash
$ task bump:check    # プレビュー（変更なし）
$ task bump:patch    # パッチをバンプ（毎回のコミット後）
$ task bump:minor    # マイナーをバンプ（月初めに1度）
$ task bump:major    # メジャーをバンプ（年初めに1度）
```

**使用頻度と説明：**

- **`task bump:patch`**（頻繁）：`fix`または`feat`コミット後に実行
  - パッチバージョンを自動更新、`CHANGELOG.md`も自動生成

- **`task bump:minor`**（月1回）：月が変わった際に実行
  - 例：2026年3月から4月への移行時に実行

- **`task bump:major`**（年1回）：年が変わった際に実行
  - 例：2026年から2027年への移行時に実行

### 品質管理

#### Pre-commitフック

Pre-commitフックをセットアップすることで、コミット前に自動的にコードをチェックできます：

```bash
$ task pre-commit:setup    # フックをインストール
$ task pre-commit          # 全ファイルをチェック
$ task pre-commit:update   # フックを最新に更新
```

Pre-commitフックは以下の検査を実行します：
- Commitizen：コミットメッセージの形式チェック
- Ruff：Pythonコードの形式チェック
- JSON/TOML/YAML/XML の妥当性チェック
- 末尾の空白・マージコンフリクト の検出

#### 依存パッケージの管理

```bash
$ task deps:setup      # Python環境をセットアップ
$ task deps:check      # 更新可能なパッケージを確認
$ task deps:update     # パッケージを更新（uv.lockも更新）
```

パッケージを更新した場合は、`uv.lock`をGitにコミットしてください。

### その他の有用なタスク

```bash
$ task version   # 現在のバージョンを表示
$ task status    # Gitの状態を表示
$ task log       # 最近のコミットを表示（10件）
$ task push      # mainブランチをプッシュ
```

### コンテンツの標準化と規則

詳しい執筆ガイドラインと技術仕様については、[CLAUDE.md](CLAUDE.md)を参照してください。
そこには以下の内容が記載されています：

- **ドキュメント構造**：`逆引き形式`（目的ベースの整理）の説明
- **日本語スタイル**：JTF（Japan Typesetting Foundation）style guide への準拠
- **Sphinx設定**：MyST Parser、タグシステム、etc.
- **REST/Markdown 記法**：コード例、数式、アドモニション（注釈）の書き方
- **ROOT技術リファレンス**：C++/Pythonサンプル、メソッドシグネチャの記載方法

---

## 📝 ライセンス

MIT License

## 📧 お問い合わせ

質問やフィードバックは[GitHub Issues](https://github.com/shotakaha/kumaroot/issues)でお願いします。
