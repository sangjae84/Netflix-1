import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common

common.page_config()

st.title("Distribution of movie durations in South Korea and the United States")

data = common.get_sales()

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']
