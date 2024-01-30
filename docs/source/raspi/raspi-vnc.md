# VNCしたい

``Raspberry Pi Configuration``でVNCを有効にします。

## RealVNCしたい

``Bookworm（Debian 12）``より前のRaspberry Pi OSではデフォルトの画面共有ソフトは``RealVNC``でした。
macOS標準のVNC（Finder.appからVNC接続）を使うと、VNCのバージョンが不一致というエラーが表示される（はずな）ので、以下のようにRealVNCの設定を変更してください。

1. {guilabel}`Security` -> {guilabel}`Encription`: ``Prefer off``
2. {guilabel}`Authentication`: `VNC password`
3. {guilabel}`Users & Permissions`: `Standard User`のパスワードを設定
