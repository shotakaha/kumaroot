# Emacsしたい（`emacs`）

```console
$ emacs
$ emacsclient
```

`emacs`は、Emacsエディターを操作するコマンドです。
キーバインドがクセつよですが、カスタマイズすればするほど、手に馴染んできます。
Emacs24からパッケージ管理システムに対応してパッケージの導入も簡単になりました。

ゼロからカスタマイズしてもいいのですが、
[Emacs Prelude](https://prelude.emacsredux.com/en/latest/)や
[Spacemacs](https://www.spacemacs.org/)など、好みのディストリビューションを導入するのがよいと思います。
細かいことは[](../emacs/emacs-usage.md)に整理しました。

:::{note}

大学の時の親友が「Emacsは環境だよ」と教えてくれました。
最初はなにを言っているのかさっぱりわかりませんでしたが、使い続けているうちにその意味が分かってきました。
一度Emacsを起動するとテキスト編集だけでなく、ブラウジングやメール操作も含めて、すべてそこで簡潔させたくなるのです。

:::

## インストールしたい（`emacs`）

```console
$ brew info emacs-app
$ brew install --cask emacs-app
$ brew upgrade emacs-app
```

`emacs`はHomebrewでインストールできます。
フォーミュラ名は`emacs`、カスク名は`emacs-app`です。
GUI版Emacsを使う場合は`emacs-app`をインストールします。

:::{note}

2009年ころからEmacsを使っていましたが、2020年ころにVS Codeに乗り換えました。
GitHubアカウントを介して、複数のパソコンで設定が同期できるのはとても便利です。

しかし、VS Codeはあくまでエディターであり、ブラウジングだったり、メールの読み書きをしたいとは思いません。
Emacsを使っていたころに感じた「ずっとここで作業してたい」という感覚はなんだったのでしょうか。

:::

## 特定の行を開きたい（`+LINE`）

```console
$ emacs +42 ファイル名
```

ファイル名の前に`+LINE`を指定すると、指定した行にカーソルを合わせた状態でファイルを開けます。
`grep`や`rg`の検索結果からジャンプしたいときに便利です。

## ターミナル内で起動したい（`-nw`）

```console
$ emacs -nw ファイル名
```

`-nw`（`--no-window-system`）オプションで、GUIウィンドウを開かずにターミナル内でEmacsを起動できます。
SSH接続先などGUIが使えない環境で使います。

## 素の状態で起動したい（`-Q`）

```console
$ emacs -Q
```

`-Q`（`--quick`）オプションで、`init.el`などの設定ファイルを一切読み込まずに起動できます。
設定ファイルのトラブルシューティングや、パッケージの動作確認に使います。

## スクリプトとして実行したい（`--batch`）

```console
$ emacs --batch --eval '(princ (+ 1 2))'
3
```

`--batch`オプションで、GUIを使わずにEmacs Lispを実行できます。
設定ファイルの検証や、簡単な処理の自動化に使います。

## デーモンしたい（`--daemon`）

```console
// デーモンを起動（1度だけ）
$ emacs --daemon

// emacsclientで接続
$ emacsclient ファイル名
```

`emacs --daemon`でEmacsをデーモンとして常駐させることができます。
このデーモンに対して、`emacsclient`から接続する運用もできます。
Emacsのデメリットである起動コストを省略できるので、長時間使うほど便利さを感じられます。
詳しくは[Emacsクライアントしたい](../emacs/emacs-emacsclient.md)を参照してください。
