# プロジェクトしたい（`quarto create`）

```console
// quarto create [type] [commands...]
// type: project | extension
// project_template: default | website | blog | book | manuscript | confluence
// extension_template: shortcode | filter | revealjs plugin | journal format | custom format | metadata | brand | engine

$ quarto create project website --no-prompt .
$ quarto create project website --no-prompt test-website
```

`quarto create`コマンドでプロジェクトを作成できます。
`[type]`は`project`もしくは`extension`を指定します。

:::{caution}

`quarto create --help`で表示されるシグネチャと、
実際のコマンドの使い方が合っていないようです。
`type`指定のあとに、テンプレート指定が必要です。
テンプレートは`type`によって選択肢が異なります。

:::

## ウェブサイトしたい（`quarto create project website`）

```console
$ quarto create project website test-website
```

:::{note}

`quarto create`コマンドは、カレントディレクトリにしかプロジェクトを作成できないようです。

```console
// 絶対パスを指定しても、カレントディレクトリにプロジェクトが作成される
$ quarto create project website /tmp/test-website
```

:::
