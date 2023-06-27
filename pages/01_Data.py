import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("South Korea-Data")
data = pd.read_csv("./netflix1.csv")
sk_data = data[data['country'] == 'South Korea']
st.write(sk_data)

st.title("United States-Data")
usa_data = data[data['country'] == 'United States']
st.write(usa_data)
