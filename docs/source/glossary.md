# 用語集

```{eval-rst}
.. index::
    pair: Sphinx; glossary
```

## Sphinx

OSS開発などで利用されているドキュメンテーションビルダーのひとつ。
ひとつのソースファイルからさまざまな形式に出力できるのでとても便利。
``reST`` 記法を覚えるのは大変なので ``MyST`` 拡張を導入して
``Markdown`` 記法で書けるようにすることをオススメします。

```{eval-rst}
.. index::
    pair: ROOT; glossary
```

## ROOT

高エネルギー物理学分野で利用されている解析用フレームワーク。
スイスのCERNを中心に開発されている。

```{eval-rst}
.. index::
    pair: GAS; glossary
```

## Google Apps Script (GAS)

Googleサービスを自動化するためのスクリプト言語。
V8ランタイムに対応しており、実質JavaScriptと思ってコーディングしてよさそう。

```{eval-rst}
.. index::
    pair: LaTeX; glossary
```

## LaTeX

文書を作成するための組版ソフト。
（理系の）学術分野でよく使われている。
定型のある文書を作成するのに適している。

```{eval-rst}
.. index::
    pair: Emacs; glossary
```

## Emacs

昔からあるテキストエディター。
独特なキーバインドで操作する必要があるが、一度慣れてしまうともう離れられない。

```{eval-rst}
.. index::
    pair: VSCode; glossary
```

## Visual Studio Code (VS Code)

モダンなテキストエディター。
近年、急速にシェアを伸ばしてきている（と思う）。
僕もEmacsから乗り換えた。
Awsome Emacs Keymap の拡張機能を追加すればEmacsのキーバインドが使えて快適。

```{eval-rst}
.. index::
    pair: Git; glossary
```

## Git

ファイルのバージョン管理をするためのコマンドラインツール。
使い方を覚えるために訓練は必要だが、Subversionなどの従来の
ツールより使いやすくなっている気がする。

```{eval-rst}
.. index::
    single: Git; GitHub
```

## GitHub

Gitリポジトリのホスティングサービスのひとつ。
OSS開発などで多用されている。
外部サービスと連携して使いやすくする必要がある。

```{eval-rst}
.. index::
    single: Git; GitLab
```

## GitLab

Gitリポジトリのホスティングサービスのひとつ。
変更の承認機能やCIツールも組み込まれていて、
はじめからチームでの運用がしやすくなっていると感じる。
GitLab自体がOSSなので、オンプレミスでホストすることもできる。

```{eval-rst}
.. index::
    single: Python; programming language
```

## Python

プログラミング言語のひとつ。データ分析・科学計算・Webアプリケーション開発など幅広い用途で使用される。
KumaROOTの多くのツールやライブラリが依存している基本的な言語。

```{eval-rst}
.. index::
    single: Docker; containerization
```

## Docker

コンテナー型仮想化技術。アプリケーションと依存関係をイメージとしてパッケージ化し、
一貫した実行環境を構築することで、開発環境から本番環境までの環境差異を排除できる。
近年のチーム開発で必須のツール。

```{eval-rst}
.. index::
    single: NumPy; Python library
```

## NumPy

Python向けの数値計算ライブラリ。多次元配列（ndarray）と線形代数・フーリエ変換などの
高速な計算機能を提供する。Pythonデータ分析・科学計算の基盤をなす。

```{eval-rst}
.. index::
    single: Pandas; Python library
```

## Pandas

Python向けのデータフレームライブラリ。CSV・JSONなどの形式でデータを読み込み、
グルーピング・結合・ピボットなどの操作で統計分析・データクリーニングを実施する。

```{eval-rst}
.. index::
    single: Matplotlib; data visualization
```

## Matplotlib

Pythonにおける主要な2次元グラフ描画ライブラリ。線グラフ・散布図・ヒストグラムなど
さまざまな図表を生成できる。データ分析結果を視覚的に表現するのに使われる。

```{eval-rst}
.. index::
    single: JSON; data format
```

## JSON

JavaScriptオブジェクト記法を基にしたデータ交換形式。
Webアプリケーション・REST API・設定ファイルなど多くの場所で使用される。
人間が読みやすく、多くのプログラミング言語でサポートされている。

```{eval-rst}
.. index::
    single: YAML; configuration format
```

## YAML

人間が読みやすい設定ファイル形式。Docker Compose設定・CI/CDパイプライン設定・
Kubernetesマニフェストなど、さまざまな設定ファイルで標準的に使用されている。
インデント構造で階層的なデータを表現できる。

```{eval-rst}
.. index::
    single: Jupyter; interactive environment
```

## Jupyter

対話的なPython実行環境。Jupyter NotebookやJupyter Labでコード・実行結果・説明文を
統合したドキュメントを作成できる。データ分析・機械学習の開発や学習に最適。

```{eval-rst}
.. index::
    single: pytest; testing framework
```

## pytest

Python向けのユニットテストフレームワーク。テストケースの実行・結果の報告を簡潔に行える。
fixtureやプラグインで拡張可能で、TDD（テスト駆動開発）に適している。

```{eval-rst}
.. index::
    single: Poetry; package management
```

## Poetry

Python向けの依存関係・パッケージ管理ツール。pyproject.tomlで統一的に管理でき、
仮想環境の作成・パッケージのインストール・プロジェクトのビルド・公開が簡単。

```{eval-rst}
.. index::
    single: GitHub Actions; CI/CD
```

## GitHub Actions

GitHubに統合されたCI/CDサービス。push・PRなどのイベントをトリガーに
自動テスト・ビルド・デプロイを実行できる。YAMLで設定ファイルを記述する。

