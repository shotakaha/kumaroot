# 目次したい（``_toc.yml``）

```console
$ myst init --write-toc
```

ウェブサイトのテーマがデフォルト（``book-theme``）の場合、左サイドバーには、サイト構造の目次が自動で表示されます。

この目次は、プロジェクト直下に置いた``_toc.yml``で表示をカスタマイズできます。
表示項目は``jb-book``（Jupyter Book）形式で設定します。
詳細は[Table of Contents - MyST](https://mystmd.org/guide/table-of-contents)を参照してください。

```yaml
format: jb-book
root: index
chapters:
  - title: Samples
    sections:
      - file: samples/0001
      - file: samples/0002
      - file: samples/0003
```
