# KumaROOT プロジェクトレビュー

**レビュー日**: 2026年5月30日  
**対象**: ドキュメント設計、サンプルコード配置、コード管理設計

---

## 1. プロジェクト概要と現状

### プロジェクト特性

**KumaROOT** は高エネルギー物理学向けドキュメント・プロジェクトです。

- **規模**: 88,725行（88.7kloc）、1236ファイル
- **ドキュメント構成**: 49カテゴリ×複数ガイド
- **コンテンツ**: Markdown/reStructuredText混在、コード例、54個の画像資産
- **ビルドツール**: Sphinx + MyST Parser
- **公開先**: Read the Docs（自動ビルド）

### 強み

✅ **明確な設計哲学**
- 「逆引き形式」（目的ベース「〇〇したい」）の一貫性
- 日本語スタイル規約（JTF準拠）を CLAUDE.md に体系化
- 初学者向けとしての道筋が明確

✅ **堅牢な開発環境**
- Conventional Commits + Commitizen による統制
- カレンダーベース版番号管理（YYYY.MM.PATCH）
- Pre-commit フック（Ruff, JSON/YAML検証）
- `uv` による依存管理の統一

✅ **スケーラブルな構成**
- カテゴリごとのディレクトリ分離
- toctree による階層的な導線設計
- Sphinx タグ機能による横断的な整理

---

## 2. ドキュメント中心設計の分析

### 2.1 設計パターン

#### A. **技術リファレンス型** (ROOT, matplotlib など)

