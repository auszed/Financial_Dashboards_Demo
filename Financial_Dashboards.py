# ---------------------------------
# packages that we will needing

# streamlit run name of the file
import streamlit as st

"""
# Header
## subheader
"""

# or do this
st.title("title")
st.write("write")


# stucture data
some_dictonary = {
    "key":"value",
    "key2":"value2"}
some_list= [1,2,3]

st.write(some_dictonary)
st.write(some_list)

st.sitebar("write_sidebar")
'''
import pandas as pd
# visualization
import plotly
# database postgrade
import psycopg2

# apis this its not working currently
# import request

# api for twitter or x
import tweepy
'''








