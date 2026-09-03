# KumaROOTプロジェクトレビュー

**レビュー日**: 2026年5月30日 → 2026年9月3日更新
**対象**: ドキュメント設計、サンプルコード配置、コード管理設計
**前回**: 2026年5月30日（Docker Example・Pythonサンプル統合の作業ログ。完了分は本稿から削除し、[AGENTS.md](./AGENTS.md)の *Sample Code Management* 節に反映済み）

---

## 1. 現状サマリー

| 指標 | 値（2026年9月3日時点） |
| --- | --- |
| Git管理ファイル数 | 約1,565 |
| ドキュメントページ（`.md`/`.rst`） | 約1,277 |
| カテゴリ（`docs/source/*/`） | 38 |
| ROOTリファレンスページ | 109 |
| 画像資産 | 54 |
| ビルド | Sphinx + MyST Parser |
| 公開先 | Read the Docs（主）、GitHub Pages（`static.yml`、併存） |

### 確立済みの強み

- **「逆引き形式」の一貫性**——「〇〇したい」ベースの構成が全カテゴリで徹底されている
- **日本語スタイル規約**——JTF準拠、[AGENTS.md](./AGENTS.md)に体系化
- **開発プロセスの成熟**——Conventional Commits + Commitizen、カレンダーベース版番号（YYYY.MM.PATCH）、pre-commit（Ruff・JSON・TOML・YAML検証）、`uv`による依存統一
- **リリース自動化**——`v*`タグのpushで`release.yml`がGitHub Releaseを作成する（本文はCHANGELOG.mdの該当バージョン節を切り出す）。週次の`update_changelog.yml`がCHANGELOGを追従更新する
- **コード例のSingle Source of Truth（Docker・Python完了）**——`docs/examples/`に実ファイルを集約し、`literalinclude`で参照する

### 完了済み（前回レビューからの成果）

- **Docker Example**: 13ドキュメントをテンプレート統一（平均215行→32行）、YAML15個を`docs/examples/docker/`に集約、旧`docker/examples/`サブディレクトリを削除
- **Pythonサンプル**: `docs/examples/python/`に21スクリプト（jupytext light形式）、`docs/notebooks/`に`.ipynb`21個を自動生成（`.gitignore`済み）
- **設定反映済み**: `jupytext.toml`は`docs/examples/python/`・`docs/notebooks/`・`mystmd/`の3フォーマット構成。`.gitignore`に`docs/examples/**/*.ipynb`と`docs/notebooks/**/*.ipynb`

---

## 2. 未解決の課題

### 🔴 2.1 `scripts/`が旧版のまま残存し、`docs/examples/python/`と分岐している

- `scripts/`は**2024年12月が最後の更新**。以降jupytext管理外（`jupytext.toml`にエントリなし）。
- `docs/examples/python/`（2026年5月作成）とファイル名は21個すべて一致するが、**中身は分岐**している（`bs4.py`・`pandas-gps.py`などが相違。一部のみ同一）。
- どちらが正なのか文書上で明示されておらず、編集先を誤ると片方が腐る。

**推奨**:

1. `scripts/`と`docs/examples/python/`を1ファイルずつdiffし、`scripts/`側に生きた変更が残っていないか確認する
2. 生きた差分があれば`docs/examples/python/`へ取り込む
3. `scripts/`を削除する（`git rm -r scripts/`）
4. `notebooks/`（リポジトリ直下、jupytext旧出力先）も未使用なら同時に削除する
5. 削除を1コミットにまとめる（`refactor(examples): drop legacy scripts/ and notebooks/ dirs`）

### 🟡 2.2 `python-jupytext.md`が旧ディレクトリ構成を例示している

[docs/source/python/python-jupytext.md](docs/source/python/python-jupytext.md)の`jupytext.toml`サンプル（122行付近）が

```toml
"notebooks/" = "ipynb"
"markdowns/" = "md:myst"
"scripts/" = "py:light"
```

