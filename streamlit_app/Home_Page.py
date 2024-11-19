import streamlit as st

# Title for the homepage
st.title('Road Accident & Fleet Efficiency Dashboard')

# Subtitle
st.markdown("""
Welcome to the **Road Accident & Fleet Efficiency Dashboard**! This platform provides a detailed analysis of road accidents in India and the condition of the truck fleet. The interactive features help to understand trends, fleet efficiency, and factors impacting the work state of truck drivers in India.
""")


# Description of Dashboard Features
st.markdown("""
### What You Can Explore:
1. **Age and Gender-wise Accident Distribution**  
   Understand how road accidents vary across different age groups and genders, helping identify vulnerable groups and focus on safety measures.
   
2. **Reasons for Accidents**  
   Discover the most common causes of accidents and explore actionable steps to mitigate these risks.

3. **Rural vs Urban Road Accident Distribution**  
   Compare accident statistics in rural and urban areas, identifying location-specific risks for targeted interventions.

4. **Vehicle Fleet Efficiency**  
   Analyze the types, age, and condition of vehicles (especially trucks) operating in India. Investigate how fleet age and efficiency correlate with accident rates.

5. **Weather-wise Accident Distribution**  
   Understand the role of weather conditions in accident occurrence and how adverse weather impacts driver behavior.

6. **Year-wise Accident Distribution**  
   Explore trends in road accidents over time, identifying peak years of accidents and their correlation with policy changes or economic factors.
   
7. **Accident vs. Fleet Employment**  
   Investigate the relationship between accidents, fleet employment, and driver conditions to uncover factors contributing to the state of truck drivers in India.
""")

# Recommendations Section
st.markdown("""
### Insights & Recommendations for Improving Truck Driver Work State:
Based on the data analysis, we propose the following recommendations to improve the work state of truck drivers in India:
- **Fleet Age Optimization**: The older the fleet, the higher the chances of accidents due to mechanical failure. It’s crucial to replace aging trucks and improve vehicle maintenance schedules.
- **Driver Welfare Programs**: Implementing better driver welfare programs, focusing on mental health and physical well-being, especially after long working hours.
- **Technology Integration**: Introducing telematics and GPS systems in trucks to monitor driver behavior and ensure safety on the road.
- **Driver Training**: Offering more focused and region-specific driver training programs, particularly for rural drivers who may not be accustomed to modern road safety practices.
- **Regulation & Policy Change**: Enforcing strict regulations on vehicle condition and age, and introducing financial incentives for maintaining a safer, more efficient fleet.
""")

# Footer
st.info("💡 *Data and insights pave the way to safer roads and better truck driver conditions. Explore the dashboard to find patterns and contribute to making India's road transport safer!*")
