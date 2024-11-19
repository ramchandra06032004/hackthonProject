import streamlit as st
import pandas as pd
import plotly.express as px
from helper import returnYearVSAccidentGraph, returnDeathAndDiedGraphPerYear, returnRoadLengthGraph  # Assuming all functions are in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Road Accident Analysis", layout="wide")

# Title of the page
st.title("Year-wise Road Accident and Casualty Distribution in India")

# Brief introduction
st.markdown("""
This section delves into a comprehensive analysis of road accidents, fatalities, injuries, and road length in India over the years. 
We will explore trends, identify critical patterns, and uncover insights that highlight the evolving road safety landscape in the country.
The analysis presented here aims to assist policymakers, safety advocates, and the general public in understanding the trajectory of road safety in India.
""")

# Plot for Year-wise Road Accident Distribution
st.subheader("Year-wise Accident Distribution")
accident_graph = returnYearVSAccidentGraph()  # Fetching the year vs accident distribution graph
st.plotly_chart(accident_graph)  # Display the graph

# Storytelling explanation for the accident graph
st.markdown("""
### Key Insights:
The first graph illustrates a clear trend in road accidents from 1970 to 2020. Initially, road accidents saw a steady increase, reflecting the country's rapid population growth, urbanization, and expansion of transportation networks. This surge was likely driven by a rise in vehicle ownership, road infrastructure challenges, and insufficient safety measures.

However, post-2010, we observe a deceleration in the growth rate of accidents, with a slight decrease in certain years. This suggests that initiatives to improve road safety—such as stricter traffic laws, awareness campaigns, better road designs, and advancements in vehicle technology—may be yielding positive results in curbing accidents. 

This shift could also indicate the beginning of a safer road environment as India adapts to modern safety standards.
""")

# Plot for Year-wise Deaths and Injuries Distribution
st.subheader("Year-wise Death and Injury Distribution")
death_injury_graph = returnDeathAndDiedGraphPerYear()  # Fetching the year vs death and injury distribution graph
st.plotly_chart(death_injury_graph)  # Display the graph

# Storytelling explanation for the death and injury graph
st.markdown("""
### Key Insights:
The second graph highlights the number of fatalities and injuries resulting from road accidents over time. While injuries have risen linearly, likely due to growing traffic volumes, fatalities show a promising decline, particularly after 2015. This reduction in fatalities suggests that recent improvements in vehicle safety, emergency response systems, and road safety policies are starting to take effect.

Key factors contributing to this decline include:
- Enhanced vehicle safety features, such as airbags and anti-lock braking systems (ABS)
- Improved emergency medical services (EMS) and accident response times
- Stricter enforcement of traffic laws and regulations

These trends reflect the positive impact of safety initiatives, signaling that while road accidents remain a concern, efforts to reduce loss of life are gradually succeeding.
""")

# Plot for Year-wise Road Length Distribution
st.subheader("Year-wise Road Length Distribution")
road_length_graph = returnRoadLengthGraph()  # Fetching the year vs road length distribution graph
st.plotly_chart(road_length_graph)  # Display the graph

# Storytelling explanation for the road length graph
st.markdown("""
### Key Insights:
The third graph demonstrates a consistent increase in India's road length over the years. This steady expansion of road infrastructure is indicative of the country's commitment to improving connectivity and supporting its growing population and economy. Expanding road networks, especially in rural and remote areas, plays a crucial role in enhancing accessibility and reducing travel times.

However, the increase in road length must be complemented by better road safety measures, as longer roads and more vehicles on the road can lead to greater risk if safety standards are not adequately maintained.

With this infrastructural growth, it's essential to continue focusing on both safety and quality of road construction to ensure that the expanding network does not outpace safety measures.
""")

# Additional text with larger font sizes
st.markdown("""
## In-Depth Analysis and Implications
This analysis provides critical insights into how road accidents, fatalities, injuries, and road infrastructure have evolved over the years in India. By understanding these patterns, we can identify key areas for improvement in road safety and develop targeted interventions.

### Future Considerations:
- **Policymakers**: Should focus on implementing and enforcing more stringent road safety regulations, particularly in urban areas where accidents are most frequent.
- **Safety Advocates**: Should emphasize public education campaigns on safe driving practices and promote the adoption of vehicle safety technologies.
- **Infrastructure Planners**: Should continue expanding road networks, but ensure that the quality of roads, road markings, and signage keeps pace with the growth in traffic.

By acting on these insights, we can aim for a safer road environment in India, reducing both the frequency and severity of accidents while improving the overall quality of road infrastructure.
""")
