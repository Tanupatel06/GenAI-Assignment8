import streamlit as st

#For Displaying title
st.title("Price Calculator")

#For Getting Number as Input
price = st.number_input("Enter Product Price")

#For Getting Discount using Slider
discount = st.slider("Select Discount (%)",0,50)

#For Calculatiins
final_price = price - (price * discount / 100)

#For Displaying Final Price
st.success(f"Final Price :{final_price}")