import streamlit as st

st.write("""
# SQL SRS
Spaced Repetition System
SQL Practice
""")

Option = st.selectbox(
    "What would you like to review",
    ("Joins", "Group By", "Windows Functions"),
    index=None,
    placeholder="Select a theme...",
)

st.write(f'you have selected {Option}')

data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
df = pd.DataFrame(data)


