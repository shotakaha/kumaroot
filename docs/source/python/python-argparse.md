# オプション解析したい（``argparse``）

```python
import argparse

def main() -> None:

    # ArgumentParserオブジェクトを作成
    parser = argparse.ArgumentParser()

    # 位置引数を追加
    parser.add_argument("url", help="URL")

    # オプション引数を追加
    parser.add_argument("--config", help="設定")
    parser.add_argument("--debug", help="デバッグ")

    # 引数／オプション設定を取得
    args = parser.parse_args()
    # args.url
    # args.config
    # args.debug

    if args.debug:
        # デバッグ設定

    return

if __name__ == "__main__":
    main()
```

``argparse``はPython標準のオプション解析モジュールです。
簡単かつ高機能にオプションを追加できます。

ヘルプドキュメントを書く代わりに、
スクリプトに追加しておくとよいと思います。
