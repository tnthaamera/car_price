import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import numpy as np

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df): 
  st.header('Visualise Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader('Scatterplot')
  features_list = st.multiselect('Select the x-axis values:', ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for feature in features_list:
    st.subheader(f"Scatter plot between {feature} and price")
    plt.figure(figsize = (12, 6))
    sns.scatterplot(x=feature, y='price', data=car_df)
    st.pyplot()
  st.subheader('Visualisation Selector')
  plot_types = st.multiselect('Select the charts or plots:', ('Histogram', 'Box Plot', 'Correlation Heatmap'))
  if 'Histogram' in plot_types:
    st.subheader("Histogram")
    columns = st.selectbox("Select the column to create its histogram",
                                      ('carwidth', 'enginesize', 'horsepower'))
    plt.hist(car_df[columns], bins='sturges')
    st.pyplot()

    # Create box plot using the 'seaborn' module and the 'st.pyplot()' function.
  if 'Box Plot' in plot_types: 
    st.subheader('Box Plot')
    columns = st.selectbox("Select the column to create its box plot",
                                      ('carwidth', 'enginesize', 'horsepower'))
    sns.boxplot(x=car_df[columns])
    st.pyplot()

    # Display correlation heatmap using the 'seaborn' module and the 'st.pyplot()' function.
  if 'Correlation Heatmap' in plot_types:
    st.subheader("Correlation Heatmap")
    plt.figure(figsize = (8, 5))
    ax = sns.heatmap(car_df.corr(), annot = True) # Creating an object of seaborn axis and storing it in 'ax' variable
    bottom, top = ax.get_ylim() # Getting the top and bottom margin limits.
    ax.set_ylim(bottom + 0.5, top - 0.5) # Increasing the bottom and decreasing the bottom margins respectively.
    st.pyplot()