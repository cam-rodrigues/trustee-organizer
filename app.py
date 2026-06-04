import streamlit as st

st.set_page_config(
    page_title="Trustee Organizer",
    layout="wide"
)

GREEN = "#072E00"

st.markdown(
    f"""
    <h1 style='color:{GREEN};'>
        Trustee Organizer
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------
# TOP ROW
# --------------------------

col1, col2, col3 = st.columns([1, 2, 1])

# Overview Box
with col1:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">Overview</h3>

            <p style="color:{GREEN};">
                Total Trusts
            </p>

            <p style="color:{GREEN};">
                Active Trusts
            </p>

            <p style="color:{GREEN};">
                Closed Trusts
            </p>
            """,
            unsafe_allow_html=True
        )

# Family Tree Box
with col2:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">
                Trust Family Tree
            </h3>

            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            """,
            unsafe_allow_html=True
        )

# Value Box
with col3:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">
                Account Value
            </h3>

            <p style="color:{GREEN};">
                Ending Value
            </p>
            """,
            unsafe_allow_html=True
        )

st.write("")

# --------------------------
# MIDDLE ROW
# --------------------------

left, right = st.columns([2, 1])

with left:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">
                Trusts
            </h3>

            <p style="color:{GREEN};">
                Select a trust to view its profile.
            </p>

            <br>
            <br>
            <br>
            <br>
            <br>
            """,
            unsafe_allow_html=True
        )

with right:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">
                Upcoming Deadlines
            </h3>

            <br>
            <br>
            <br>
            <br>
            <br>
            """,
            unsafe_allow_html=True
        )

st.write("")

# --------------------------
# BOTTOM ROW
# --------------------------

bottom_left, bottom_right = st.columns(2)

with bottom_left:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">
                Recent Activity
            </h3>

            <br>
            <br>
            <br>
            <br>
            """,
            unsafe_allow_html=True
        )

with bottom_right:
    with st.container(border=True):
        st.markdown(
            f"""
            <h3 style="color:{GREEN};">
                Quick Actions
            </h3>

            <br>
            <br>
            <br>
            <br>
            """,
            unsafe_allow_html=True
        )