と、実リポジトリの構成（`docs/examples/python/`・`docs/notebooks/`・`mystmd/`）と食い違っている。読者がこの例を真似ると旧構成を再現してしまう。

**推奨**: リポジトリ実物の`jupytext.toml`に合わせて書き換える（`fix(python-jupytext): align jupytext.toml sample with repo layout`）。

### 🟡 2.3 `docs/examples/root/`が空のまま（フェーズ3未着手）

ディレクトリだけ存在し中身はゼロ。ROOTリファレンスは109ページあり、C++/Pythonコードはすべて`.md`に埋め込まれている。Docker・Pythonで確立したパターンをROOTに広げる作業が止まっている。

**推奨**（着手する場合の最小ステップ）:

1. `root-th1-fill.md`のC++/Python例を`docs/examples/root/th1-fill.cpp`・`.py`に切り出す
2. 同ページを`literalinclude`に置換し、ビルドを確認する（`task docs:build`）
3. 1ページで運用感を確かめてから横展開の可否を判断する
4. ROOT例は**実行にビルド環境が必要**なため、pre-commit・CIでの構文チェックは「コンパイルせずlintのみ」に留めるのが現実的

### 🟢 2.4 Read the DocsとGitHub Pagesの二重公開

`static.yml`がpushごとにGitHub Pagesへデプロイする一方、[AGENTS.md](./AGENTS.md)と`pyproject.toml`の`homepage`はRead the Docsを正としている。意図的な冗長化（今回は維持を選択）だが、どちらが「正」かを[AGENTS.md](./AGENTS.md)に一文で明記しておくと迷いがない。

---

## 3. コード例配置の設計（現行）

```
kumaroot/
├── docs/
│   ├── source/
│   │   ├── docker/docker-example-*.md   ← literalinclude で参照（統一テンプレート）
│   │   ├── root/root-*.md               ← 現状はコード埋め込み（フェーズ3で切り出し予定）
│   │   └── <38 categories>/
│   ├── examples/                        ← 実行可能コードの集約先（RTD 配下、literalinclude 対象）
│   │   ├── docker/   … 15 YAML          ✅ 完了
│   │   ├── python/   … 21 .py (jupytext) ✅ 完了
│   │   └── root/                        ⬜ 空（フェーズ3）
│   └── notebooks/   … 21 .ipynb 自動生成（.gitignore）
├── mystmd/                              ← MyST Markdown、Node.js ツールチェーン用に独立継続
├── scripts/                            ⚠️ 旧 jupytext 出力、2024-12 以降放置（2.1 で削除提案）
└── notebooks/                          ⚠️ リポジトリ直下の旧出力先、未使用（2.1 で削除提案）
```

**配置ルール**（[AGENTS.md](./AGENTS.md)の *Sample Code Management* に準拠）:

| コード種別 | 方式 | 配置 |
| --- | --- | --- |
| Docker Compose | `literalinclude`参照 | `docs/examples/docker/*.yaml` |
| Pythonスニペット | jupytext `.py`（`--sync`で`.ipynb`生成） | `docs/examples/python/*.py` |
| C++/Python（ROOT） | 当面は埋め込み、順次`literalinclude`へ | `docs/examples/root/`（予定） |
| テキストのみの説明 | ドキュメント内に直接記述 | —— |

---

## 4. 次のステップ（優先順）

1. **`scripts/`・直下`notebooks/`の整理**——2.1。分岐の確認→取り込み→削除。低リスク・高効果。
2. **`python-jupytext.md`の修正**——2.2。読者が旧構成を再現しないよう即時対応。
3. **ROOTパターン適用のパイロット**——2.3。`root-th1-fill.md`1ページで試し、横展開の判断材料にする。
4. **[AGENTS.md](./AGENTS.md)に公開先の「正」を明記**——2.4。

CIでの実行テスト・出力キャッシュ・ビルド時間最適化は、上記が片付いてから改めて検討する。

---

**参考**: レビュー方針はauto-memory（`memory/`配下）に保存。
