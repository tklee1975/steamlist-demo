import streamlit as st
import numpy as np
import pandas as pd

random_data = np.random.randn(10, 20)

dataframe = pd.DataFrame(random_data, 
                         columns=('col %d' % i for i in range(20)))

# Highlight the maximum value in each column
st.dataframe(dataframe.style.highlight_max(axis=1)) # axis=1 Row 
