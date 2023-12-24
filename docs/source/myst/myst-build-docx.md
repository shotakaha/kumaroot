# Wordしたい（``myst build --docx``）

```yaml
---
exports:
  - format: docx
    output: exports/ファイル名.docx
---
```

PDF形式で出力したいページのフロントマターに``format: docx``を指定します。
出力ファイル名（``output:``）は省略可能です。

```console
$ myst build --docx
```

ファイルは{file}`_build/exports/`に生成されます。


[Exporting to Word](https://myst-tools.org/docs/mystjs/creating-word-documents)
