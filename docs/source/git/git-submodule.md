# サブモジュールしたい（``git submodule``）

```console
$ git submodule add リポジトリURL ディレクトリ名
```

``git submodule``で外部リポジトリを、自分のリポジトリのサブディレクトリに配置できます。
ウェブサイトのテーマなど、自分では手を加えないけれど、参照したい場合などに使います。

```console
$ git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
$ git status
new file: .gitmodules
new file: themes/ananke

$ git diff --cached
diff --git a/.gitmodules b/.gitmodules
new file mode 100644
index 0000000..5154615
--- /dev/null
+++ b/.gitmodules
@@ -0,0 +1,3 @@
+[submodule "themes/ananke"]
+       path = themes/ananke
+       url = https://github.com/theNewDynamic/gohugo-theme-ananke.git
diff --git a/themes/ananke b/themes/ananke
new file mode 160000
index 0000000..c086834
--- /dev/null
+++ b/themes/ananke
@@ -0,0 +1 @@
+Subproject commit c086834f0ebfa39b8b6b0cfed010588a6907a91c
```
