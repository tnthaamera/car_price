import streamlit as st
import numpy as np
import pandas as pd

# Define a function 'app()' which accepts 'car_df' as an input.
def app(): 
  st.header('Car Price Prediction App')
  st.text('''This web app allows a user to predict the prices of a car based on their engine
  size, horse power, dimensions and the drive wheel type parameters.''')

