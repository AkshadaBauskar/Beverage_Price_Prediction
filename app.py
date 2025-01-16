import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("best_model.pkl")

# Streamlit app setup
st.title("Beverage Price Prediction")
st.write("Predict the price range of a beverage based on user input.")

# Define encoding mappings for categorical variables
encoding_mappings = {
    'gender': {"Male": 0, "Female": 1, "Other": 2},
    'zone': {"Urban": 3, "Metro": 4, "Rural": 1, "Semi-Urban": 2},
    'occupation': {"Working Professional": 0, "Student": 1, "Entrepreneur": 2, "Retired": 3},
    'income_levels': {"<10L": 1, "> 35L": 5, "16L - 25L": 3, "10L - 15L": 2, "26L - 35L": 4},
    'consume_frequency(weekly)': {"0-2 times": 1, "3-4 times": 2, "5-7 times": 3},
    'current_brand': {"Newcomer": 0, "Established": 1},
    'preferable_consumption_size': {"Small (250 ml)": 1, "Medium (500 ml)": 2, "Large (1 L)": 3},
    'awareness_of_other_brands': {"0 to 1": 1, "2 to 4": 2, "above 4": 3},
    'reasons_for_choosing_brands': {"Price": 1, "Quality": 2, "Availability": 3, "Brand Reputation": 4},
    'flavor_preference': {"Traditional": 0, "Exotic": 1},
    'purchase_channel': {"Online": 0, "Retail Store": 1},
    'packaging_preference' : {"Simple" : 0, "Premium" :1 , "Eco-friendly": 2},
    'health_concerns': {"Low (Not very concerned)": 0, "Medium (Moderately health-conscious)": 1, "High (Very health-conscious)": 2},
    'typical_consumption_situations': {"Active (e.g., Sports, gym)": 0, "Social (e.g., Parties)": 1, "Casual (e.g., At home)": 2}
}

# Updated mapping predicted classes to actual price ranges in INR
price_range_mapping = {
    0: "50-100 INR",
    1: "101-150 INR",
    2: "151-200 INR",
    3: "200-250 INR"
}

# Input fields for user data
st.header("Input Beverage Characteristics")

# First Row - 4 Features
col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with col2:
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
with col3:
    zone = st.selectbox("Zone", options=['Urban', 'Metro', 'Rural', 'Semi-Urban'])
with col4:
    occupation = st.selectbox("Occupation", options=['Working Professional', 'Student', 'Entrepreneur', 'Retired'])

# Second Row - 4 Features
col5, col6, col7, col8 = st.columns(4)
with col5:
    income_levels = st.selectbox("Income Levels (in L)", options=['<10L', '> 35L', '16L - 25L', '10L - 15L', '26L - 35L'])
with col6:
    consume_freq = st.selectbox("Consume Frequency (weekly)", options=['3-4 times', '5-7 times', '0-2 times'])
with col7:
    current_brand = st.selectbox("Current Brand", options=['Newcomer', 'Established'])
with col8:
    preferable_consumption_size = st.selectbox("Preferable Consumption Size", options=['Medium (500 ml)', 'Large (1 L)', 'Small (250 ml)'])

# Third Row - 4 Features
col9, col10, col11, col12 = st.columns(4)
with col9:
    awareness_of_other_brands = st.selectbox("Awareness of Other Brands", options=['0 to 1', '2 to 4', 'above 4'])
with col10:
    reasons_for_choosing_brands = st.selectbox("Reasons for Choosing Brands", options=['Price', 'Quality', 'Availability', 'Brand Reputation'])
with col11:
    flavor_pref = st.selectbox("Flavor Preference", options=['Traditional', 'Exotic'])
with col12:
    purchase_channel = st.selectbox("Purchase Channel", options=['Online', 'Retail Store'])

# Fourth Row - 2 Features
col13, col14, col15 = st.columns(3)
with col13:
    packaging_preference = st.selectbox("Packaging Preference", options =['Simple', 'Premium', 'Eco-friendly'])
with col14:
    health_concerns = st.selectbox("Health Concerns", options=['Medium (Moderately health-conscious)', 'Low (Not very concerned)', 'High (Very health-conscious)'])
with col15:
    typical_consumption_situations = st.selectbox("Typical Consumption Situations", options=['Active (e.g., Sports, gym)', 'Social (e.g., Parties)', 'Casual (e.g., At home)'])

# Button for prediction
if st.button("Predict Price Range"):
    awareness = encoding_mappings['awareness_of_other_brands'][awareness_of_other_brands]
    frequency = encoding_mappings['consume_frequency(weekly)'][consume_freq]
    cf_ab_score = frequency / (awareness + frequency) if (awareness + frequency) != 0 else 0.001
    zas_score = encoding_mappings['zone'][zone] * encoding_mappings['income_levels'][income_levels]
    bsi = 1 if (encoding_mappings['current_brand'][current_brand] != 1 and encoding_mappings['reasons_for_choosing_brands'][reasons_for_choosing_brands] in [1, 2]) else 0

    user_data = pd.DataFrame({
        'age': [age],
        'gender': [encoding_mappings['gender'][gender]],
        'zone': [encoding_mappings['zone'][zone]],
        'occupation': [encoding_mappings['occupation'][occupation]],
        'income_levels': [encoding_mappings['income_levels'][income_levels]],
        'consume_frequency(weekly)': [frequency],
        'current_brand': [encoding_mappings['current_brand'][current_brand]],
        'preferable_consumption_size': [encoding_mappings['preferable_consumption_size'][preferable_consumption_size]],
        'awareness_of_other_brands': [awareness],
        'packaging_preference' : [packaging_preference]
    })

    user_data = pd.get_dummies(user_data)
    model_features = model.get_booster().feature_names
    user_data = user_data.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(user_data)
    readable_prediction = price_range_mapping.get(int(prediction[0]), "Unknown")
    st.success(f"Predicted Price Range: {readable_prediction}")