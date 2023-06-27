import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import common
import seaborn as sns

common.page_config()

st.title("Distribution of movie durations in South Korea and the United States")

data = common.get_sales()



# 데이터 필터링
sk_movies_data = data[(data['country'] == 'South Korea') & (data['type'] == 'Movie')]
duration_sk = sk_movies_data['duration'].str.replace(' min', '').astype(int)

usa_movies_data = data[(data['country'] == 'United States') & (data['type'] == 'Movie')]
duration_usa = usa_movies_data['duration'].str.replace(' min', '').astype(int)

# 그래프 설정
fig, ax = plt.subplots(figsize=(10, 6))
plt.hist(duration_sk, bins=30, density=True, alpha=0.5, color='red', label='South Korea')
sns.kdeplot(duration_sk, color='red', label='South Korea')
plt.hist(duration_usa, bins=30, density=True, alpha=0.5, color='green', label='United States')
sns.kdeplot(duration_usa, color='green', label='United States')
plt.title('Distribution of Movie Durations for Netflix Content')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')
plt.legend()

# Streamlit 앱 설정
st.set_page_config(layout="wide")
st.title("Distribution of movie durations in South Korea and the United States")
st.pyplot(fig)