**構造**:
```
root-<method>.md
├── C++ コード例（`#include` 付き）
├── Python コード例
├── 概念説明（メソッドシグネチャ）
├── 実装例（「〇〇したい」の複数パターン）
└── 関連メソッド + 公式ドキュメント
```

**例**: `root-th1-fill.md`
- 単一の値を入力したい
- 重みを追加したい
- など3〜5個のユースケース

**特徴**：
- ✅ コード例が冒頭（「お絵かきソフト」のアナロジー）
- ✅ 複数言語サポート（C++/Python）
- ⚠️ 長いドキュメントになりやすい（実装サンプルが多い）

#### B. **実践例型** (Docker など)

**構造**:
```
docker-example-<service>.md
├── docker-compose.yaml（最初に提示）
├── 基本的な使い方
├── 複数のユースケース（「パッケージをインストール」など）
├── バージョン情報テーブル
├── 特徴表（メリット/デメリット/最適用途）
└── 参考資料
```

**例**: `docker-example-ubuntu.md`
- パッケージをインストールしたい
- 開発環境として使いたい
- テスト環境として使いたい

**特徴**：
- ✅ 実行可能な YAML/Dockerfile が `docs/source/docker/examples/` に物理配置
- ✅ コンテナの多様な用途を網羅
- ⚠️ 実ファイルとドキュメントテキストが重複している

#### C. **索引型** (root-usage.md など)

**構造**:
```
<category>-usage.md
├── 概要説明
└── toctree（複数の詳細ガイドへのリンク）
```

**特徴**：
- ✅ ハブ＆スポーク構造で拡張性が高い
- ✅ 新しいガイド追加が容易

---

## 3. サンプルコード配置の改善と実装 ✅

### 3.1 コード管理場所の再構成（完了）

**Before（分散）:**
```
kumaroot/
├── docs/source/
│   ├── root/root-*.md          ← C++/Python コード例（埋め込み）
│   ├── docker/examples/        ← 実ファイル（docker-compose.yaml など）
│   │   ├── docker-ubuntu/compose.yaml
│   │   ├── docker-mariadb/
│   │   └── docker-wordpress-mariadb/
│   ├── emacs/fig/              ← スクリーンショット
│   └── ...
├── scripts/                    ← jupytext形式（py:light）
├── mystmd/                     ← MyST Markdown形式（md:myst）
└── notebooks/                  ← （未使用）
```

**After（統一）:**
```
kumaroot/
├── docs/
│   ├── source/
│   │   ├── docker/
│   │   │   └── docker-example-*.md ← 統一テンプレート（参照のみ）
│   │   ├── root/
│   │   │   └── root-*.md
│   │   └── ...
│   └── examples/                    ← 全コード例を統合 ✅
│       ├── docker/
│       │   ├── ubuntu.yaml
│       │   ├── nginx.yaml
│       │   ├── mariadb.yaml
│       │   └── ... (15個)
│       ├── root/                    （準備済み、段階展開予定）
│       └── python/                  （準備済み）
│
├── scripts/                         （削除予定）
├── mystmd/                          （独立継続）
└── notebooks/                       （未使用）
```

### 3.2 改善実装（完了） ✅

**Docker Example ドキュメントのリファクター完了:**

| 改善項目 | 実装内容 | 効果 |
| --- | --- | --- |
| **統一テンプレート** | 13ファイル全て標準化（25～35行） | 読者の認知コスト低下、メンテ性向上 |
| **YAML 一元化** | `docs/examples/docker/` に 15個を集約 | Single Source of Truth 実現 |
| **literalinclude 化** | 全ドキュメントで `../../examples/docker/*.yaml` 参照 | ドキュメント↔ファイルの同期自動化 |
| **テンプレート構造** | 起動→操作→終了→説明 | 初学者がすぐに試せる設計 |

**移行による削減:**
- ファイルサイズ: 平均 215行 → 32行（85%削減）
- docker/examples/ サブディレクトリ: 削除完了
- hugo, mystmd: toctree から除外

### 3.3 現在のメンテナンスフロー（改善後）

改善後のワークフロー：

```
YAML ファイル変更（docs/examples/docker/*.yaml）
  ↓
ドキュメントは自動的に最新内容を表示
  ↓
Pre-commit フック（YAML検証）チェック
  ↓
コミット
```

**改善点**:
- ✅ YAML ファイルが唯一の情報源（DRY原則）
- ✅ literalinclude で自動同期
- ✅ ドキュメント内の手動修正が不要
- ✅ 構文チェックが自動実行される

---

## 4. サンプルコード管理設計の改善（Docker Example 実装完了）

### 実装済みアーキテクチャ

### 実装済みアーキテクチャ: Docker Example

**目標達成**: `docs/examples/docker/` にコード例を統合、`literalinclude` で参照

**実装内容**:

| コード種別 | 方式 | 配置 | 形式 |
| --- | --- | --- | --- |
| **Docker Compose** | ファイル参照 ✅ | `docs/examples/docker/` | .yaml |
| **C++/Python スニペット** | 準備済み | `docs/examples/root/` | 実ファイル |
| **Jupyter/出力結果** | 準備済み | `docs/examples/python/` | .py (jupytext) |
| **テキストのみの説明** | 埋め込み | ドキュメント | Markdown |

**現在の実装構造**:

```
kumaroot/
├── docs/
│   ├── source/
│   │   ├── docker/
│   │   │   └── docker-example-*.md     ← literalinclude で参照 ✅
│   │   └── ...
│   └── examples/                        ← 統合コード例（RTD対応）
│       ├── docker/                      ✅ 実装完了
│       │   ├── ubuntu.yaml
│       │   ├── nginx.yaml
│       │   ├── mariadb.yaml
│       │   └── ... (15個)
│       ├── root/                        📋 準備済み
│       └── python/                      📋 準備済み
│
├── mystmd/                              ← 独立（Node.js用）
└── scripts/                             ← 削除対象（python/ へ統合予定）
```

**達成事項**:
- ✅ Docker コード例の Single Source of Truth 実現
- ✅ 13 ファイルのドキュメント統一（25～35行）
- ✅ `docs/examples/docker/` に 15個の YAML 一元化
- ✅ すべてのドキュメントで `literalinclude` 対応
- ✅ DRY 違反を解消（ドキュメント↔ファイル自動同期）

---

## 5. 次フェーズの計画（ROOT とPython 統合）

### 5.1 ディレクトリ構造（Docker 実装済み、ROOT/Python 準備中）

```
kumaroot/
├── docs/
│   ├── source/
│   │   ├── root/
│   │   │   ├── root-usage.md
│   │   │   ├── root-th1-fill.md
│   │   │   │   ```{literalinclude} ../examples/root/th1-fill.cpp
│   │   │   │   :language: cpp
│   │   │   │   ```
│   │   │   └── ...
│   │   ├── docker/
│   │   │   ├── docker-examples.md
│   │   │   ├── docker-example-ubuntu.md
│   │   │   │   ```{literalinclude} ../examples/docker/ubuntu.yaml
│   │   │   │   :language: yaml
│   │   │   │   ```
│   │   │   └── ...
│   │   └── ...
│   └── examples/                       ← 全コード例を統合（RTD対応）
│       ├── README.md                  ← 使い方ガイド
│       ├── root/
│       │   ├── th1-fill.cpp
│       │   ├── th1-fill.py
│       │   ├── gstyle-setoptstat.cpp
│       │   └── ...
│       ├── docker/
│       │   ├── ubuntu.yaml
│       │   ├── mariadb.yaml
│       │   └── ...
│       └── python/                    ← jupytext形式
│           ├── matplotlib-intro.py    （YAML+Pythonヘッダ）
│           ├── pandas-gps.py
│           └── ...
│
├── mystmd/                            ← 独立継続（Node.js用）
├── scripts/                           ← （削除対象）
│
├── .pre-commit-config.yaml
│   # 追加:docs/examples/の構文チェック（shellcheck, pylintなど）
│   # 追加:docs/examples/python/のjupytext同期チェック
│
└── jupytext.toml
    # 更新:"docs/examples/python/" = "py:light"
```

### 5.2 jupytext設定（更新が必要）

**現在の`jupytext.toml`**:

```toml
[formats]
"notebooks/" = "ipynb"
"mystmd/" = "md:myst"
"scripts/" = "py:light"
```

**推奨される更新案**:

```toml
[formats]
# docs/examples/python/ に統一（scripts/ → docs/examples/python/）
"docs/examples/python/" = "py:light"

# MyST Markdown（Node.js処理対応、継続）
"mystmd/" = "md:myst"
```

**変更点**:
- `"scripts/" = "py:light"`→`"docs/examples/python/" = "py:light"`に変更
- `"notebooks/" = "ipynb"`は削除（notebooks/は使用しなくなる）
- `mystmd/`は独立継続（Node.js処理用）
- ReadtheDocs互換性を確保（`docs/`配下）

### 5.3 Sphinx 設定の変更

**docs/source/conf.py**:
```python
# MyST Parser 拡張有効化
myst_enable_checkboxes = True
myst_footnote_transition = False

# literalinclude の言語別ハイライト
highlight_language = 'python'

# コード例参照パスの設定
source_suffix = {'.md': 'markdown', '.rst': 'restructuredtext'}
```

### 5.4 .gitignore の更新

`.ipynb`ファイルをGitから除外:

```gitignore
# Jupyter (docs/examples/python/ で生成される)
docs/examples/**/*.ipynb
*.ipynb_checkpoints/
```

### 5.5 GitHub Actions CI の追加（オプション）

**`.github/workflows/validate-examples.yml`**:
```yaml
name: Validate Code Examples

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate Shell Scripts
        run: |
          find examples/ -name "*.sh" -exec shellcheck {} \;

      - name: Validate YAML
        run: |
          find examples/ -name "*.yaml" -exec yamllint {} \;

      - name: Check Python Examples (lint only)
        run: |
          pip install ruff
          ruff check examples/python/ --select E,W
