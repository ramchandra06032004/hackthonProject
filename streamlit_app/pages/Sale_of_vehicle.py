import streamlit as st
from helper import returnsaleGraph  # Assuming the function is in 'helper.py'

# Title of the dashboard
st.title('Year-wise and Combined Vehicle Sales Dashboard')

# Brief Introduction
st.markdown("""
Explore the trends in vehicle sales across different categories and combined data. This dashboard highlights key insights into the sales trends, with a notable drop observed after 2018–2019 across various vehicle types. 
Understanding these patterns is crucial for businesses, policymakers, and consumers to gauge market dynamics and make informed decisions.
""")

# Dropdown for selecting the option (vehicle or combined)
options = ['Combined', 'Passenger Cars', 'Utility Vehicles', 'Vans', 'Total Passenger Vehicles',
           'MandHCVs', 'LCVs', 'Total CVs', 'Three Wheelers', 'Scooters',
           'Motorcycles', 'Mopeds', 'Total Two Wheelers']
selected_option = st.selectbox('Select Vehicle Type or Combined', options)

# Call the function and pass the selected option
graph = returnsaleGraph('combined' if selected_option == 'Combined' else selected_option)

# Display the graph
st.plotly_chart(graph, use_container_width=True)

# Additional Insights Section
st.subheader('Sales Trends Insights (2018–2019)')
st.markdown("""
- **Sales Decline After 2018–2019:** 
  The data reveals a consistent drop in vehicle sales across all categories post-2018–2019. Several factors contributed to this trend:
  - **Economic Slowdown:** Decreased purchasing power and reduced consumer demand.
  - **BS-VI Emission Standards:** Transition to new emission standards caused delays in vehicle purchases.
  - **Increased Costs:** Rising prices for vehicles due to higher raw material costs, insurance, and taxes.
  - **Shift in Consumer Preferences:** Urban consumers increasingly favor ride-sharing platforms over personal vehicle ownership.
  - **Policy and Financial Challenges:** The introduction of new GST rates, changes in the Motor Vehicle Act, and liquidity crunches in NBFCs contributed to market uncertainty.

- **Significance of Monitoring Trends:**
  This downturn in vehicle sales is essential for stakeholders (manufacturers, policymakers, investors) to develop strategies and adapt to changing market conditions.
""")

# Additional Graph Annotations
st.subheader('Key Observations from the Graph')
st.markdown("""
1. **Combined Sales:** A sharp decline is evident in 2018–2019, with slow recovery in subsequent years.
2. **Passenger Cars:** Similar downward trend, particularly during the 2018–2019 period.
3. **Utility Vehicles & Two-Wheelers:** These segments show a consistent decline, mirroring the overall market slowdown.
4. **Category Comparison:** Use the dropdown above to explore sales trends for specific vehicle categories, allowing for deeper insights into individual segments.
""")

# User Engagement Section
st.info("💡 Tip: Select 'Combined' or a specific vehicle category from the dropdown to explore detailed sales trends for each segment.")
