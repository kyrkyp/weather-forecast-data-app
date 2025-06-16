import streamlit as st


st.title("Weather forecast for the next days")
place = st.text_input("Enter a place to get the weather forecast: ")
days = st.slider(
    "Select the number of days for the forecast:",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} forecast for {place} for the next {days} days")