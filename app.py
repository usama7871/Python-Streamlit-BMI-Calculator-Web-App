# prompt: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes, 

import streamlit as st

def calculate_bmi(weight, height):
    """Calculates the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def main():
    """Main function for the Streamlit app."""
    bmi_history = []  # List to store BMI history

    """Main function for the Streamlit app."""
    st.title("BMI Calculator")

    unit = st.selectbox("Select unit:", ["Metric (kg, m)", "Imperial (lbs, in)"])
    
    if unit == "Imperial (lbs, in)":
        weight = st.number_input("Enter your weight in pounds:", min_value=0.0)
        height = st.number_input("Enter your height in inches:", min_value=0.0)
        weight_kg = weight * 0.453592
        height_m = height * 0.0254
    else:
        weight = st.number_input("Enter your weight in kilograms:", min_value=0.0)
        height = st.number_input("Enter your height in meters:", min_value=0.0)
        weight_kg = weight
        height_m = height

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight_kg, height_m)
            st.write(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 25:
                st.write("You are in a healthy weight range.")
            elif 25 <= bmi < 30:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
        else:
            st.write("Please enter valid weight and height values.")

    st.write("BMI Categories:")
    st.bar_chart({
        "Underweight": 18.5,
        "Healthy": 24.9,
        "Overweight": 29.9,
        "Obese": 30
    })

if __name__ == "__main__":
    main()
