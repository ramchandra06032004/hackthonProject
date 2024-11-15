import streamlit as st
from helper import returnVehicleWiseAccidentGrapth  # Assuming this function is in 'helper.py'

# Set up Streamlit page
st.set_page_config(page_title="Vehicle-wise Accident Distribution", layout="wide")

# Title of the page
st.title("Vehicle-wise Road Accident Distribution in India")

# Brief introduction
st.markdown("""
This section provides an analysis of road accidents by different types of vehicles in India. By identifying the types of vehicles most frequently involved in accidents, 
we can gain valuable insights for developing targeted road safety measures and regulations for various vehicle categories.
""")

# Plot for Vehicle-wise Distribution of Road Accidents
st.subheader("Vehicle-wise Distribution of Road Accidents")
vehicle_graph = returnVehicleWiseAccidentGrapth()  # Call function to get vehicle-wise accident distribution graph
st.plotly_chart(vehicle_graph)  # Display the graph

st.markdown("""
### Key Insights by Vehicle Type:
1. **Two-Wheelers**: 
   - Two-wheelers represent the highest proportion of road accidents in 2019. Due to their exposure, vulnerability, and significant numbers on the road, they are particularly at risk. This trend underscores the need for targeted safety measures for two-wheeler riders, including strict helmet enforcement and awareness programs.

2. **Cars, Taxis, Vans, and LMVs**:
   - Following two-wheelers, the category of cars, taxis, vans, and LMVs (Light Motor Vehicles) shows a high accident involvement. With the growing ownership of LMVs in urban and suburban areas, this trend calls for focused interventions on seatbelt usage, speed management, and road discipline.

3. **Buses and Trucks/Lorries**:
   - Heavy vehicles, including buses and trucks, also contribute to a notable portion of road accidents. Given the severity of accidents involving larger vehicles, improving safety standards and driver training for heavy vehicle operators is essential.

4. **Other Non-Motorized Vehicles**:
   - Though smaller in number, accidents involving e-rickshaws and other non-motorized vehicles highlight the need for safer integration of these vehicles on roads.
""")

# Additional Insights and Recommendations
st.markdown("""
## Recommendations Based on Vehicle Type:
- **Two-Wheeler Safety Initiatives**: Strengthening helmet laws, safe riding campaigns, and enforcing speed limits can reduce accidents involving two-wheelers.
- **Car and LMV Regulations**: Promoting responsible driving behaviors, strict adherence to seatbelt laws, and speed control measures can help decrease car-related accidents.
- **Heavy Vehicle Safety**: Ensuring mandatory training, vehicle maintenance, and compliance with load limits are critical for reducing accidents involving buses and trucks.
- **Safe Integration for Non-Motorized Vehicles**: Establishing clear lanes and road-sharing rules for non-motorized vehicles can improve road safety for all users.
""")
