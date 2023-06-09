# -*- coding: utf-8 -*-
"""python_project0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SimpETsqER9hJ58omkxqvMM4qS824M7j
"""

!pip install streamlit

!pip install opencage

# Commented out IPython magic to ensure Python compatibility.
# %%writefile python_project0.py
# import streamlit as st
# from opencage.geocoder import OpenCageGeocode
# 
# # Set up geocoder with your API key
# geocoder = OpenCageGeocode('4282708e690a4923be167247f1b2dded')
# 
# # Define the address to geocode
# address = '1600 Amphitheatre Parkway, Mountain View, CA'
# 
# # Geocode the address
# result = geocoder.geocode(address)
# 
# # Extract latitude and longitude from the result
# if result and len(result):
#     latitude = result[0]['geometry']['lat']
#     longitude = result[0]['geometry']['lng']
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)

!streamlit run --server.port 8502 python_project0.py