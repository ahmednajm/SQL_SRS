# pylint: disable=missing-module-docstring

import duckdb
import streamlit as st

con = duckdb.connect(database='data/exercises_sql_tables.duckdb', read_only=False)

#solution_df = duckdb.query(ANSWER_STR).df()

st.write("""
# SQL SRS
Spaced Repetition System
SQL Practice
"""
         )

with st.sidebar:
    Theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "Group By", "window_functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write(f"you have selected {Theme}")
    exercise = con.execute(f" select * from memory_state where theme='{Theme}' ").df()
    st.write(exercise)

st.header("enter your code:")
query = st.text_area(label="your SQL code here", key="user_input")
# if query:
#    result = duckdb.sql(query).df()
#    st.dataframe(result)
#
#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError as e:
#        st.write("some columns are missing")
#
#    n_line_difference = result.shape[0] - solution_df.shape[0]
#    if n_line_difference != 0:
#        st.write(f"result has {n_line_difference} line difference with the solution_df")
#
# tab2, tab3 = st.tabs(["Tables", "Solutions"])
# with tab2:
#    st.write("Table: beverages")
#    st.dataframe(beverages)
#    st.write("Table: food_items")
#    st.dataframe(food_items)
#    st.write("expected:")
#    st.dataframe(solution_df)
# with tab3:
#    st.write(ANSWER_STR)
