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

## 3. サンプルコード配置の現状分析

### 3.1 コード管理場所（複数の分散）

```
kumaroot/
├── docs/source/
│   ├── root/root-*.md          ← C++/Python コード例（埋め込み）
│   ├── docker/examples/        ← 実ファイル（docker-compose.yaml など）
│   │   ├── docker-ubuntu/compose.yaml
│   │   ├── docker-mariadb/
│   │   └── docker-wordpress-mariadb/
│   ├── emacs/fig/              ← スクリーンショット
│   ├── git/fig/
│   └── (その他の例)
│
├── scripts/                    ← jupytext形式（py:light）
│   ├── matplotlib.py           （YAML+Pythonヘッダ）
│   ├── pandas-dataframe.py
│   ├── pexpect.py
│   └── (20+ ファイル）
│
├── mystmd/                     ← MyST Markdown形式（md:myst）
│   ├── index.md
│   ├── matplotlib.md
│   └── (20+ ファイル)
│
└── notebooks/                  ← （将来：scripts/を統合）
    └── （現在は未使用）
```

### 3.2 問題点と傾向

| コード配置 | 形式 | 特徴 | 課題 |
| --- | --- | --- | --- |
| **docs/source/*.md** | Markdown 埋め込み | テキスト、そのまま表示 | バージョン追跡不可、実行テストなし |
| **docs/source/docker/examples/** | 実ファイル（YAML など） | コピペ実行可能 | ドキュメントとの同期が手動、メンテナンスコスト高 |
| **scripts/** | Jupyter (jupytext) | 実行可能、出力キャプチャ可 | コンテンツと物理分離、更新追跡が煩雑 |
| **mystmd/** | MyST Markdown | Node.js 処理対応 | 用途不明確、ドキュメント連携が不明 |

### 3.3 同期・メンテナンスの現状

現在のワークフロー：

```
コード変更
  ↓
（手動で）ドキュメント内のコード例を修正
  ↓
（手動で）docker-compose.yaml を更新
  ↓
Pre-commit フック（Ruff, JSON検証）チェック
  ↓
コミット
```

**問題**:
- ✗ ドキュメント内コード例とファイルの同期が手動
- ✗ `docker-compose.yaml` の変更を `docker-example-ubuntu.md` に反映するのが手作業
- ✗ コード例の実行確認がない
- ✗ `scripts/` フォルダの実行結果がドキュメントに現れていない

---

## 4. よりよいサンプルコード管理設計の提案

### 案 A: 「Single Source of Truth」パターン

**目標**: コード ファイルを唯一の情報源にし、ドキュメントから自動生成・参照

```
kumaroot/
├── docs/source/docker/examples/
│   ├── docker-ubuntu/
│   │   ├── compose.yaml          ← 実ファイル（唯一の情報源）
│   │   └── README.md             ← 説明（生成可能）
│   └── ...
│
├── examples/                      ← コード例の専用フォルダ（新規）
│   ├── root/
│   │   ├── root-th1-fill.cpp     ← C++ 例（実行可能）
│   │   ├── root-th1-fill.py      ← Python 例（実行可能）
│   │   └── root-rdataframe.cpp
│   ├── docker/
│   │   └── (docker-compose.yaml への参照)
│   └── ...
│
└── docs/source/*.md
    ├── <!-- include-code: ../examples/root/root-th1-fill.cpp -->
    ├── <!-- include-code: ../examples/root/root-th1-fill.py -->
    └── （ドキュメンテーション文）
```

**実装方式**:
- Sphinx の `literalinclude` 指令を使用（既に MyST Parser が対応）
- コード例を `examples/` に集約
- ドキュメントから `{{ include("../../examples/...") }}` で参照
- Git で examples/ 以下の変更を追跡

**メリット**:
- ✅ コード例が実行可能・テスト可能
- ✅ DRY (Don't Repeat Yourself)
- ✅ バージョン管理が明確
- ✅ CI で実行テスト可能

**課題**:
- パス管理が複雑（相対パス調整）
- MyST Parser の `include` 指令の確認が必要

### 案B:「docs/examples統合+jupytext」パターン（推奨）

**目標**: 全コード例を`docs/examples/`に統合し、jupytextで`.py`を管理

```
kumaroot/
├── docs/
│   ├── source/
│   │   ├── *.md
│   │   ├── root/
│   │   └── ...
│   ├── examples/                       ← 全コード例を統合（RTD対応）
│   │   ├── README.md
│   │   ├── root/
│   │   │   ├── th1-fill.cpp
│   │   │   ├── th1-fill.py
│   │   │   └── ...
│   │   ├── docker/
│   │   │   └── ubuntu.yaml
│   │   └── python/                    ← jupytext形式
│   │       ├── matplotlib-intro.py    （YAML+Pythonヘッダ）
│   │       ├── pandas-gps.py
│   │       └── ...
│   └── _build/
│
├── mystmd/                            ← 独立（Node.js用）
└── docs/source/*.md
    └── <!-- 全て ../examples/ を参照 -->
```

**実装方式**:
- jupytextで`.py`/`.md`を**単一ソース**として管理（`docs/examples/python/`配下）
- `.ipynb`は必要時に自動生成（Git管理外）
- Pre-commitで`.py`と`.md`の同期を自動化
- `scripts/`フォルダを削除して`docs/examples/python/`に統合

**メリット**:
- ✅**コード例の源が一箇所**（`docs/examples/`）
- ✅**ReadtheDocs対応**（`docs/`配下なので安全）
- ✅**テキストベース管理**（Git diff/merge容易）
- ✅ドキュメントから`../examples/`で全て参照可能
- ✅ファイル管理がシンプル（`.ipynb`バイナリ化回避）
- ✅既に`scripts/`にjupytext形式が存在

**課題**:
- プロジェクトルート直下の`examples/`から`docs/examples/`への移動
- `scripts/` → `docs/examples/python/`への移行作業

### 案C:「docs/examples全統合」パターン（最終推奨）

**全コード例を`docs/examples/`に統合し、ドキュメント参照を一元化**

|コード種別|方式|配置|形式|
|---|---|---|---|
|**実行可能コード**(Docker,bash)|ファイル参照|`docs/examples/`|実ファイル|
|**C++/Pythonスニペット**|ファイル埋め込み|`docs/examples/`|実ファイル|
|**Jupyter/出力結果を含む例**|jupytext管理|`docs/examples/python/`|`.py`(jupytext)|
|**テキストのみの説明**|埋め込み|ドキュメント|Markdown|

**実装構造**:

```
kumaroot/
├── docs/
│   ├── source/
│   │   ├── root/root-th1-fill.md
│   │   │   (includes: ../examples/root/th1-fill.cpp)
│   │   ├── docker/docker-example-ubuntu.md
│   │   │   (includes: ../examples/docker/ubuntu.yaml)
│   │   └── ...
│   └── examples/               ← 全コード例を統合（RTD対応）
│       ├── README.md
│       ├── root/
│       │   ├── th1-fill.cpp   # literalinclude で参照
│       │   ├── th1-fill.py
│       │   └── ...
│       ├── docker/
│       │   └── ubuntu.yaml    # literalinclude で参照
│       └── python/            ← jupytext形式
│           ├── matplotlib-intro.py
│           ├── pandas-gps.py
│           └── ...
│
├── mystmd/                    ← 独立（Node.js用）
└── scripts/                   ← （削除対象）
```

**メリット**:
- ✅**コード例の源が一箇所**（`docs/examples/`に統一）
- ✅**ReadtheDocs対応**（`docs/`配下で安全）
- ✅全てのドキュメント参照が`../examples/`で統一
- ✅`.ipynb`のバイナリ化を避ける（Gitdiff/merge容易）
- ✅`scripts/`フォルダを削除してスッキリ
- ✅段階的な導入が可能

**導入手順**:
1. `docs/examples/`ディレクトリを作成
2. `docs/examples/root/`、`docs/examples/docker/`を作成
3. `docs/examples/python/`を作成（`scripts/`をここに移行）
4. `docs/source/docker/examples/`から`.yaml`をコピー
5. ROOTドキュメントで`literalinclude`を試用
6. Pre-commitに「jupytext同期チェック」を追加（オプション）
7. `.gitignore`に`docs/examples/**/*.ipynb`を追加
8. `scripts/`フォルダを削除
9. `jupytext.toml`を更新（`"docs/examples/python/" = "py:light"`）

---

## 5. 推奨実装案（docs/examples全統合）の詳細

### 5.1 ディレクトリ構造の提案

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

## 6. 移行計画（段階的実装）

### フェーズ1:基盤準備（1〜2週間）

- [ ] `examples/`ディレクトリ作成（root/、docker/、python/を含む）
- [ ] 既存Docker compose.yamlを`examples/docker/`にコピー
- [ ] `scripts/`を`examples/python/`に移行
- [ ] CLAUDE.mdに「サンプルコード管理」セクション追加
- [ ] `.gitignore`に`examples/**/*.ipynb`を追加
- [ ] `jupytext.toml`を更新（`"examples/python/" = "py:light"`）

### フェーズ2:ROOTドキュメントへの適用（2〜4週間）

- [ ] ROOTの簡単な例（th1-fill.cpp）を`examples/root/`に移行
- [ ] `root-th1-fill.md`で`literalinclude`を試用
- [ ] CIで動作確認
- [ ] フィードバック収集

### フェーズ3:全体への展開（段階的）

- [ ] 他のROOT例を順次`examples/`へ移行
- [ ] Docker例を`examples/docker/`に統一
- [ ] `scripts/`フォルダーを削除
- [ ] Pre-commitに「jupytext同期チェック」を追加（オプション）
- [ ] GitHubActionsワークフロー追加

### フェーズ4:最適化（継続的）

- [ ] CIでの実行テスト追加（可能な限り）
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
