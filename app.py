import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Loan Search & Comparison",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏦 Loan Search & Comparison")
st.write(
    "Search and compare Home Loans, Car Loans and Personal Loans "
    "with important loan details."
)

st.divider()

# --------------------------------------------------
# LOAN DATA
# --------------------------------------------------

loans = [

    # ---------------- HOME LOANS ----------------

    {
        "Loan Type": "Home Loan",
        "Bank": "State Bank of India (SBI)",
        "Interest Rate": "7.25% - 8.70%",
        "Loan Purpose": "Purchase / Construction / Renovation of Home",
        "Tenure": "Up to 30 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per SBI scheme",
        "Policybazaar Link":
            "https://www.policybazaar.com/home-loan/",
        "Official Bank Link":
            "https://homeloans.sbi/"
    },

    {
        "Loan Type": "Home Loan",
        "Bank": "Bank of India",
        "Interest Rate": "7.10% - 10.25%",
        "Loan Purpose": "Purchase / Construction of Home",
        "Tenure": "Up to 30 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/home-loan/",
        "Official Bank Link":
            "https://bankofindia.co.in/"
    },

    {
        "Loan Type": "Home Loan",
        "Bank": "Canara Bank",
        "Interest Rate": "7.15% - 10.00%",
        "Loan Purpose": "Home Purchase / Construction",
        "Tenure": "Up to 30 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/home-loan/",
        "Official Bank Link":
            "https://canarabank.com/"
    },

    {
        "Loan Type": "Home Loan",
        "Bank": "Punjab National Bank (PNB)",
        "Interest Rate": "7.20% - 9.00%",
        "Loan Purpose": "Purchase / Construction / Repair",
        "Tenure": "Up to 30 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/home-loan/",
        "Official Bank Link":
            "https://www.pnbindia.in/"
    },

    {
        "Loan Type": "Home Loan",
        "Bank": "Axis Bank",
        "Interest Rate": "8.00% - 11.90%",
        "Loan Purpose": "Purchase / Construction / Balance Transfer",
        "Tenure": "Up to 30 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/home-loan/",
        "Official Bank Link":
            "https://www.axisbank.com/"
    },

    # ---------------- CAR LOANS ----------------

    {
        "Loan Type": "Car Loan",
        "Bank": "State Bank of India (SBI)",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "Purchase of New / Used Car",
        "Tenure": "Up to 7 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per SBI policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/car-loan/",
        "Official Bank Link":
            "https://sbi.co.in/"
    },

    {
        "Loan Type": "Car Loan",
        "Bank": "HDFC Bank",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "Purchase of New / Used Car",
        "Tenure": "Up to 7 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/car-loan/",
        "Official Bank Link":
            "https://www.hdfcbank.com/"
    },

    {
        "Loan Type": "Car Loan",
        "Bank": "ICICI Bank",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "New / Used Car Purchase",
        "Tenure": "Up to 7 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/car-loan/",
        "Official Bank Link":
            "https://www.icicibank.com/"
    },

    {
        "Loan Type": "Car Loan",
        "Bank": "Axis Bank",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "New / Used Car Purchase",
        "Tenure": "Up to 7 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/car-loan/",
        "Official Bank Link":
            "https://www.axisbank.com/"
    },

    # ---------------- PERSONAL LOANS ----------------

    {
        "Loan Type": "Personal Loan",
        "Bank": "HDFC Bank",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "Medical / Education / Travel / Personal Expenses",
        "Tenure": "Up to 5 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/personal-loan/",
        "Official Bank Link":
            "https://www.hdfcbank.com/"
    },

    {
        "Loan Type": "Personal Loan",
        "Bank": "ICICI Bank",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "Personal / Medical / Education / Travel",
        "Tenure": "Up to 7 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/personal-loan/",
        "Official Bank Link":
            "https://www.icicibank.com/"
    },

    {
        "Loan Type": "Personal Loan",
        "Bank": "Axis Bank",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "Personal Expenses / Emergency / Travel",
        "Tenure": "Up to 5 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per bank policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/personal-loan/",
        "Official Bank Link":
            "https://www.axisbank.com/"
    },

    {
        "Loan Type": "Personal Loan",
        "Bank": "State Bank of India (SBI)",
        "Interest Rate": "Check current rate",
        "Loan Purpose": "Personal Expenses / Education / Medical",
        "Tenure": "Up to 7 years",
        "Eligibility": "Salaried / Self-employed",
        "Processing Fee": "As per SBI policy",
        "Policybazaar Link":
            "https://www.policybazaar.com/personal-loan/",
        "Official Bank Link":
            "https://sbi.co.in/"
    }
]

# --------------------------------------------------
# CREATE DATAFRAME
# --------------------------------------------------

df = pd.DataFrame(loans)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("🔍 Search Loan")

loan_type = st.sidebar.selectbox(
    "Select Loan Type",
    [
        "All Loans",
        "Home Loan",
        "Car Loan",
        "Personal Loan"
    ]
)

search_bank = st.sidebar.text_input(
    "Search Bank"
)

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------

result = df.copy()

if loan_type != "All Loans":
    result = result[
        result["Loan Type"] == loan_type
    ]

if search_bank:
    result = result[
        result["Bank"].str.contains(
            search_bank,
            case=False,
            na=False
        )
    ]

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Loans",
        len(result)
    )

with col2:
    st.metric(
        "Loan Types",
        result["Loan Type"].nunique()
    )

with col3:
    st.metric(
        "Banks/Lenders",
        result["Bank"].nunique()
    )

st.divider()

# --------------------------------------------------
# DISPLAY RESULT
# --------------------------------------------------

if len(result) > 0:

    st.subheader("📋 Available Loan Details")

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No loan found for the selected search."
    )

# --------------------------------------------------
# DETAILED VIEW
# --------------------------------------------------

st.divider()

st.subheader("🔎 View Individual Loan")

if len(result) > 0:

    selected_bank = st.selectbox(
        "Select Bank",
        result["Bank"].unique()
    )

    selected_data = result[
        result["Bank"] == selected_bank
    ].iloc[0]

    st.write(
        f"### {selected_data['Bank']} - "
        f"{selected_data['Loan Type']}"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.write(
            "**Interest Rate:**",
            selected_data["Interest Rate"]
        )

        st.write(
            "**Loan Purpose:**",
            selected_data["Loan Purpose"]
        )

        st.write(
            "**Tenure:**",
            selected_data["Tenure"]
        )

        st.write(
            "**Eligibility:**",
            selected_data["Eligibility"]
        )

    with c2:

        st.write(
            "**Processing Fee:**",
            selected_data["Processing Fee"]
        )

        st.link_button(
            "🌐 Policybazaar",
            selected_data["Policybazaar Link"]
        )

        st.link_button(
            "🏦 Official Bank Website",
            selected_data["Official Bank Link"]
        )

# --------------------------------------------------
# EXCEL DOWNLOAD
# --------------------------------------------------

st.divider()

st.subheader("📥 Download Loan Data")

excel_data = result.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Loan Data as CSV",
    data=excel_data,
    file_name="loan_details.csv",
    mime="text/csv"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Loan rates and eligibility are indicative. "
    "Always verify the latest terms with the lender before applying."
  )
