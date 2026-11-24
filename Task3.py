import streamlit as st

#Display the main heading
st.title("Product Entry Form")

#Display heading in sidebar
st.sidebar.header("Product Details")

#Accept product name
product_name = st.text_input("Enter Product Name")

#Accept product price
product_price = st.number_input("Enter Product Price")

#Select product category
category = st.selectbox( "Select Category", ["Electronics", "Clothing", "Food", "Other"] )

#Create submit button
if st.button("Submit Product"): 
    st.success("Product Added Successfully!")