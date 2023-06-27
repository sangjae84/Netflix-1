import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import common
import seaborn as sns

common.page_config()

st.title("Distribution of movie durations in South Korea and the United States")

data = common.get_sales()

#한국에서 제작된 영화 데이터 필터링
sk_movies_data = data[(data['country'] == 'South Korea') & (data['type'] == 'Movie')]
sk_durations = sk_movies_data['duration'].str.extract('(\d+)').astype(int)

#미국에서 제작된 영화 데이터 필터링
usa_movies_data = data[(data['country'] == 'United States') & (data['type'] == 'Movie')]
usa_durations = usa_movies_data['duration'].str.extract('(\d+)').astype(int)

#Tab 구성
tab1, tab2, tab3 = st.columns(3)

with tab1:
# 그래프 설정 (한국 영화)
plt.figure(figsize=(10, 6))
sns.histplot(sk_durations, bins=30, color='red', kde=True)
plt.title('Distribution of Movie Durations for Netflix Content in South Korea')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')
st.pyplot(plt)

with tab2:
# 그래프 설정 (미국 영화)
plt.figure(figsize=(10, 6))
sns.histplot(usa_durations, bins=30, color='green', kde=True)
plt.title('Distribution of Movie Durations for Netflix Content in the United States')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')
st.pyplot(plt)

with tab3:
# 그래프 설정 (한국 vs. 미국 영화)
plt.figure(figsize=(10, 6))
sns.histplot(sk_durations, bins=30, color='red', kde=True, label='South Korea')
sns.histplot(usa_durations, bins=30, color='green', kde=True, label='United States')
plt.title('Distribution of Movie Durations for Netflix Content')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')
plt.legend()
st.pyplot(plt)