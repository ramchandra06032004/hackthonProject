import streamlit as st
from helper import returnAgeWiseAccidentGraph, returnGenderWiseAccidentGraph  # Assuming these functions are in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Age and Gender-wise Accident Distribution", layout="wide")

# Title of the page
st.title("Age and Gender-wise Road Accident Distribution in India")

# Brief introduction
st.markdown("""
This section provides a comprehensive analysis of road accidents in India based on age and gender demographics. 
Identifying high-risk groups allows for targeted safety measures and interventions. 
Here, you will find insights on which age groups and genders are most impacted by road accidents, helping us to understand road safety challenges.
""")

# Plot for Age-wise Distribution of Road Accidents
st.subheader("Age-wise Distribution of Road Accidents")
age_graph = returnAgeWiseAccidentGraph()  # Call function to get age-wise accident distribution graph
st.plotly_chart(age_graph)  # Display the age-wise distribution graph

# Storytelling explanation for age-wise accident trends
st.markdown("""
### Age-wise Insights:
1. **Age Group 25-35**:
   - This age group is involved in the highest number of road accidents, with over 78,000 accidents reported in 2019. 
     Both males and females in this group face high accident rates, making it the most at-risk demographic for road accidents.

2. **Young Drivers (18-25)**:
   - The 18-25 age group also shows substantial accident involvement, reflecting the challenges faced by newer, less-experienced drivers. 
     Enhanced training and awareness campaigns could benefit this group, reducing their accident risk.

3. **Older Age Groups**:
   - Accident involvement declines in individuals above 50, possibly due to lower driving frequency and adherence to safer driving habits.
   
These trends underscore the need for focused safety interventions targeting young adults (18-35) to reduce accident rates effectively.
""")

# Plot for Gender-wise Distribution of Road Accidents
st.subheader("Gender-wise Distribution of Road Accidents")
gender_graph = returnGenderWiseAccidentGraph()  # Call function to get gender-wise accident distribution pie chart
st.plotly_chart(gender_graph)  # Display the gender-wise distribution graph

# Storytelling explanation for gender-wise accident trends
st.markdown("""
### Gender-wise Insights:
In 2019, there is a distinct gender-based pattern in road accidents:
- **Males**: Account for a significant majority, representing **85.6%** of road accidents. This trend reflects higher exposure and engagement in driving activities by men in India.
- **Females**: Represent **14.4%** of road accidents. Although a smaller percentage, the rate is notable and calls for inclusive road safety programs that address both male and female drivers.

The clear gender disparity in accident involvement suggests the need for targeted programs, especially in educating and reducing risky driving behaviors among male drivers.
""")

# Additional Insights and Recommendations
st.markdown("""
## Key Recommendations:
Based on age and gender insights, here are some recommendations:
- **Awareness Campaigns for Young Adults**: Educational programs focusing on safe driving practices, especially for the 18-35 age group.
- **Gender-specific Initiatives**: Enhanced awareness and enforcement of traffic laws, particularly targeting male drivers, who constitute the majority of accident cases.
- **Enhanced Driver Education for Young Drivers**: Defensive driving courses and stricter licensing processes for younger drivers can help improve safety and reduce accident rates.
""")


