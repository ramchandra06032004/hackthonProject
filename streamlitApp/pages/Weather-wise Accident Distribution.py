import streamlit as st
from helper import returnWeatherWiseAccidentGraph  # Assuming this function is in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Weather-wise Accident Distribution", layout="wide")

# Title of the page
st.title("Weather-wise Road Accident Distribution in India")

# Brief introduction
st.markdown("""
This section examines how weather conditions impact road accidents in India. By analyzing accident rates across various weather types, we can gain insights into how weather affects road safety, especially during challenging conditions like rain or fog.
""")

# Plot for Weather-wise Distribution of Road Accidents
st.subheader("Accidents by Weather Condition")
weather_graph = returnWeatherWiseAccidentGraph()  # Call function to get weather-wise accident distribution graph
st.plotly_chart(weather_graph)  # Display the graph

# Storytelling explanation for weather-wise accident trends
st.markdown("""
### Key Insights:
1. **Sunny or Clear Weather**:
   - Surprisingly, the majority of accidents occur during clear or sunny weather. This could be due to higher traffic volumes, driver overconfidence, or increased vehicle speeds in good visibility conditions.
   - In clear weather, drivers may not anticipate accidents as readily, potentially leading to less caution on the road. 

2. **Rainy or Foggy Conditions**:
   - While accidents are less frequent in adverse weather conditions, they tend to be more severe due to factors such as reduced visibility, slippery road surfaces, and extended braking distances.
   - Rainy and foggy weather still contributes significantly to accident statistics and calls for cautious driving practices to mitigate risks in these conditions.

3. **Weather-Specific Recommendations**:
   - During sunny and clear weather, promoting awareness of safe driving practices—such as observing speed limits, maintaining safe distances, and avoiding distractions—can help reduce accident rates.
   - In adverse weather, infrastructure improvements like reflective road signs, road lighting, and warning systems can help improve safety.
""")

# Additional analysis section
st.markdown("""
## Analysis of Weather-Related Factors on Accident Rates
Understanding that most accidents happen in favorable weather conditions allows for targeted interventions:
- **Driver Education**: Encouraging safe driving habits in all weather conditions is essential, as accident rates are high even when visibility and road conditions are optimal.
- **Safety Campaigns**: Public safety campaigns focused on cautious driving in clear weather may be as crucial as those aimed at adverse weather driving.

With better awareness and infrastructure, accident rates in both clear and adverse weather conditions can be minimized.
""")
