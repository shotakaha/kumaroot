# Wordしたい（``myst build --docx``）

```yaml
---
exports:
  - format: docx
    output: exports/ファイル名.docx
---
```

PDF形式で出力したいページのフロントマターに``format: docx``を指定します。
出力ファイル名はオプションです。

```console
$ myst build --docx
```


[Exporting to Word](https://myst-tools.org/docs/mystjs/creating-word-documents)
