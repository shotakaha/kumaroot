# ボタンしたい（``st.button``）

```python
submit = st.button("送信")
```

``st.button``でウェブアプリにボタンを配置します。
引数はボタンのラベル名です。
ボタンを押すと返り値が``True``になります。

## 送信ボタンしたい（``st.form_submit_button``）

```python
with st.form(key="フォームの名前"):
    name = st.text_input("名前")

    submit = st.form_submit_button("送信")
    cancel = st.form_submit_button("キャンセル")

    if submit:
        st.text(f"名前：{name}")
```

入力エリアからフォーカスがはずれると自動でリロードされます。
``st.form``のコンテキスト内に配置すると自動リロードを無効にできます。
