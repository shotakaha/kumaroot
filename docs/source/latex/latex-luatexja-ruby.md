# ルビを振りたい（``luatexja-ruby``）

```latex
\ltjruby{素粒子}{そ|りゅう|し}
\ruby{素粒子}{そ|りゅう|し}
```

`luatexja-ruby`は[luatexja](./latex-luatexja.md)の拡張パッケージで、
日本語組版にルビを設定するパッケージです。
`ltruby`コマンドで、ルビの振り方を指定できます。

ルビ用のパッケージは他にもいろいろあるようですが、`luatexja-ruby`を使えばよさそうです。
`\ruby`コマンドが別パッケージで使われていない場合、`\ltjruby`コマンドのエイリアスとして使用できます。

## リファレンス

- ``texdoc luatexja-ruby``
