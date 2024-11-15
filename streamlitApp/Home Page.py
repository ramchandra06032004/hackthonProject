import streamlit as st

# Set up the title page
st.set_page_config(page_title="Road Accident Analysis in India", layout="centered")

# Main title
st.title("Road Accident Analysis & Findings Insights in India")

# Subtitle with message
st.subheader("Insights into Accident Patterns and Future Trend Predictions")

# Brief introduction message
st.markdown("""
Welcome to our interactive dashboard on road accidents across India. This platform aims to provide a deep dive into accident data, exploring various patterns and factors to understand the root causes and trends over time. Through data-driven insights, we aim to support efforts toward safer roads and informed policy making.
""")

# Sections to guide users on available insights
st.markdown("### Key Insights Explored:")
st.write("In this analysis, we examine the following aspects:")

st.markdown("""
- **Future Trend Prediction**: Using an **RNN model** trained on historical data, we forecast accident trends for upcoming years.
- **Monthly Distribution of Accidents**: Understand how accident frequencies change month by month.
- **Primary Causes of Accidents**: Analyze factors such as overspeeding, driver fatigue, and other causes.
- **Gender-Based Distribution**: Study accident distribution among male and female drivers.
- **Vehicle Type Analysis**: Assess accident rates based on vehicle types, including trucks, cars, two-wheelers, and more.
- **Weather Conditions**: Observe how weather types (rainy, sunny, foggy, etc.) impact accident occurrences.
- **Yearly Trends and Urban vs. Rural Data**: Compare accident patterns over years, with a focus on rural and urban differences.
""")

# Impact statement
st.markdown("""
By examining these key areas, we aim to uncover critical patterns that can inform safety initiatives and contribute to the well-being of road users across India. Let's explore the data together and work towards actionable insights for a safer future on our roads.
""")