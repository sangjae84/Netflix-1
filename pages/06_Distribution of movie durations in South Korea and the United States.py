import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import common
import seaborn as sns

common.page_config()

st.title("Distribution of movie durations in South Korea and the United States")

data = common.get_sales()

# Tab 구성
tab1, tab2, tab3 = st.tabs(["South Korea", "United States"," "])

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

