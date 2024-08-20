# 画面分割したい（``st.columns``）

```python
# 2分割
col1, col2 = st.columns(2)

# 3分割
col1, col2, col3 = st.columns(3)

with col1:
    st.title("カラム1")

with col2:
    st.title("カラム2")

with col3:
    st.title("カラム3")
```

``st.columns``で縦分割できます。
引数に分割数を指定します。
