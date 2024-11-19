import streamlit as st

# Set up Streamlit page
st.set_page_config(page_title="Snowflake Integration in Road Accident Analysis", layout="wide")

# Title of the page
st.title("How Snowflake is Used in This Project")

# Introduction about Snowflake usage
st.markdown("""
In this project, I utilized **Snowflake**, a cloud-based data platform, in combination with **Python**, **Pandas**, **NumPy**, and **Plotly** to preprocess, analyze, and visualize road accident data. Below is an explanation of how I leveraged Snowflake for data handling and analysis tasks.
""")

# Section 1: Data Preprocessing on Snowflake with Python Libraries
st.subheader("1. Data Preprocessing on Snowflake with Python")
st.markdown("""
- I used **Snowflake** to store and manage the large-scale road accident dataset. Snowflake's cloud platform allowed me to efficiently load the raw data into Snowflake tables.
- After importing the data into Snowflake, I used **Python** along with **Pandas** and **NumPy** to preprocess and clean the data. This included tasks such as handling missing values, filtering out irrelevant records, and converting data into a more usable format.
- For example, missing values were handled using **Pandas' fillna()** function, and data type conversions were done to ensure that columns like dates and numeric values were in the correct format for analysis.
""")

# Section 2: Snowflake Jupyter Notebooks for Analysis and Plotting
st.subheader("2. Data Analysis and Plotting in Snowflake Jupyter Notebooks")
st.markdown("""
- I used **Snowflake Jupyter Notebooks** to perform the data analysis and plotting. Snowflake's integration with Jupyter provided a seamless environment for running Python code directly on data stored within Snowflake.
- Using **Pandas**, I analyzed the road accident data, including calculating accident statistics, fatalities, injuries, and accident trends over time. **NumPy** was used for numerical operations and aggregations.
- After the analysis, I used **Plotly** to create interactive graphs that visualize key insights such as accident trends over the years, fatalities, and injury distributions.
- The generated plots and processed data were then saved as **Pandas DataFrames**, which were stored back in **Snowflake** for easy access and future use.
""")

# Section 3: Storing and Retrieving Processed Data in Snowflake
st.subheader("3. Storing and Retrieving Processed Data in Snowflake")
st.markdown("""
- After the data preprocessing and analysis, I stored the results, including aggregated tables and processed datasets, back into **Snowflake**. This allowed for easy retrieval whenever the data was needed for visualization or further analysis in the Streamlit app.
- The use of **Snowflake's data storage** allowed me to store large DataFrames securely and efficiently, ensuring that my project can scale and handle large volumes of data.
- I also took advantage of Snowflake's **data-sharing** capabilities, making it easier to share results and processed data with collaborators and stakeholders.
""")

# Section 4: Benefits of Using Snowflake with Python Libraries
st.subheader("4. Benefits of Using Snowflake with Python Libraries")
st.markdown("""
- **Seamless Integration**: Snowflake's integration with Python and libraries like **Pandas** and **NumPy** made the entire data processing workflow smooth and efficient. I was able to leverage Snowflake for data storage and use Python for detailed data manipulation and analysis.
- **Scalability**: Snowflake's cloud-based architecture allowed me to scale up the data processing when working with large datasets without worrying about infrastructure.
- **Real-Time Access**: Snowflake allowed me to easily access the processed data in real-time for visualization and reporting, providing a dynamic and interactive data analysis environment.
- **Performance**: Snowflake’s compute resources were optimized to handle the data processing and analysis tasks without any performance degradation, ensuring that the project could handle growing datasets efficiently.
- **Security and Collaboration**: Snowflake provided a secure platform for storing sensitive road accident data and enabled seamless collaboration with other team members, allowing them to access the necessary data for further analysis.
""")

# Conclusion
st.markdown("""
In conclusion, integrating **Snowflake** with **Python**, **Pandas**, **NumPy**, and **Plotly** enabled me to effectively handle, preprocess, analyze, and visualize road accident data. This combination of technologies ensured that the project could scale efficiently, while providing real-time access to processed data for interactive analysis and decision-making.
""")
