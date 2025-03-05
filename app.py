
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom CSS for black background and stylish headings
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: black;
        color: white;
    }
    h2 {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #ff4757;
    }
    h3 {
        text-align: center;
        font-size: 24px;
        color: #ffa502;
    }
    .stSelectbox, .stNumberInput, .stButton>button {
        width: 100%;
        font-size: 18px;
    }
    .stButton>button {
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s ease-in-out;
        background-color: #ff4757;
        color: white;
    }
    .stButton>button:hover {
        background-color: #ff6b81 !important;
    }
    </style>
""", unsafe_allow_html=True)

# App Heading
st.markdown("<h2>Unit Converter</h2>", unsafe_allow_html=True)
st.markdown("<h3>Convert Length, Weight, and Time Instantly</h3>", unsafe_allow_html=True)
st.write("Welcome! Select a category to get started.")

# Categories for conversion
category = st.selectbox("Select a category:", ["Length", "Weight", "Time"])

# Conversion logic
def convert_units(value, unit_from, unit_to, conversion_dict):
    return value * conversion_dict[unit_from] / conversion_dict[unit_to]

if category == "Length":
    st.subheader("Convert Length")
    units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
elif category == "Weight":
    st.subheader("Convert Weight")
    units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
else:
    st.subheader("Convert Time")
    units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400}

# User input fields
value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
unit_from = st.selectbox("From:", list(units.keys()))
unit_to = st.selectbox("To:", list(units.keys()))

# Convert button
if st.button("Convert"):
    if value > 0:
        result = convert_units(value, unit_from, unit_to, units)
        st.success(f"{value} {unit_from} = {result:.4f} {unit_to}")
    else:
        st.warning("Please enter a value greater than zero!")

# Footer
st.markdown("<h4 style='text-align: center; color: #ff4757;'>Made with ❤️ by Rehana Ali</h4>", unsafe_allow_html=True)
