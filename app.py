import streamlit as st

st.set_page_config(
    page_title="Trustee Organizer",
    layout="wide"
)

st.title("Dashboard")

# Top Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.container(border=True, height=120)

with col2:
    st.container(border=True, height=120)

with col3:
    st.container(border=True, height=120)

with col4:
    st.container(border=True, height=120)

st.write("")

# Middle Row
left, right = st.columns([2, 1])

with left:
    st.container(border=True, height=400)

with right:
    st.container(border=True, height=400)

st.write("")

# Bottom Row
col1, col2 = st.columns(2)

with col1:
    st.container(border=True, height=300)

with col2:
    st.container(border=True, height=300)
