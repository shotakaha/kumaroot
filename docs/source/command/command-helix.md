# Helixしたい（``hx``）

```console
$ brew install helix
```

[vim](./command-vim.md)などにインスパイアされたモーダルエディターです。
vimより、コマンド操作のキーバインドに一貫性があったり、
ヘルプ／補完パネルを表示してくたりと親切です。

真のvimmerを目指さないのであれば、こちらのほうが使いやすいと思いました。
僕はGitエディターに``hx``を設定しています。

```cfg
# ~/.gitconfig
[core]
    editor = hx
```
