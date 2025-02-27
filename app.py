import streamlit as st
import time

# function to calculate bmi
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# function to categorize bmi
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight 😟"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight 😊"
    elif 25 <= bmi < 29.9:
        return "Overweight 🤔"
    else:
        return "Obesity ⚠️"

# streamlit app layout
def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
    st.markdown(
        """
        <style>
        /* Apply background color to the entire app */
        .stApp {
            background-color: #dfe6e9;
        }

        /* Style for the sidebar */
        .css-1lcbmhc {
            background-color: #2d3436;
        }

        /* Style for the title and main content */
        .css-18e3th9 {
            background-color: FFFFFF;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # title & description
    st.title("BMI Calculator 💪")
    st.write("This app calculates your Body Mass Index (BMI) and shows your weight category based on the result. 🚀")

    # input fields
    st.sidebar.header("Enter your details 👇")
    weight = st.sidebar.number_input("Weight in (kg) ⚖️", min_value=1.0, step=0.1)
    height = st.sidebar.number_input("Height in (m) 📏", min_value=0.1, step=0.01)

    # calculate bmi & categorize
    if st.sidebar.button("Calculate BMI 😎"):
        st.subheader("Calculating BMI...")

        # Progress bar animation
        progress = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.03)  # Simulate some delay
            progress.progress(percent_complete + 1)

        # Perform BMI calculation after animation
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        # Display Results
        st.subheader("Result 📝:")
        st.header("Your BMI is:")
        st.write(f"{bmi:.2f} 📊")

        st.header("Weight Category:")
        st.write(category)

        # Suggestion based on category
        if category == "Underweight 😟":
            st.warning("You are underweight. Consider consulting a healthcare provider. 💡")
        elif category == "Normal weight 😊":
            st.success("You have a normal body weight. Keep up the good work! 👍")
        elif category == "Overweight 🤔":
            st.warning("You are slightly overweight. Try adopting a healthier lifestyle. 🏋️‍♂️")
        else:
            st.error("You are in the obesity range. Please seek medical advice. 🚨")

    # Footer
    st.markdown("---")
    st.markdown(f"Made by 😍[Kiran Wahid](https://github.com/kiranwahid/python-bmicalculator-project08)")

main()
