import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})


st.write("Table with DataFrame:")
st.write(df)
# df or simply call `df`