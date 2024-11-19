import streamlit as st
import plotly.express as px
from helper import returnReasonWiseAccidentGraph  # Assuming the function is in 'helper.py'

# Set up Streamlit page configuration
st.set_page_config(page_title="Reasons for Road Accidents", layout="wide")

# Title of the page
st.title("Road Accident Causes and Contributing Factors in India")

# Brief Introduction
st.markdown("""
In this section, we analyze the primary reasons behind road accidents in India. 
Understanding these causes is essential for identifying areas where road safety measures need to be strengthened. 
The pie chart below visualizes the distribution of accidents caused by different factors such as speeding, drunken driving, and others.
""")

# Plot for Reasons of Accidents
st.subheader("Distribution of Road Accidents by Cause")
reason_graph = returnReasonWiseAccidentGraph()  # Call function to get pie chart of accident reasons
st.plotly_chart(reason_graph, use_container_width=True)  # Display the pie chart

# Storytelling Explanation for the Reasons of Accidents
st.markdown("""
### Key Insights from the Data:

1. **Over-Speeding (638,056 accidents)**:  
   - The leading cause of accidents, speeding reduces reaction time and increases accident severity. Stricter speed limits, along with improved enforcement, are necessary to reduce these incidents. 

2. **Drunken Driving (24,512 accidents)**:  
   - Though fewer than speeding-related accidents, drunk driving remains a serious threat. Alcohol impairs judgment, coordination, and reaction times. Greater awareness campaigns and stricter enforcement are essential in addressing this issue.

3. **Driving on the Wrong Side (48,862 accidents)**:  
   - A significant contributor to head-on collisions, wrong-way driving is often seen in high-traffic areas. Public awareness campaigns and stricter law enforcement can help reduce this dangerous behavior.

4. **Jumping Red Light (8,886 accidents)**:  
   - Running red lights is a common but dangerous habit that leads to accidents. Increased traffic signal visibility, along with penalties for violations, can help curb this behavior.

5. **Others (156,644 accidents)**:  
   - This category includes causes like mechanical failures, adverse weather conditions, and pedestrian errors. While less frequent, these causes require safety measures, including vehicle maintenance and weather-specific guidelines for drivers.

By examining these factors, we can prioritize safety measures targeting the most common causes of accidents, ultimately reducing fatalities and injuries.
""")

# Additional Insights and Recommendations
st.markdown("""
## Key Takeaways:
This data highlights the major contributors to road accidents in India. Over-speeding is the most frequent cause, followed by driving on the wrong side and drunken driving. 
To improve road safety, it is essential to focus on these areas:

- **Stricter Speed Regulations**: Imposing stricter speed limits and enhancing law enforcement.
- **Awareness Campaigns on Drunken Driving**: Educating the public and enforcing the no-tolerance policy for alcohol-related driving.
- **Enforcement of Traffic Rules**: Stronger monitoring and penalties for violations like driving on the wrong side and jumping red lights.

Addressing these issues will significantly reduce accident rates and improve road safety across the nation.
""")

# Call to Action/Conclusion
st.markdown("""
### Conclusion:
By understanding the root causes of road accidents, we can implement targeted measures that effectively address these issues and make Indian roads safer for everyone. Data-driven policies can help reduce accident rates, save lives, and contribute to a safer driving environment.
""")

# Footer Section
st.info("💡 *The key to preventing road accidents is identifying the causes. Use the data insights to make informed decisions and save lives.*")
