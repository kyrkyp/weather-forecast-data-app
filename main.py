import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather forecast for the next days")
place = st.text_input("Enter a place to get the weather forecast: ")
days = st.slider(
    "Select the number of days for the forecast:",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} forecast for {place} for the next {days} days")

if place != "":
    try:
        filtered_data = get_data(place, days)
        
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            # Convert temperatures from Kelvin to Celsius
            temperatures = [temp - 273.15 for temp in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            weather_icons = {
                "Clear": "☀️",
                "Clouds": "☁️", 
                "Rain": "🌧️",
                "Snow": "❄️",
                "Drizzle": "🌦️",
                "Thunderstorm": "⛈️",
                "Mist": "🌫️",
                "Fog": "🌫️"
            }
            
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            
            cols = st.columns(min(len(sky_conditions), 8))
            for i, (condition, date) in enumerate(zip(sky_conditions, dates)):
                if i < len(cols):
                    with cols[i]:
                        icon = weather_icons.get(condition, "🌤️")
                        st.markdown(f"<div style='text-align: center'><h1>{icon}</h1><p>{condition}</p><small>{date.split()[0]}</small></div>", unsafe_allow_html=True)
    except Exception as e:
        error_message = str(e)
        if "doesn't exist" in error_message:
            st.error(f"🌍 {error_message}")
            st.info("💡 Please check the city name and try again.")
        else:
            st.error(f"⚠️ Error: {error_message}")
            st.info("🔄 Try again later.")