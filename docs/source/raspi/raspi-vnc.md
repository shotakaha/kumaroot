# VNCしたい

デスクトップの設定からVNCを有効にします。

1. {guilabel}`Preferences` → {guilabel}`Raspberry Pi Configuration`を選択する
2. {guilabel}`Interface`タブを選択する
3. {guilabel}`VNC`のトグルボタンを有効にする

## WayVNCしたい

``Bookworm（Debian 12）``ではデフォルトの画面共有ツールが``wayvnc``になりました。

## RealVNCしたい

``Bookworm（Debian 12）``より前は、デフォルトの画面共有ソフトは``RealVNC``でした。
macOS標準のVNC（Finder.appからVNC接続）を使うと、VNCのバージョンが不一致というエラーが表示される（はずな）ので、以下のようにRealVNCの設定を変更してください。

1. {guilabel}`Security` -> {guilabel}`Encription`: ``Prefer off``
2. {guilabel}`Authentication`: `VNC password`
3. {guilabel}`Users & Permissions`: `Standard User`のパスワードを設定
