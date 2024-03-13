# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""
solution_df = duckdb.query(ANSWER_STR).df()

st.write(
    """
# SQL SRS
Spaced Repetition System
SQL Practice
"""
)

with st.sidebar:
    Option = st.selectbox(
        "What would you like to review",
        ("Joins", "Group By", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write(f"you have selected {Option}")

st.header("enter your code:")
query = st.text_area(label="your SQL code here", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("some columns are missing")

    n_line_difference = result.shape[0] - solution_df.shape[0]
    if n_line_difference != 0:
        st.write(f"result has {n_line_difference} line difference with the solution_df")

tab2, tab3 = st.tabs(["Tables", "Solutions"])
with tab2:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)
with tab3:
    st.write(ANSWER_STR)
