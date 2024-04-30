# タイトルしたい（``{{ .Title }}``）

/content/記事/index.md
:   ```toml
    title = "記事のタイトル"
    ```

/layouts/_default/single.html
:   ```go
    <h1>{{ .Title }}</h1>
    ```

/public/記事/index.html
:   ```html
    <h1>記事のタイトル</h1>
    ```

## Emojiしたい（``{{ .Title | emojify }}``）

/content/記事/index.md
:   ```toml
    title = "記事のタイトル :heart:"
    ```

/layouts/_default/single.html
:   ```go
    <h1>{{ .Title | emojify }}
    ```

/public/記事/index.html
:   ```html
    <h1>記事のタイトル 🩷</h1>
    ```
