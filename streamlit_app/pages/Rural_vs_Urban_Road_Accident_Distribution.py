import streamlit as st
from helper import returnRuralUrbanAccidentGraph, returnYearWiseRuralUrbanGraph  # Assuming the function is in 'helper.py'

# Set up Streamlit page configuration
st.set_page_config(page_title="Rural and Urban Accident Distribution", layout="wide")

# Title of the page
st.title("Rural vs. Urban Road Accident Distribution in India")

# Brief Introduction
st.markdown("""
This section delves into the distribution of road accidents across rural and urban areas in India. By analyzing the dynamics of accidents in these distinct settings, we can identify the unique safety challenges faced by both areas. 
This data-driven analysis helps target specific interventions for reducing accidents in both rural and urban settings.
""")

# Plot for Rural and Urban Distribution of Road Accidents
st.subheader("Rural and Urban Accident Distribution by State")
rural_urban_graph = returnRuralUrbanAccidentGraph()  # Call function to get rural and urban accident distribution graph
st.plotly_chart(rural_urban_graph, use_container_width=True)  # Display the graph

# Storytelling Explanation for Rural and Urban Accident Trends
st.markdown("""
### Key Insights:
1. **Uttar Pradesh (UP) and Maharashtra (MH)**:
   - UP and MH exhibit high accident rates in both rural and urban areas. In these states, road safety interventions need to address specific issues like high vehicle density, diverse road conditions, and inconsistent traffic law enforcement.

2. **Rural vs. Urban Accident Patterns**:
   - **Rural Areas**: Accidents are often caused by higher speeds, fewer traffic controls, and limited emergency response infrastructure. A lack of road signs and speed limits can exacerbate accident severity.
   - **Urban Areas**: Urban regions face congestion, complex intersections, and pedestrian-related accidents. Traffic laws and road design improvements are critical to improving safety in these areas.

3. **Safety Recommendations for High-Risk States**:
   - Targeted safety measures should be designed to address the unique challenges of rural and urban settings. For high-risk states like UP and MH, strategies could include infrastructure upgrades, enhanced traffic enforcement, and better community education.
""")

# Recommendations Section
st.markdown("""
## Recommendations Based on Rural and Urban Accident Data:
- **Rural Areas**:
   - Focus on enforcing speed limits, improving road signage, and expanding emergency response networks to reduce accident severity and frequency.
   
- **Urban Areas**:
   - Address traffic congestion, enhance pedestrian safety, and ensure strict enforcement of traffic laws to improve road safety in urban environments.

- **State-Specific Initiatives for UP and MH**:
   - Given the high accident rates, these states would benefit from focused road safety campaigns, infrastructure investments, and stricter enforcement to address the unique accident patterns observed in both rural and urban regions.
""")

# Dropdown for selecting the year range
year_options = ['Combined', '2018', '2019', '2020', '2021']
selected_year = st.selectbox('Select Year', year_options)

# Fetch and display year-wise rural and urban accident graph
fig = returnYearWiseRuralUrbanGraph(selected_year)
st.plotly_chart(fig, use_container_width=True)

# Insights on Yearly Trends in Rural and Urban Accidents
st.markdown("""
### Observed Trend (2018-2021): Urban Accidents Decrease, Rural Accidents Increase
From the year-wise data, the following patterns are observed:

- **Urban Areas**: There's a noticeable **decrease in accidents** over time. This trend could be attributed to better infrastructure, more rigorous traffic regulation, and successful road safety initiatives.

- **Rural Areas**: In contrast, **rural accidents have increased** over the years. This rise may be due to expanding rural road networks, a lack of stringent traffic regulations, and limited safety infrastructure.

As rural infrastructure continues to grow, addressing these safety challenges will be crucial to reducing rural accident rates.
""")

# Footer Section
st.info("💡 *Improving road safety in both rural and urban areas requires tailored interventions. Use the data insights to develop focused strategies for accident reduction.*")
