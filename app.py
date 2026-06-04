import streamlit as st

st.set_page_config(
    page_title="Trustee Operations System",
    layout="wide"
)

st.title("Trustee Operations System")

st.divider()

# Summary Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Trusts", "12")

with col2:
    st.metric("Active Trusts", "10")

with col3:
    st.metric("Closed Trusts", "2")

with col4:
    st.metric("Total Ending Value", "$24,850,000")

st.divider()

# Account Details
st.subheader("Account Details")

col1, col2 = st.columns(2)

with col1:
    st.text("Law Firm")
    st.text("G&B")

    st.text("Account Name")
    st.text("Alderman Accounts")

with col2:
    st.text("Primary Attorney")
    st.text("John Smith")

    st.text("Primary CPA")
    st.text("Jane Doe")

st.divider()

# Trust Summary
st.subheader("Trust Summary")

trust_data = [
    {
        "Trust ID": "12345678",
        "Trust Name": "William & Clarice Alderman IRR INS Trust",
        "Status": "Active",
        "Ending Value": "$4,235,000"
    },
    {
        "Trust ID": "87654321",
        "Trust Name": "Alderman Family Trust",
        "Status": "Active",
        "Ending Value": "$2,150,000"
    }
]

st.dataframe(
    trust_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Upcoming Deadlines
col1, col2 = st.columns(2)

with col1:
    st.subheader("Upcoming Deadlines")

    st.write("Annual Accounting - Due 12/31/2026")
    st.write("Beneficiary Notice - Due 07/15/2026")
    st.write("Tax Filing - Due 04/15/2027")

with col2:
    st.subheader("Recent Activity")

    st.write("06/04/2026 - Trust Updated")
    st.write("06/01/2026 - Distribution Processed")
    st.write("05/15/2026 - Annual Report Generated")
