import streamlit as st

#Title and Description
st.title("Simple Sales Dashboard")
st.write("This dashboard displays monthly sales data.")

#List of months
months = ["January", "February", "March", "April"]

#Dictionary of monthly sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

#Select a month
selected_month = st.selectbox("Select a Month", months)

#Display selected month's sales
st.metric("Monthly Sales", sales[selected_month])

#Display bar chart
st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))