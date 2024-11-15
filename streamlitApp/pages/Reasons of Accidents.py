import streamlit as st
import plotly.express as px
from helper import returnReasonWiseAccidentGraph  # Assuming the function is in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Reasons for Road Accidents", layout="wide")

# Title of the page
st.title("Road Accident Causes and Contributing Factors in India")

# Brief introduction
st.markdown("""
In this section, we analyze the primary reasons behind road accidents in India. 
Understanding these causes is essential for identifying areas where road safety measures need to be strengthened. 
The pie chart below visualizes the distribution of accidents caused by different factors such as speeding, drunken driving, and others.
""")

# Plot for Reasons of Accidents
st.subheader("Distribution of Road Accidents by Cause")
reason_graph = returnReasonWiseAccidentGraph()  # Call function to get pie chart of accident reasons
st.plotly_chart(reason_graph)  # Display the pie chart

# Storytelling explanation for the reasons of accidents
st.markdown("""
The pie chart above clearly shows the main causes of road accidents in India, with the following key insights:

1. **Over-Speeding (638,056 accidents)**: 
   - The most prominent reason for accidents, over-speeding contributes to a large proportion of road accidents. Speeding reduces reaction time and increases the severity of accidents, making it a critical area to address through stricter speed limits and better enforcement.

2. **Drunken Driving (24,512 accidents)**:
   - While significantly lower than over-speeding, drunken driving remains a significant cause of accidents. Alcohol impairs judgment, coordination, and reaction times, making it crucial for authorities to increase awareness and enforcement against drinking and driving.

3. **Driving on the Wrong Side (48,862 accidents)**:
   - Another major contributor to accidents is driving on the wrong side of the road. This can cause head-on collisions, leading to fatal accidents. Increased awareness and strict law enforcement are necessary to curb this dangerous behavior.

4. **Jumping Red Light (8,886 accidents)**:
   - Disregarding traffic signals is another dangerous habit that leads to accidents. This behavior is often seen at busy intersections and is a significant contributor to both minor and serious accidents. Addressing this issue requires better traffic signal visibility and penalties for violations.

5. **Others (156,644 accidents)**:
   - The "Others" category includes various causes, such as mechanical failures, weather conditions, and pedestrian errors. These factors also need to be considered in safety measures, and it's important to understand the specifics of what falls under this category for targeted interventions.

By visualizing and understanding these reasons, we can prioritize road safety measures that focus on the most significant factors contributing to road accidents, ultimately reducing the number of accidents and saving lives.
""")

# Additional text with larger font sizes
st.markdown(""" 
## Key Takeaways
The data from this pie chart highlights the critical areas where road safety interventions need to be focused. Over-speeding stands out as the most common cause of accidents, followed by driving on the wrong side and drunken driving. 
Addressing these causes will be instrumental in improving road safety and reducing the occurrence of accidents in India.
""")


