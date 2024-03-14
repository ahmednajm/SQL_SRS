# pylint: disable=missing-module-docstring
import ast

import duckdb
import streamlit as st

con = duckdb.connect(database='data/exercises_sql_tables.duckdb', read_only=False)

#solution_df = duckdb.query(ANSWER_STR).df()

st.text("""
######  SQL SRS  ######
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

st.header("Enter your code:")
query = st.text_area(label="",
                     key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)
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
tab2, tab3 = st.tabs(["Tables", "Solutions"])
with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f'table : {table}')
        table_df = con.execute(f'select * from {table}').df()
        st.write(table_df)
with tab3:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.text(answer)
