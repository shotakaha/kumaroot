# 自前のパッケージを定義したい（`\ProvidesPackage`）

```latex
%% パッケージ名.sty
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{自作パッケージ名}[yyyy/mm/dd vバージョン パッケージの説明]

% 必要なパッケージ
\RequirePackage{graphicx}

% カスタムコマンド
\newcommand{\コマンド名}[引数の数]{コマンドの定義}

% カスタム環境
\newenvironment{環境名}[オプション]{%
  環境の定義
}
```

自作したコマンドや環境を**パッケージ**としてまとめることができます。
ファイルの拡張子は`.sty`とし、`$HOME/texmf/`に配置し、`$ mktexlsr ~/texmf`を実行します。

## パッケージ化したい

```console
パッケージ名/
├── tex/latex/パッケージ名/    # パッケージ本体
│   ├── パッケージ名.sty        # パッケージの機能
│   └── パッケージ名.cls        # クラスファイル（必要なら）
├── doc/latex/パッケージ名/    # ドキュメントやサンプルコード
│   ├── パッケージ名.pdf        # ドキュメント（PDF形式）
│   ├── パッケージ名.tex        # PDFドキュメントを生成するLaTeXソース
│   ├── examples/             # サンプルコード
│   │   └── example1.tex
│   └── README.md             # リポジトリ用の簡易説明
├── source/latex/パッケージ名/    # ソースコード（生成用ファイル）
│   ├── パッケージ名.dtx           # ソースファイル
│   └── パッケージ名.ins           # インストールスクリプト
└── LICENSE    # ライセンス情報
```

パッケージを作成する時のディレクトリ構造です。
どこかに定義されている訳ではないですが、
最近のパッケージはこのような構造になっていることが多い気がします。

```console
$ latex パッケージ名.ins       # パッケージ名.styを生成
$ lualatex パッケージ名.dtx    # パッケージ名.pdfを生成
```

### ビルド用ファイル（`.dtx`）

```latex
% パッケージ名.dtx

% ドライバーの設定: PDFドキュメントを生成するための設定
% \iffalse
%<*driver>
\documentclass{ltxdoc}
\EnableCrossrefs
\CodelineIndex
\RecordChanges
\begin{document}
  \DocInput{パッケージ名.dtx}
\end{document}
%</driver>
% \fi

% ドライバーの設定: PDFドキュメントを生成するための設定
%<package>
\ProvidesPackage{パッケージ名}[yyyy/mm/dd vバージョン パッケージの一行説明]
\newcommand{\コマンド}[引数の数]{コマンドの内容}
%</package>

%<class>
\ProvidesClass{クラス名}[yyyy/mm/dd vバージョン クラスの一行説明]
\newcommand{\コマンド}[引数の数]{コマンドの内容}
%</class>
```

### インストール用ファイル（`.ins`）

```latex
% パッケージ名.ins
%
% This is the installation script for パッケージ名.
% Run this file with the command: latex パッケージ名.ins
% This will generate the following files:
% - パッケージ名.sty: The LaTeX package
% - パッケージ名.cls: The document class
%
% docstripパッケージを読み込む（.dtxからコードを抽出）
\input docstrip
% 実行時の進捗メッセージを抑制（オプション）
\keepsilent

% ファイル生成のルールを定義
% パッケージファイルを生成
\generate{
  \file{パッケージ名.sty}{\from{パッケージ名.dtx}{package}}
}

% クラスファイルを生成（オプション）
\generate{
  \file{パッケージ名.cls}{\from{パッケージ名.dtx}{class}}
}

% スクリプトの終了
\endbatchfile
```