```

### 5.6 ドキュメント記述ガイド（CLAUDE.md に追加）

```markdown
## サンプルコード管理

### コード例の配置

- **実行可能なコード**: `examples/<category>/` に配置
- **出力結果を含む例**: `notebooks/` の Jupyter Notebook を使用
- **テキストのみの説明**: ドキュメント内に直接記述

### 参照方法

#### C++/Python 例の参照（literalinclude）

```markdown
# C++ の例

:::{literalinclude} ../../examples/root/th1-fill.cpp
:language: cpp
:linenos:
:::
```

#### docker-compose.yaml の参照

```markdown
# Ubuntu コンテナの基本設定

:::{literalinclude} ../../examples/docker/ubuntu.yaml
:language: yaml
:::
```

### メンテナンス

- `examples/` 配下のコード変更を加えたら、ドキュメント文を確認
- Pre-commit フック実行時に構文チェックが自動実行
- GitHub Actions で全体の整合性を確認


---

## 6. 実装進捗（2026年5月30日）

### ✅ フェーズ1: Docker Example 実装完了

- ✅ `docs/examples/` ディレクトリ作成（root/、docker/、python/ を含む）
- ✅ Docker compose.yaml を `docs/examples/docker/` に統一（15個）
- ✅ CLAUDE.md に「サンプルコード管理」セクション追加
- ✅ `.gitignore` に `docs/examples/**/*.ipynb` を追加
- ✅ `jupytext.toml` を更新（`"docs/examples/python/" = "py:light"`）
- ✅ 13 ファイルのドキュメント統一化（テンプレート化）
- ✅ すべてのドキュメントで `literalinclude` 実装

