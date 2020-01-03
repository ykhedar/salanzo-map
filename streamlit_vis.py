import pandas as pd
import streamlit as st
import get_farmlands


location = st.slider('Point Number', 0, 100, 1)


def get_current_position(lat1, lon1, loc):
    lat_ = get_farmlands.getLongLat(0, loc, lat1, lon1, "lat")
    lon_ = get_farmlands.getLongLat(0, loc, lat1, lon1, "lon")
    return lat_, lon_


def generate_data_start(curr_lat, curr_long, loc):
    # Read the csv file into a pandas data frame
    curr_lat, curr_long = get_current_position(curr_lat, curr_long, loc)
    nrst_pt = get_farmlands.get_nearest_point(curr_lat, curr_long, True)
    nrst_pt_df = pd.DataFrame([[1, nrst_pt[0], nrst_pt[1]]], columns=["id", "lat", "lon"])
    df = pd.read_csv(filepath_or_buffer="data/test2.csv", names=["id", "lat", "lon"])
    pt_to_query_df = pd.DataFrame([[1, curr_lat, curr_long]], columns=["id", "lat", "lon"])
    return curr_lat, curr_long, nrst_pt_df, df, pt_to_query_df


def create_map(curr_lat, curr_long, nrst_pt_df, df, pt_to_query_df):
    st.deck_gl_chart(
    viewport={
        'mapStyle': 'mapbox://styles/mapbox/streets-v11',
        'latitude': curr_lat,
        'longitude': curr_long,
        'zoom': 11,
        'pitch': 0,
    },
    layers=[
        {
        'type': 'ScatterplotLayer',
        'data': df,
        'getFillColor':  [0, 0, 0],
        'opacity': 0.05,
        'getRadius': 150
       },
       {
        'type': 'ScatterplotLayer',
        'data': nrst_pt_df,
        'getFillColor':  [255, 0, 0],
        'getRadius': 250
       },
        {
        'type': 'ScatterplotLayer',
        'data': pt_to_query_df,
        'getFillColor':  [0, 0, 255],
        'getRadius': 250
       },
        ])


curr_lat, curr_long, nrst_pt_df, df, pt_to_query_df = generate_data_start(52.20472, 0.14056, location)
create_map(curr_lat, curr_long, nrst_pt_df, df, pt_to_query_df)
