# Claudeしたい（`claude`）

```console
$ brew install --cask claude
$ claude
```

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
