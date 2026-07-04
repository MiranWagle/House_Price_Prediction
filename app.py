
import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="centered"
)

model = joblib.load("house_price_model.pkl")
feature_names = joblib.load("feature_names.pkl")


st.title("🏡 House Price Prediction")
st.markdown(
    "Enter the house details below to predict the estimated selling price."
)

st.divider()

area = st.number_input(
    "Area (Square Feet)",
    min_value=500,
    max_value=20000,
    value=5000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

stories = st.number_input(
    "Stories",
    min_value=1,
    max_value=5,
    value=2
)

mainroad = st.selectbox(
    "Main Road",
    ["Yes", "No"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["Yes", "No"]
)

basement = st.selectbox(
    "Basement",
    ["Yes", "No"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["Yes", "No"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["Yes", "No"]
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=10,
    value=1
)


furnishing = st.selectbox(
    "Furnishing Status",
    [
        "Semi-Furnished",
        "Unfurnished"
    ]
)


mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0

semi_furnished = 1 if furnishing == "Semi-Furnished" else 0
unfurnished = 1 if furnishing == "Unfurnished" else 0

input_data = pd.DataFrame([{
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "parking": parking,
    "furnishingstatus_semi-furnished": semi_furnished,
    "furnishingstatus_unfurnished": unfurnished
}])


input_data = input_data[feature_names]



if st.button("Predict House Price"):

    prediction = model.predict(input_data)[0]

    st.success("Prediction Successful!")

    st.metric(
        label="Estimated House Price",
        value=f"₹ {prediction:,.2f}"
    )

    st.info(
        "The predicted price is based on the Linear Regression model trained on the housing dataset."
    )