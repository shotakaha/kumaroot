# 設定ファイルを分割したい（オススメ）

```txt
config
├── _default
        ├── hugo.toml
        ├── languages.en.toml
        ├── languages.ja.toml
        ├── menus.en.toml
        ├── menus.ja.toml
        └── params.toml
```

[前ページの設定ファイル](./hugo-config-hugo.md)は、セクションごとにファイルを分割できます。

準備する手間はかかりますが`/hugo.toml`にまとめるより、分割することをオススメします。
増築する可能性が少しでもあるならば強くオススメします。
