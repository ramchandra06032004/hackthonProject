import streamlit as st
import plotly.express as px
from helper import returnVehicleWiseAccidentGrapth  # Assuming the function is in 'helper.py'

# Set up Streamlit page configuration
st.set_page_config(page_title="Vehicle-wise Accident Distribution", layout="wide")

# Title of the page
st.title("Vehicle-wise Road Accident Distribution in India")

# Brief Introduction
st.markdown("""
In this section, we analyze the distribution of road accidents based on vehicle types in India. Understanding how different vehicles contribute to road accidents is essential for developing targeted safety measures and policies. The chart below visualizes the involvement of various vehicle types in accidents, helping us identify key areas for improvement.
""")

# Plot for Vehicle-wise Accident Distribution
st.subheader("Distribution of Road Accidents by Vehicle Type")
vehicle_graph = returnVehicleWiseAccidentGrapth()  # Call function to get the graph for vehicle-wise accident distribution
st.plotly_chart(vehicle_graph, use_container_width=True)  # Display the graph interactively

# Storytelling Explanation for the Vehicle-wise Accident Distribution
st.markdown("""
### Key Insights from the Data:

1. **Two-Wheelers**:  
   - Two-wheelers contribute to the highest proportion of road accidents. Their smaller size and exposure on the road make them particularly vulnerable. To reduce accidents, it is critical to focus on **helmet laws**, **awareness campaigns**, and **better road infrastructure** for riders.

2. **Cars, Taxis, Vans, and LMVs**:  
   - This category, which includes cars, taxis, vans, and Light Motor Vehicles (LMVs), accounts for a significant share of road accidents. These vehicles are often involved in accidents due to urban congestion. To mitigate these incidents, **seatbelt enforcement**, **speed management**, and **improved traffic discipline** are necessary.

3. **Heavy Vehicles (Buses, Trucks, Lorries)**:  
   - Accidents involving heavy vehicles like buses, trucks, and lorries are less frequent, but they tend to be more severe. Improved **driver training**, **maintenance** of heavy vehicles, and ensuring **load compliance** are essential to prevent such accidents.

4. **Non-Motorized Vehicles**:  
   - Non-motorized vehicles such as e-rickshaws and bicycles contribute to accidents, particularly in mixed traffic conditions. To ensure their safety, **dedicated lanes**, **clear road-sharing rules**, and **safety regulations** need to be enforced.

5. **Others**:  
   - This category includes accidents involving other vehicle types, including vehicles with unusual features or rare incidents. Although less frequent, these accidents still require attention, such as **vehicle inspections** and **emergency response plans**.

By analyzing this data, we can identify the key vehicle types that require more attention and focused safety measures.
""")

# Additional Insights and Recommendations
st.markdown("""
## Key Takeaways:
This data highlights that two-wheelers are the most common vehicle involved in road accidents, followed by cars and LMVs. Heavy vehicles also play a significant role in severe accidents. To improve road safety, the following actions are recommended:

- **Two-Wheeler Safety Initiatives**: Enforce helmet laws, raise awareness on safe riding, and improve infrastructure.
- **Car and LMV Regulations**: Promote seatbelt use, regulate speeds, and improve road discipline.
- **Heavy Vehicle Safety**: Train drivers, ensure vehicle maintenance, and monitor load limits.
- **Non-Motorized Vehicle Safety**: Provide dedicated lanes and enforce road-sharing rules for safety.

Addressing these areas will significantly reduce accident rates and improve road safety across India.
""")

# Conclusion and Call to Action
st.markdown("""
### Conclusion:
By understanding the role of different vehicles in road accidents, we can implement more targeted and effective road safety measures. The data-driven insights provided here will help policymakers and road safety organizations focus their efforts on the most vulnerable vehicle categories. 

With this information, we can work toward creating safer roads and reducing accident rates across the nation.
""")

# Footer Section
st.info("💡 *The key to road safety lies in understanding the role of different vehicles. Use these insights to take informed actions and save lives on the road.*")
