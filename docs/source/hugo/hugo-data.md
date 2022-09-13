# カスタムデータを読み込みたい（``/data/``）

```bash
/data/データ.toml
/themes/テーマ名/data/データ.toml
```

テンプレートやショートコードにカスタムデータを読み込ませる場合は
``/data/``ディレクトリにデータを保存します。
これらのデータは``.Site.Data.ファイル名``でアクセスできます。
対応しているデータ形式は``YAML`` / ``JSON`` / ``TOML``です。

```html
{{ range $.Site.Data.ファイル名 }}
<ul>
    {{ range .カラム名 }}
    <li>{{ . }}</li>
    {{ end }}
</ul>
{{ end }}
```

## CSVを読みこみたい

CSVファイルを読み込む場合は``getCSV``を使います。
データは``/data/``以外のディレクトリに保存する必要があります。

## リファレンス

- [Data Templates](https://gohugo.io/templates/data-templates/)
