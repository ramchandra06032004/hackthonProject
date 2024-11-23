import streamlit as st

# Title for the homepage
st.title('Road Accident & Fleet Efficiency Dashboard')

# Subtitle
st.markdown("""
Welcome to the **Road Accident & Fleet Efficiency Dashboard**! This platform provides a detailed analysis of road accidents in India and the condition of the truck fleet. 
The interactive features help to understand trends, fleet efficiency, and factors impacting the work state of truck drivers in India.
""")

# Description of Dashboard Features
st.markdown("""
### What You Can Explore:
1. **Age and Gender-wise Accident Trends**  
   Understand how road accidents vary across different age groups and genders, helping identify vulnerable groups and focus on safety measures.
   
2. **Major Causes of Road Accidents**  
   Discover the most common causes of accidents and explore actionable steps to mitigate these risks.

3. **Rural vs Urban Accident Analysis**  
   Compare accident statistics in rural and urban areas, identifying location-specific risks for targeted interventions.

4. **Digital Route Risk Assessment for Truck Drivers**  
   Leverage AI to analyze weather, road conditions, and historical data to enhance truck driver safety on Indian roads.

5. **AI-Powered Truck Safety Systems**  
   Explore how technology can reduce human error, manage driver fatigue, and improve safety in high-risk zones.

6. **Road Accident Trends Over the Years**  
   Explore trends in road accidents over time, identifying peak years of accidents and their correlation with policy changes or economic factors.
   
7. **Vehicle-wise Accident Patterns**  
   Investigate the relationship between accidents, fleet employment, and driver conditions to uncover factors contributing to the state of truck drivers in India.
""")

# Section 1: Age and Gender-wise Accident Trends
st.subheader("1. Age and Gender-wise Accident Trends")
st.markdown("### Insights")
st.markdown("""
- The 25-35 age group has the highest number of accidents due to risk-taking behavior and frequent travel.
- Males are involved in 85.6% of accidents, reflecting higher exposure and riskier driving habits.
""")
st.markdown("### Recommendations")
st.markdown("""
- Launch targeted safety campaigns for young male drivers, focusing on reducing speeding and reckless behavior.
- Introduce gender-specific safety programs to address male-dominated accident trends, such as stress management workshops and gamified training modules.
""")

# Section 2: Major Causes of Road Accidents
st.subheader("2. Major Causes of Road Accidents")
st.markdown("### Insights")
st.markdown("""
- Over-speeding is the leading cause of accidents, accounting for 638,056 incidents annually.
- Drunken driving and driving on the wrong side are significant contributors to accidents.
- Fatigue and mechanical failures also play critical roles in accidents involving trucks.
""")
st.markdown("### Recommendations")
st.markdown("""
- Enforce stricter speed regulations and penalties for drunk driving.
- Equip trucks with fatigue detection systems and ensure regular maintenance to prevent mechanical failures.
- Use technology like AI dash cams to monitor and alert drivers to unsafe conditions.
""")

# Section 3: Rural vs Urban Accident Analysis
st.subheader("3. Rural vs Urban Accident Analysis")
st.markdown("### Insights")
st.markdown("""
- Rural areas face rising accident rates due to poor infrastructure, lack of emergency response, and insufficient enforcement.
- Urban areas report higher accidents in terms of numbers but lower severity due to better road infrastructure.
""")
st.markdown("### Recommendations")
st.markdown("""
- Urban: Enhance traffic management systems and enforce stricter penalties for rule violations.
- Rural: Implement AI to identify high-risk zones, upgrade road infrastructure, and improve emergency response systems.
""")

# Section 4: Digital Route Risk Assessment for Truck Drivers
st.subheader("4. Digital Route Risk Assessment for Truck Drivers")
st.markdown("### Insights")
st.markdown("""
- Unsafe routes with poor road quality and challenging weather conditions significantly increase accident risks for truck drivers.
""")
st.markdown("### Recommendations")
st.markdown("""
- Introduce AI-based route planning tools that analyze weather, traffic patterns, and historical accident data to suggest safer routes.
- Implement real-time alerts for hazards like road closures or extreme weather.
""")

# Section 5: AI-Powered Truck Safety Systems
st.subheader("5. AI-Powered Truck Safety Systems")
st.markdown("### Insights")
st.markdown("""
- AI systems can effectively detect driver fatigue, distractions, and unsafe behaviors in real time.
""")
st.markdown("### Recommendations")
st.markdown("""
- Equip trucks with AI-powered in-cab monitoring systems to track driver health and alert them during fatigue or distractions.
- Use gamification to incentivize safe driving behaviors, rewarding drivers for adherence to safety protocols.
""")

# Section 6: Road Accident Trends Over the Years
st.subheader("6. Road Accident Trends Over the Years")
st.markdown("### Insights")
st.markdown("""
- Accident rates have shown minimal decline despite numerous policy interventions, highlighting the need for innovative solutions.
""")
st.markdown("### Recommendations")
st.markdown("""
- Regularly assess policy effectiveness and update regulations to incorporate AI-driven insights.
- Promote semi-autonomous driving technologies to reduce human error, especially for commercial vehicles.
""")

# Section 7: Vehicle-wise Accident Patterns
st.subheader("7. Vehicle-wise Accident Patterns")
st.markdown("### Insights")
st.markdown("""
- Heavy vehicles often cause severe accidents, particularly in rural areas with poor infrastructure.
""")
st.markdown("### Recommendations")
st.markdown("""
- Mandate the use of speed limiters and lane discipline systems for heavy vehicles.
- For trucks, implement collision avoidance and braking assistance technologies.
""")

# Footer
st.markdown("---")
st.markdown("By leveraging these insights and recommendations, we can work towards reducing road accidents and improving fleet efficiency in India.")
st.info("💡 For more information, check out the sidebar on the left for detailed analysis and visualizations.")
