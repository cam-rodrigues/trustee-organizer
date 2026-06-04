import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("Trustee Organizer")

st.divider()

# Top 4 Boxes
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.subheader("Total Trusts")
        st.write(" ")

with col2:
    with st.container(border=True):
        st.subheader("Active Trusts")
        st.write(" ")

with col3:
    with st.container(border=True):
        st.subheader("Closed Trusts")
        st.write(" ")

with col4:
    with st.container(border=True):
        st.subheader("Ending Value")
        st.write(" ")

st.write("")

# Middle Row
left, right = st.columns([2, 1])

with left:
    with st.container(border=True):
        st.subheader("Trust Family Tree")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

with right:
    with st.container(border=True):
        st.subheader("Upcoming Deadlines")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

st.write("")

# Bottom Row
bottom_left, bottom_right = st.columns(2)

with bottom_left:
    with st.container(border=True):
        st.subheader("Recent Activity")
        st.write(" ")
        st.write(" ")
        st.write(" ")

with bottom_right:
    with st.container(border=True):
        st.subheader("Quick Actions")
        st.write(" ")
        st.write(" ")
        st.write(" ")
