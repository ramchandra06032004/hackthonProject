import streamlit as st
from helper import returnAgeWiseAccidentGraph, returnGenderWiseAccidentGraph  # Assuming these functions are in 'helper.py'

# Set up Streamlit page configuration
st.set_page_config(page_title="Age and Gender-wise Accident Distribution", layout="wide")

# Title of the page
st.title("Age and Gender-wise Road Accident Distribution in India")

# Introduction text to set context
st.markdown("""
In this section, we provide a comprehensive analysis of road accidents in India, focusing on **age** and **gender** demographics. 
Understanding how different age groups and genders are impacted by road accidents is crucial for identifying high-risk segments and 
designing targeted interventions for improving road safety.
""")

# Age-wise Accident Distribution Chart
st.subheader("Age-wise Distribution of Road Accidents")
age_graph = returnAgeWiseAccidentGraph()  # Function to generate the age-wise distribution graph
st.plotly_chart(age_graph, use_container_width=True)  # Display the age-wise distribution graph with wider display

# Insights and Storytelling for Age-wise Trends
st.markdown("""
### Age-wise Insights:
1. **Age Group 25-35**:
   - This age group shows the highest involvement in road accidents, contributing to over **78,000 accidents** in 2019. Both men and women in this group are disproportionately affected, highlighting a critical demographic for road safety programs.
   
2. **Young Drivers (18-25)**:
   - The **18-25** age group also exhibits high accident rates, primarily due to inexperience and risky driving behaviors. Road safety campaigns focusing on this group can significantly reduce accidents.

3. **Older Drivers (50+)**:
   - Individuals above 50 years old have a significantly lower accident rate, likely due to a decline in driving frequency and adherence to safer driving practices. However, this group still represents a vulnerable segment in case of accidents.

This data emphasizes the importance of targeted safety interventions aimed at young adults and newer drivers to mitigate accident risks.
""")

# Gender-wise Accident Distribution Chart
st.subheader("Gender-wise Distribution of Road Accidents")
gender_graph = returnGenderWiseAccidentGraph()  # Function to generate the gender-wise distribution graph
st.plotly_chart(gender_graph, use_container_width=True)  # Display gender distribution graph with wider layout

# Insights and Storytelling for Gender-wise Trends
st.markdown("""
### Gender-wise Insights:
In 2019, gender-based trends in road accidents revealed the following:
- **Males**: Represent **85.6%** of road accidents, reflecting a higher exposure to road risks and a greater involvement in driving activities across India.
- **Females**: While females account for only **14.4%** of road accidents, this still represents a notable segment. Efforts to include women-specific road safety programs are important.

These statistics highlight the need for a **gender-sensitive approach** to road safety, with targeted interventions aimed at reducing risk among male drivers, who contribute to the majority of road accidents.
""")

# Key Recommendations Based on Insights
st.markdown("""
## Recommendations for Improvement:
Here are key recommendations to improve road safety based on the age and gender distribution insights:

- **Awareness Programs for Young Drivers**: Launch educational campaigns that promote safe driving, with a focus on reducing risky driving behavior among the 18-35 age group.
  
- **Gender-targeted Safety Programs**: Initiate road safety programs tailored to male drivers, who make up the majority of accident-related incidents. These could include workshops on reducing speeding and reckless driving.

- **Defensive Driving Courses**: Offer advanced driving courses for younger drivers to help them gain practical experience and improve road safety through better driving skills.
  
- **Policy Interventions for Fleet Management**: Implement policies for fleet operators that address driver welfare, focusing on younger, less experienced drivers and ensuring they receive adequate training and support.
""")

# Additional Insights & Conclusion
st.markdown("""
### Further Insights:
By incorporating age and gender-specific insights into the design of traffic safety policies, we can significantly reduce accident rates in high-risk groups. A data-driven approach ensures that interventions are targeted and effective, contributing to safer roads for all.
""")

# Footer Section
st.info("💡 *Data is crucial in shaping effective policies for road safety. Explore the dashboard for more insights and join the movement for safer roads!*")
