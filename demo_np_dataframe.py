import streamlit as st
import numpy as np

random_data = np.random.randn(10, 20)


st.write("Table with DataFrame:")
st.dataframe(random_data)
# df or simply call `df`