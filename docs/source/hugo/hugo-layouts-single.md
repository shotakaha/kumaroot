# 単体ページしたい（``/layouts/_default/single.html``）

```html
{{ define "main" }}
<section>
    <article>
        <div>
            <!-- 記事のタイトル -->
            <!-- 記事の公開日 -->
            <!-- 記事にかかる時間 -->
        </div>
        <div>
            <!-- SNSボタン -->
        </div>
        <div>
            <!-- 記事本文 -->
        </div>
    </article>

    <div>
        <!-- 関連ページのリスト -->
    </div>

    <div>
        <!-- 関連サイトのリスト -->
    </div>

    <div>
        <!-- 前のページ -->
        <!-- 次のページ -->
    </div>
</section>
{{ end }}
```
