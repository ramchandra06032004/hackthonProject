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
This section provides an in-depth analysis of road accidents, fatalities, and injuries over the years in India. 
We aim to uncover the key trends and patterns that help understand the evolving road safety situation.
Here, you will find insights into the number of accidents, fatalities, injuries, and road length distribution by year.
""")

# Plot for Year-wise Road Accident Distribution
st.subheader("Year-wise Accident Distribution")
accident_graph = returnYearVSAccidentGraph()  # Call function to get accident distribution graph
st.plotly_chart(accident_graph)  # Display the graph

# Storytelling explanation for the accident graph
st.markdown("""
From the first graph, we can clearly see a significant shift in the road accident trends over time. 
Between 1970 and 2010, road accidents showed a steady, linear increase, reflecting the rapid growth of India's population, 
increased urbanization, and the expansion of road networks. However, since 2010, we notice a slower increase, 
and in some cases, a decrease in the number of accidents. This suggests that efforts to improve road safety, stricter traffic laws, 
better awareness campaigns, and technological advancements in vehicles may be having a positive impact on reducing accidents over time.
""")

# Plot for Year-wise Deaths and Injuries Distribution
st.subheader("Year-wise Death and Injury Distribution")
death_injury_graph = returnDeathAndDiedGraphPerYear()  # Call function for deaths and injuries graph
st.plotly_chart(death_injury_graph)  # Display the graph

# Storytelling explanation for the death and injury graph
st.markdown("""
In the second graph, we observe the trends of persons killed and injured in road accidents. The number of injuries has been increasing 
linearly over time, which could be attributed to higher traffic volumes and more vehicles on the road. However, after 2015, 
we see a noticeable decrease in fatalities. This is a promising trend and could be a result of improved vehicle safety features, 
better emergency response systems, and more effective road safety policies that are starting to take effect in reducing fatalities.
""")

# Plot for Year-wise Road Length Distribution
st.subheader("Year-wise Road Length Distribution")
road_length_graph = returnRoadLengthGraph()  # Call function for road length graph
st.plotly_chart(road_length_graph)  # Display the graph

# Storytelling explanation for the road length graph
st.markdown("""
The third graph highlights the consistent, linear increase in the length of roads across India. This growth is a clear indicator of India's 
expanding infrastructure and efforts to improve connectivity, especially in rural and remote areas. With this steady increase in road 
construction, we see a nation on the rise—growing, expanding, and building the necessary infrastructure to accommodate its increasing 
population and economic activity.
""")

# Additional text with larger font sizes
st.markdown(""" 
## Detailed Analysis
Explore the detailed analysis of road accidents, fatalities, injuries, and road infrastructure over the years. 
The data provides insights into the trends and patterns of road safety in India, and understanding these patterns is crucial for 
developing effective policies and improving road safety measures.
""")

# Add a header for the RNN Model
st.markdown("## Predicting Future Trends with RNN Model")

# Add some text to introduce the RNN model
st.markdown("""
To predict future trends of road accidents, fatalities, and injuries, we are implementing a Recurrent Neural Network (RNN) model. 
The model will help forecast accident rates based on historical data, which can be valuable for planning safety interventions and policy-making.
The RNN model aims to provide reliable predictions, offering a forward-looking approach to road safety.
""")

# Placeholder for RNN model - This will be implemented later
st.markdown("""
### Placeholder for RNN Model Output
The RNN model will be displayed here once trained. Stay tuned for future predictions and insights.
""")
