import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 필터링
usa_tv_shows_data = data[(data['country'] == 'United States') & (data['type'] == 'TV Show')]
usa_seasons = usa_tv_shows_data['duration'].str.extract('(\d+)').astype(int)

sk_tv_shows_data = data[(data['country'] == 'South Korea') & (data['type'] == 'TV Show')]
sk_seasons = sk_tv_shows_data['duration'].str.extract('(\d+)').astype(int)

# 그래프 설정
fig, ax = plt.subplots(figsize=(10, 6))
sns.distplot(usa_seasons, bins=30, hist=True, kde=True, color='green', label='USA')
sns.distplot(sk_seasons, bins=30, hist=True, kde=True, color='red', label='South Korea')
plt.title('Distribution of TV Show Durations (Seasons) for Netflix Content')
plt.xlabel('Number of Seasons')
plt.ylabel('Density/Count')
plt.legend()

# Streamlit 앱 설정
st.set_page_config(layout="wide")
st.title('TV Show Durations on Netflix')
st.pyplot(fig)
