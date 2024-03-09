import duckdb
import pandas as pd
import streamlit as st

st.write('hello world')

data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
df = pd.DataFrame(data)

sql_query = st.text_area(label='Enter your query')
st.write(f'you have entered the following query : {sql_query}')

result = duckdb.query(sql_query).df()
st.write(result)

