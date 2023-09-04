# インストールしたい

```console
$ brew install rust
$ brew list rust
/opt/homebrew/Cellar/rust/1.72.0_1/.bottle/etc/bash_completion.d/cargo
/opt/homebrew/Cellar/rust/1.72.0_1/bin/cargo
/opt/homebrew/Cellar/rust/1.72.0_1/bin/cargo-clippy
/opt/homebrew/Cellar/rust/1.72.0_1/bin/clippy-driver
/opt/homebrew/Cellar/rust/1.72.0_1/bin/rust-demangler
/opt/homebrew/Cellar/rust/1.72.0_1/bin/rust-gdb
/opt/homebrew/Cellar/rust/1.72.0_1/bin/rust-gdbgui
/opt/homebrew/Cellar/rust/1.72.0_1/bin/rust-lldb
/opt/homebrew/Cellar/rust/1.72.0_1/bin/rustc
/opt/homebrew/Cellar/rust/1.72.0_1/bin/rustdoc
...（省略）...

$ rustc --version
rustc 1.72.0 (5680fa18f 2023-08-23) (Homebrew)

$ cargo --version
cargo 1.72.0 (26bba4830 2023-08-26)
```

HomebrewでRustをインストールできます。
``brew install rust``をすると関連コマンドがインストールされます。
``rustup``はしなくてもよさそうですが、``$HOME/.cargo/bin``へのPATH設定が必要です。
