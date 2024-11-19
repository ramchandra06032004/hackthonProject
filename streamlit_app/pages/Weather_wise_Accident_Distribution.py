import streamlit as st
from helper import returnWeatherWiseAccidentGraph  # Assuming this function is in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Weather-wise Accident Distribution", layout="wide")

# Title of the page
st.title("Weather-wise Road Accident Distribution in India")

# Brief introduction
st.markdown("""
In this section, we explore how various weather conditions influence road accidents in India. 
By analyzing accident data across different weather types, we can identify specific conditions that increase the likelihood of accidents, especially during adverse weather such as rain or fog.
""")

# Plot for Weather-wise Distribution of Road Accidents
st.subheader("Accidents by Weather Condition")
weather_graph = returnWeatherWiseAccidentGraph()  # Fetching the weather-wise accident distribution graph
st.plotly_chart(weather_graph)  # Display the graph interactively

# Storytelling explanation for weather-wise accident trends
st.markdown("""
### Key Insights:
1. **Clear or Sunny Weather**:
   - Despite expectations, most accidents occur during clear or sunny weather. This may be attributed to higher traffic volumes, driver complacency, or speeding in good visibility conditions.
   - In clear weather, drivers might assume that the roads are safer, which leads to less caution and a higher likelihood of accidents.

2. **Rainy or Foggy Weather**:
   - Although accidents are less frequent in rainy or foggy weather, these accidents tend to be more severe. Poor visibility, slippery roads, and longer stopping distances all contribute to higher risk.
   - The severity of accidents in such weather underlines the importance of adopting defensive driving practices and being extra cautious during adverse conditions.

3. **Weather-Specific Safety Recommendations**:
   - **Clear Weather**: Promote awareness about the risks of speeding and distractions in favorable conditions. Encourage maintaining safe distances and being vigilant on the road.
   - **Adverse Weather**: Improve infrastructure with better road signage, better road lighting, and visibility enhancements. Encourage safer driving practices, such as reducing speed and using headlights in fog or rain.
""")

# Additional analysis and targeted recommendations
st.markdown("""
## Analyzing Weather's Impact on Accident Rates:
The analysis highlights that while adverse weather contributes to fewer accidents, these incidents are often more serious. To address these trends, the following actions are recommended:

- **Driver Education**: Promote consistent safe driving habits across all weather conditions. Safety campaigns should emphasize the importance of caution, whether it's sunny or rainy.
- **Enhanced Infrastructure**: Reflective road signs, road lighting, and smart warning systems can help improve safety during adverse weather conditions, reducing the severity of accidents.

By implementing these strategies, we can mitigate the risk of accidents and create safer road environments in both favorable and challenging weather conditions.
""")
st.info("💡 Tip: Explore the interactive graph above to understand the distribution of road accidents based on different weather conditions.")