import streamlit as st

st.set_page_config(
    page_title="Trustee Organizer",
    layout="wide"
)

GREEN = "#072E00"
BACKGROUND = "#F8F9F6"
BORDER = "#D9DED6"
MUTED = "#7A8575"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {BACKGROUND};
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}

        .main-title {{
            color: {GREEN};
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 4px;
        }}

        .subtitle {{
            color: {MUTED};
            font-size: 15px;
            margin-bottom: 24px;
        }}

        .card {{
            background-color: white;
            border: 1px solid {BORDER};
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            margin-bottom: 18px;
        }}

        .card-title {{
            color: {GREEN};
            font-size: 19px;
            font-weight: 700;
            margin-bottom: 14px;
        }}

        .card-text {{
            color: {GREEN};
            font-size: 15px;
            margin-bottom: 8px;
        }}

        .empty-space-small {{
            height: 80px;
        }}

        .empty-space-medium {{
            height: 180px;
        }}

        .empty-space-large {{
            height: 260px;
        }}

        div[data-testid="stHorizontalBlock"] {{
            gap: 1.25rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="main-title">Trustee Organizer</div>
    <div class="subtitle">Trust administration dashboard</div>
    """,
    unsafe_allow_html=True
)

# Top Row
col1, col2, col3 = st.columns([1, 2, 1])

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
            <div class="empty-space-small"></div>
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

# Middle Row
left, right = st.columns([2, 1])

with left:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Trusts</div>
            <div class="empty-space-large"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Upcoming Deadlines</div>
            <div class="empty-space-large"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Bottom Row
bottom_left, bottom_right = st.columns(2)

with bottom_left:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Recent Activity</div>
            <div class="empty-space-medium"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

with bottom_right:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Quick Actions</div>
            <div class="empty-space-medium"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
