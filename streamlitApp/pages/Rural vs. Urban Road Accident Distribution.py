import streamlit as st
from helper import returnRuralUrbanAccidentGraph, returnYearWiseRuralUrbanGraph  # Assuming this function is in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Rural and Urban Accident Distribution", layout="wide")

# Title of the page
st.title("Rural vs. Urban Road Accident Distribution in India")

# Brief introduction
st.markdown("""
This section explores the distribution of road accidents across rural and urban areas in India, with a specific focus on states with the highest accident rates. 
Analyzing the rural and urban split provides insight into different accident dynamics, which can guide targeted safety measures.
""")

# Plot for Rural and Urban Distribution of Road Accidents
st.subheader("Rural and Urban Accident Distribution by State")
rural_urban_graph = returnRuralUrbanAccidentGraph()  # Call function to get rural and urban accident distribution graph
st.plotly_chart(rural_urban_graph)  # Display the graph

# Storytelling explanation for rural and urban accident trends
st.markdown("""
### Key Insights:
1. **Uttar Pradesh (UP) and Maharashtra (MH)**:
   - UP and MH consistently show high accident rates in both rural and urban areas, suggesting a need for targeted state-level interventions to address unique challenges such as high vehicle density, diverse road conditions, and differing traffic law enforcement.
   
2. **Rural vs. Urban Patterns**:
   - **Rural areas** tend to experience accidents due to factors like higher speeds on open roads, fewer traffic controls, and potentially slower emergency response times.
   - **Urban areas** face distinct challenges, including high traffic congestion, pedestrian traffic, and complex signal-controlled intersections.
   
3. **Safety Recommendations for High-Risk States**:
   - Implementing comprehensive road safety policies that address both rural and urban challenges, especially in high-risk states like UP and MH, can help reduce accident rates. Potential measures include infrastructure improvements, enhanced traffic enforcement, and community education on road safety.
""")

# Recommendations Section
st.markdown("""
## Recommendations Based on Rural and Urban Accident Data:
- **Rural Areas**:
   - Enforce speed limits, improve road signage, and expand emergency response infrastructure to address accident severity and frequency in rural regions.
   
- **Urban Areas**:
   - Focus on managing congestion, improving pedestrian safety, and enforcing traffic compliance in urban areas.
   
- **State-Specific Initiatives for UP and MH**:
   - Given the high accident rates, these states would benefit from targeted road safety campaigns, infrastructure improvements, and stricter law enforcement to address the specific accident trends in both rural and urban settings.
""")

# Dropdown for selecting year range
year_options = ['Combined', '2018', '2019', '2020', '2021']
selected_year = st.selectbox('Select Year', year_options)
fig = returnYearWiseRuralUrbanGraph(selected_year)

# Display the graph
st.plotly_chart(fig)

# Insights on Yearly Trends in Rural and Urban Accidents
st.markdown("""
### Observed Trend (2018-2021): Urban Accidents Decrease While Rural Accidents Increase
From the year-wise data, a significant pattern emerges:
- **Urban areas** show a **decrease in accident rates** over time, which may be attributed to better infrastructure, increased traffic regulation, and effective road safety measures.
- **Rural areas**, however, have seen a **rise in accident rates**. This increase could be linked to factors such as less stringent traffic control, expanding road networks into rural areas, and fewer dedicated safety measures.

As India's rural road infrastructure continues to grow, addressing these safety challenges will be crucial for reducing rural accident rates.
""")