```{eval-rst}
.. index::
    single: GitLab CI; CI/CD
```

## GitLab CI

GitLabに統合されたCI/CDサービス。.gitlab-ci.ymlでパイプラインを設定し、
push・MRなどのイベントで自動テスト・ビルド・デプロイを実行する。

```{eval-rst}
.. index::
    single: virtual environment; Python
```

## 仮想環境

Pythonプロジェクトごとに独立した実行環境を構築する仕組み。
プロジェクト間での依存パッケージのバージョン競合を防げる。
venv・virtualenv・Poetry・pyenvなどのツールで構築する。

```{eval-rst}
.. index::
    single: REST API; web service design
```

## REST API

HTTP（GET・POST・PUT・DELETE）によるリソース操作を基本とするWebサービス設計様式。
シンプルで標準化されており、多くのWebアプリケーション・モバイルアプリで使用される。

```{eval-rst}
.. index::
    single: CLI; command-line interface
```

## CLI

コマンドラインからツール・ソフトウェアを操作するインターフェイス。
GUIと比べてスクリプト化・自動化がしやすく、サーバー環境での運用に適している。

```{eval-rst}
.. index::
    single: API; application programming interface
```

## API

ソフトウェア間のやり取り仕様。外部ライブラリ・サービスの機能を利用する接点となる。
REST API・GraphQL・gRPCなど、さまざまな実装形式がある。

```{eval-rst}
.. index::
    single: SSH; network protocol
```

## SSH

暗号化ネットワークプロトコル。リモートサーバーへの安全なアクセス・コマンド実行・
ファイル転送（SCP・SFTP）などに使われる。認証に秘密鍵を使用する。

```{eval-rst}
.. index::
    single: JavaScript; programming language
```

## JavaScript

Webブラウザで実行される主要なプログラミング言語。フロントエンド開発の中心的な言語で、
Node.jsでサーバーサイド開発にも利用される。ECMAScript標準に準拠。

```{eval-rst}
.. index::
    single: TypeScript; programming language
```

## TypeScript

JavaScriptの拡張言語。静的型チェック機能を追加し、大規模プロジェクトでのバグ軽減・
開発効率向上が期待できる。Webアプリケーション・Node.jsアプリケーション開発で人気。

```{eval-rst}
.. index::
    single: C++; programming language
```

## C++

高速・効率的なプログラミング言語。ROOTフレームワークなどの科学計算ライブラリや
ゲームエンジン・組み込みシステムの開発に使われる。

```{eval-rst}
.. index::
    single: Rust; programming language
```

## Rust

メモリ安全性を保証しながら高速実行可能なプログラミング言語。
システムプログラミング・WebAssembly・CLIツール開発などで注目されている。

```{eval-rst}
.. index::
    single: SciPy; Python library
```

## SciPy

Python向けの科学計算・統計分析ライブラリ。最適化・信号処理・統計分布など
高度な数学関数を提供する。NumPyと組み合わせて使うことが多い。

```{eval-rst}
.. index::
    single: Plotly; visualization library
```

## Plotly

インタラクティブなグラフ描画ライブラリ。Pythonで利用でき、Web上で動作する
3次元プロット・地図表示など多様な可視化に対応している。

```{eval-rst}
.. index::
    single: scikit-learn; machine learning
```

## scikit-learn

Python向けの機械学習ライブラリ。分類・回帰・クラスタリング・次元削減など
幅広いアルゴリズムを提供し、統計分析・データマイニングに多用される。

```{eval-rst}
.. index::
    single: MyST; markdown parser
```

## MyST

Sphinxで使用するMarkdownパーサー。通常のSphinxはreStructuredText（reST）でしか記述できないが、
MyST拡張を導入することでMarkdown記法でドキュメントを作成できる。

```{eval-rst}
.. index::
    single: Typst; document markup
```

## Typst

最新のドキュメントマークアップ言語・組版システム。LaTeXの後継として開発され、
シンプルな記法で高品質な文書を効率的に作成できる。

```{eval-rst}
.. index::
    single: Hugo; static site generator
```

## Hugo

高速なスタティックサイトジェネレーター。GoかGo言語で開発されており、
Markdown記法でブログ・ドキュメントサイトを効率的に構築できる。

```{eval-rst}
.. index::
    single: Black; code formatter
```

## Black

Python向けのコードフォーマッター。コード規約を自動的に統一し、
チーム内でのコードスタイルの一貫性を保ちやすくする。

```{eval-rst}
.. index::
    single: MyPy; static type checker
```

## MyPy

Python向けの静的型チェッカー。型ヒントの妥当性を検査し、
実行前にバグを発見・修正できる。開発効率・コード品質向上に役立つ。

```{eval-rst}
.. index::
    single: Homebrew; package manager
```

## Homebrew

macOS向けのパッケージマネージャー。OSに付属しないツール・ライブラリを
簡単にインストール・管理・アップデートできる。LinuxにはLinuxbrewがある。

```{eval-rst}
.. index::
    single: pre-commit; git hooks
```

## pre-commit

Gitのpre-commitフックを簡単に管理するフレームワーク。
コミット前に自動的にコードフォーマット・リント・テストなどを実行し、品質維持を支援。

```{eval-rst}
.. index::
    single: TOML; configuration format
```

## TOML

設定ファイル形式。YAML同様に人間が読みやすく、pyproject.toml（Python）・Cargo.toml（Rust）など
プログラミング言語のプロジェクト設定で広く使用されている。

```{eval-rst}
.. index::
    single: Geant4; simulation framework
```

## Geant4

高エネルギー物理分野で利用される粒子・放射線シミュレーションフレームワーク。
CERN開発で、粒子検出器の応答・放射線量の計算などに用いられる。
