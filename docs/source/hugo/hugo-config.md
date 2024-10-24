# 設定ファイルしたい（`/config/環境名/`）

```txt
config
├── _default
│   ├── hugo.toml
│   ├── languages.en.toml
│   ├── languages.ja.toml
│   ├── menus.en.toml
│   ├── menus.ja.toml
│   └── params.toml
└── production
    └── hugo.toml
```

設定ファイルは、セクションごとにファイルを分割できます。
多言語したい場合、そのセクションの言語でファイルを作成すればよいので、簡単に対応できます。

また、環境ごとにディレクトリを分けることができます。
デフォルト設定（`config/_default/`）には常に読み込む設定を保存します。
環境ごとに上書きする設定は`config/環境名/`に保存します。

```{toctree}
---
maxdepth: 1
---

```

## 設定ファイルしたい（`hugo --config`）

```console
$ hugo --config 設定ファイル
$ hugo --config 設定ファイル1,設定ファイル2,設定ファイル3
```

`--config`オプションで設定ファイルのパスを変更できます。
複数の設定ファイルを指定したり、
ディレクトリを指定したりできます。