### ✅ フェーズ2: Pythonサンプル・Jupyterノートブック統合完了

**完成内容**:

- ✅ `docs/examples/python/`に21個のPythonスクリプト統合（jupytext ライト形式）
- ✅ `docs/notebooks/`に21個のJupyterノートブックを自動生成（`.ipynb`）
- ✅ `jupytext.toml`を更新:
  - `"docs/examples/python/" = "py:light"` - ソース管理
  - `"docs/notebooks/" = "ipynb"` - ノートブック生成
- ✅ `.gitignore`に `docs/notebooks/**/*.ipynb`を追加（生成ファイル除外）
- ✅ `CLAUDE.md`に Python サンプルセクション追加
  - Single Source of Truth パターン説明
  - Jupyter ノートブック生成ワークフロー説明
  - 配置構造と管理方式を明記

**達成事項**:

- 21個のノートブックが `docs/notebooks/`に生成完了
- Python スクリプトはテキストベース（Git 管理）
- Jupyter ノートブックは自動生成（実行テスト用）
- 完全な Single Source of Truth（`.py`が唯一の情報源）
- Read the Docs 互換性確保（`docs/`配下）

### 📋 フェーズ 3: ROOT ドキュメント への適用（次）

- [ ] ROOT の簡単な例（th1-fill.cpp）を `docs/examples/root/` に移行
- [ ] `root-th1-fill.md` で `literalinclude` を試用
- [ ] CI で動作確認
- [ ] フィードバック収集

### 📋 フェーズ 4: 全体への展開（その後）

- [ ] 他の ROOT 例を順次 `docs/examples/` へ移行
- [ ] `scripts/` フォルダを削除（`docs/examples/python/` に統合）
- [ ] Pre-commit に「jupytext 同期チェック」を追加（オプション）
- [ ] GitHub Actions ワークフロー追加

### 📋 フェーズ 4: 最適化（継続的）

- [ ] CI での実行テスト追加（可能な限り）
- [ ] コード例の出力キャッシング
- [ ] ドキュメント生成時間の最適化

---

## 7. まとめ

### 現在の強み

✅ **ドキュメント設計の一貫性** - 「逆引き形式」が徹底されている  
✅ **開発プロセスの成熟** - Conventional Commits、版番号管理が確立  
✅ **スケーラブルな構造** - カテゴリ分離、toctree による拡張性  

### 課題

⚠️ **サンプルコード管理の分散** - 埋め込み、ファイル、Jupyter が混在  
⚠️ **DRY 違反** - ドキュメントとファイルの重複  
⚠️ **メンテナンスコスト** - 同期が手動、実行テストなし  

### 推奨する次のステップ

🎯 **Hybrid パターンの導入**
- `examples/` ディレクトリを作成し実行可能コード集約
- Sphinx の `literalinclude` で参照
- 段階的に既存ドキュメント に適用

🎯 **CI 自動化**
- コード例の構文検証
- 実行可能なものの実行テスト
- 定期的な整合性チェック

このアプローチにより、**保守性と信頼性を大幅に向上**させることができます。

---

**付録**: メモリに保存した feedback 参照  
参考: [[feedback_root_review_policy.md](../memory/feedback_root_review_policy.md)]
