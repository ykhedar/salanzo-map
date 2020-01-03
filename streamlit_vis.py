import pandas as pd
import numpy as np
import streamlit as st
import get_nearest_pnt


def get_current_position():
    lat_ = 52.20472 + np.random.random_sample()/10
    lon_ = 0.14056 + np.random.random_sample()/10
    return lat_, lon_


# Read the csv file into a pandas data frame
curr_lat, curr_long = get_current_position()

nrst_pt = get_nearest_pnt.get_nearest_point(curr_lat, curr_long)
nrst_pt_df = pd.DataFrame([[1, nrst_pt[0], nrst_pt[1]]], columns=["id", "lat", "lon"])

df = pd.read_csv(filepath_or_buffer="data/test2.csv", names=["id", "lat", "lon"])


pt_to_query_df = pd.DataFrame([[1, curr_lat, curr_long]], columns=["id", "lat", "lon"])


st.deck_gl_chart(
viewport={
    'latitude': curr_lat,
    'longitude': curr_long,
    'zoom': 11,
    'pitch': 0,
},
layers=[
    {
    'type': 'ScatterplotLayer',
    'data': df,
    'getFillColor':  [0, 255, 0]
   },
   {
    'type': 'ScatterplotLayer',
    'data': nrst_pt_df,
    'getFillColor':  [255, 0, 0]
   },
    {
    'type': 'ScatterplotLayer',
    'data': pt_to_query_df,
    'getFillColor':  [0, 0, 255]
   },
    ])