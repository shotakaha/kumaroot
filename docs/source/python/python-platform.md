# バージョン情報したい（`platform`）

```python
import platform

# OS情報
platform.version()

# アーキテクチャ情報
platform.platform()

# Python情報
platform.sys.version()
platform.sys.executable()
```

`platform`モジュールで、実行環境のバージョンを確認できます。
`platform`の中で`sys`や`os`モジュールをインポートしているため、
それらのモジュールがもつメソッド／変数にもアクセスできます。
