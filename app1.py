# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Set the title and description of the app
st.title("Simple Data Visualization App")
st.write("This is a simple Streamlit app to visualize random data.")

# Create a sidebar for user input
st.sidebar.header("User Input")

# Generate random data
np.random.seed(0)
data = np.random.randn(50, 2)
df = pd.DataFrame(data, columns=['X', 'Y'])

# Create a checkbox for displaying raw data
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df)

# Create a line chart
st.subheader("Line Chart")
st.line_chart(df)

# Create a scatter plot
st.subheader("Scatter Plot")
st.scatter_chart(df)

# Create a histogram using Matplotlib
st.subheader("Histogram")
fig, ax = plt.subplots()
ax.hist(df['X'], bins=20)
st.pyplot(fig)


# Create a bar chart
st.subheader("Bar Chart")
st.bar_chart(df)

# Create a map (dummy data)
st.subheader("Map")
st.map()

# Create a footer
st.sidebar.text("By Your Name")

# Run the app with 'streamlit run app.py' in the terminal
