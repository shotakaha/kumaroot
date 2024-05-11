# Page Variables


| ページ階層 | コンテンツ | テンプレート | パーマリンク | ``.IsHome`` | ``.IsNode`` | ``.IsPage`` | ``.IsSection`` | ``.Kind`` |
|---|---|---|---|---|---|---|---|---|
| トップページ | ``/content/_index.md`` | ``/layouts/index.html`` | ``/`` | ``true`` | ``true`` | | | ``home`` |
| カスタム404 | | ``/layouts/404.html`` | ``/404.html`` | | ``true`` | | | ``404`` |
| セクション | ``/content/sec/_index.md`` | ``/layouts/_default/list.html`` | ``/sec/`` | | ``true`` | | ``true`` | ``section`` |
| サブセクション | ``/content/sec/sub/_index.md`` | ``/layouts/_default/list.html`` | ``/sec/sub/`` | | ``true`` | | ``true`` | ``section`` |
| 記事リスト | ``/content/posts/_index.md`` | ``/layouts/_default/list.html`` | ``/posts/`` | | ``true`` | | ``true`` | ``section`` |
| 記事 | ``/content/posts/first_post.md`` | ``/layouts/_default/single.html`` |``/posts/first_post/`` | | | ``true`` | | ``page`` |
| 記事 | ``/content/posts/release/awesome_release.md`` | ``/layouts/_default/single.html`` | ``/posts/resease/awesome_release/`` | | | ``true`` | | ``page`` |
| タクソノミー名 | (fromtmatter) | ``/layouts/_default/確認する.html`` | ``/tags/`` | | ``true`` | | | ``taxonomy`` |
| タクソノミー | (frontmatter) | ``/layouts/_default/確認する.html`` | ``/tags/タグ名`` | | ``true`` | | | ``term`` |




https://gohugo.io/variables/page/
