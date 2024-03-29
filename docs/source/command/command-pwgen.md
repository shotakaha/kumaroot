# パスワード生成したい（``pwgen``）

```console
$ brew install pwgen
$ pwgen オプション 文字数 パスワード数
```

パスワードの使い回しは厳禁ですが、人間の頭で思いつくには限界があります。
そういったことは``pwgen``におまかせしましょう。

オプションを使ってパスワードに含まれる文字数を調整できます。

```console
$ pwgen -sB 20 1  # 完全ランダム / 似たような文字を除外
XKjYRCof4a4r4yWLkYqa

$ pwgen -y 20 1  # 特殊文字を含む
Ahf5TiaNg`ie2pi,shai
```

:::{note}

パスワードは**文字数を長くすること**が大切です。
近年はマシンのパワー（=GPUの性能）があがり、パスワードをクラックされる時間もどんどん短くなっています。
サービスで利用できる限界まで文字数を使いましょう。

・・・え？8文字までしか使えない？そんなサービスを使うのはやめましょう。

:::
