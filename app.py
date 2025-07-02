import streamlit as st
import pandas as pd
import joblib
import base64

# Function to set background image from local file
def set_bg_image(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call the function with your sky image
set_bg_image("Screenshot 2025-06-29 215641.png")


# Custom dark background style
st.markdown(
    """
    <style>
        /* Set background color and text color */
        .main {
            background-color: #1e1e2f;
            color: #f5f5f5;
        }

        /* Style the sidebar */
        .css-1d391kg, .css-1v0mbdj {
            background-color: #2c2f4a;
        }

        /* Style input boxes and buttons */
        .stTextInput > div > div > input,
        .stNumberInput input,
        .stSelectbox div div,
        .stButton > button {
            background-color: #333752;
            color: #ffffff;
            border: 1px solid #555;
        }

        .stButton > button {
            background-color: #4c84ff;
            color: white;
            font-weight: bold;
        }

        .stButton > button:hover {
            background-color: #355ac1;
        }

        /* Style headings */
        h1, h2, h3 {
            color: #f0f0f0;
        }

        /* Success message styling */
        .stMarkdown h2, .stSuccess {
            background-color: #3a3a50;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the trained model
model = joblib.load("rain_prediction_model.pkl")

# Title and layout setup
st.set_page_config(page_title="Rain Prediction App", layout="wide")
st.title("🌦️ Rain Tomorrow Prediction")
st.markdown("Fill in the weather data to predict if it will rain tomorrow.")

# Define categorical feature options
locations = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Hobart', 'Darwin']
wind_directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                   'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']

# Input layout using columns
col1, col2, col3 = st.columns(3)

with col1:
    location = st.selectbox("Location", locations)
    min_temp = st.number_input("MinTemp (°C)", value=10.0)
    max_temp = st.number_input("MaxTemp (°C)", value=25.0)
    rainfall = st.number_input("Rainfall (mm)", value=0.0)
    evaporation = st.number_input("Evaporation (mm)", value=5.0)
    sunshine = st.number_input("Sunshine (hrs)", value=6.0)

with col2:
    wind_gust_dir = st.selectbox("WindGustDir", wind_directions)
    wind_gust_speed = st.number_input("WindGustSpeed (km/h)", value=35.0)
    wind_dir_9am = st.selectbox("WindDir9am", wind_directions)
    wind_dir_3pm = st.selectbox("WindDir3pm", wind_directions)
    wind_speed_9am = st.number_input("WindSpeed9am (km/h)", value=15.0)
    wind_speed_3pm = st.number_input("WindSpeed3pm (km/h)", value=20.0)

with col3:
    humidity_9am = st.number_input("Humidity9am (%)", value=65.0)
    humidity_3pm = st.number_input("Humidity3pm (%)", value=50.0)
    pressure_9am = st.number_input("Pressure9am (hPa)", value=1012.0)
    pressure_3pm = st.number_input("Pressure3pm (hPa)", value=1010.0)
    cloud_9am = st.slider("Cloud9am (oktas)", 0, 9, 4)
    cloud_3pm = st.slider("Cloud3pm (oktas)", 0, 9, 5)
    temp_9am = st.number_input("Temp9am (°C)", value=18.0)
    temp_3pm = st.number_input("Temp3pm (°C)", value=24.0)
    rain_today = st.selectbox("RainToday", ['No', 'Yes'])

# Encode categorical variables manually for now
encoded_location = locations.index(location)
encoded_gust_dir = wind_directions.index(wind_gust_dir)
encoded_dir_9am = wind_directions.index(wind_dir_9am)
encoded_dir_3pm = wind_directions.index(wind_dir_3pm)
encoded_rain_today = 1 if rain_today == "Yes" else 0

# Make prediction
if st.button("🌧️ Predict Rain Tomorrow"):
    input_data = pd.DataFrame({
        'Location': [encoded_location],
        'MinTemp': [min_temp],
        'MaxTemp': [max_temp],
        'Rainfall': [rainfall],
        'Evaporation': [evaporation],
        'Sunshine': [sunshine],
        'WindGustDir': [encoded_gust_dir],
        'WindGustSpeed': [wind_gust_speed],
        'WindDir9am': [encoded_dir_9am],
        'WindDir3pm': [encoded_dir_3pm],
        'WindSpeed9am': [wind_speed_9am],
        'WindSpeed3pm': [wind_speed_3pm],
        'Humidity9am': [humidity_9am],
        'Humidity3pm': [humidity_3pm],
        'Pressure9am': [pressure_9am],
        'Pressure3pm': [pressure_3pm],
        'Cloud9am': [cloud_9am],
        'Cloud3pm': [cloud_3pm],
        'Temp9am': [temp_9am],
        'Temp3pm': [temp_3pm],
        'RainToday': [encoded_rain_today]
    })

    try:
        prediction = model.predict(input_data)[0]
        result = "🌧️ Yes, it will rain tomorrow." if prediction == 1 else "☀️ No, it won't rain tomorrow."
        st.subheader("Prediction Result")
        st.success(result)
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
