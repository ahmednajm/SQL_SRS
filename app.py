import streamlit as st
import pandas as pd
import io
import duckdb

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution = duckdb.query(answer).df()

st.write("""
# SQL SRS
Spaced Repetition System
SQL Practice
""")

with st.sidebar:
    Option = st.selectbox(
        "What would you like to review",
        ("Joins", "Group By", "Windows Functions"),
        index=None,
        placeholder="Select a theme...")
    st.write(f'you have selected {Option}')

st.header("enter your code:")
query = st.text_area(label="your SQL code here", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solutions"])
with tab2:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write('expected:')
    st.dataframe(solution)
with tab3:
    st.write(answer)
