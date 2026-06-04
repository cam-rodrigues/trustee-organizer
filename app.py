import streamlit as st

st.set_page_config(
    page_title="Trustee Organizer",
    layout="wide"
)

GREEN = "#072E00"
LIGHT_BG = "#F8F9F6"
BORDER = "#D9DED6"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {LIGHT_BG};
        }}

        .main-title {{
            color: {GREEN};
            font-size: 38px;
            font-weight: 700;
            margin-bottom: 0px;
        }}

        .subtitle {{
            color: {GREEN};
            font-size: 15px;
            margin-bottom: 25px;
        }}

        .card {{
            background-color: white;
            border: 1px solid {BORDER};
            border-radius: 14px;
            padding: 22px;
            min-height: 160px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
        }}

        .large-card {{
            min-height: 360px;
        }}

        .medium-card {{
            min-height: 260px;
        }}

        .card-title {{
            color: {GREEN};
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 18px;
        }}

        .card-text {{
            color: {GREEN};
            font-size: 15px;
            margin-bottom: 10px;
        }}

        .placeholder {{
            color: #8A9585;
            font-size: 14px;
            margin-top: 20px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="main-title">Trustee Organizer</div>
    <div class="subtitle">Trust administration dashboard</div>
    """,
    unsafe_allow_html=True
)

# Top Row
col1, col2, col3 = st.columns([1.1, 2.2, 1.1], gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Overview</div>
            <div class="card-text">Total Trusts</div>
            <div class="card-text">Active Trusts</div>
            <div class="card-text">Closed Trusts</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Trust Family Tree</div>
            <div class="placeholder">Relationship map will appear here.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Account Value</div>
            <div class="card-text">Ending Value</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# Middle Row
left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown(
        """
        <div class="card large-card">
            <div class="card-title">Trusts</div>
            <div class="placeholder">Trust list will appear here.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        """
        <div class="card large-card">
            <div class="card-title">Upcoming Deadlines</div>
            <div class="placeholder">Deadlines will appear here.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# Bottom Row
bottom_left, bottom_right = st.columns(2, gap="large")

with bottom_left:
    st.markdown(
        """
        <div class="card medium-card">
            <div class="card-title">Recent Activity</div>
            <div class="placeholder">Activity log will appear here.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with bottom_right:
    st.markdown(
        """
        <div class="card medium-card">
            <div class="card-title">Quick Actions</div>
            <div class="placeholder">Action buttons will appear here.</div>
        </div>
        """,
        unsafe_allow_html=True
    )
