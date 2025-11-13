# GPG鍵したい

```console
// GPG鍵ペアの確認
$ gpg --list-keys

// GPG鍵ペアの生成
$ gpg --full-generate-key
```

`gpg`コマンドでGPG鍵（公開鍵と秘密鍵のペア）を生成できます。
GPG鍵やファイルの暗号化や送信メールの署名などに利用できます。
また、追加の設定でSSH鍵として利用することもできます。

:::{seealso}

## GnuPGとPGP

GnuPG（GNU Privacy Guard）と
PGP（Pretty Good Privacy）は、
名前が似ていて混同しやすいですが、両者には以下のような歴史的な関係があります。

PGP（Pretty Good Privacy）は1991年に開発された個人向けの暗号化・署名用ツールで、当初は商用ソフトとして提供されました。
その技術をベースに、1997年に暗号化・署名の標準仕様としてOpenPGPが策定されました。

GnuPG（GNU Privacy Guard）は
このOpenPGPに準拠した完全オープンソースの実装として
1999年に登場しました。
GnuPGはLinuxなどで広く使われており、現在のデファクトスタンダードになっています。

つまり、GnuPG（GNU Privacy Guard）を使っておけばOKということです。

:::
