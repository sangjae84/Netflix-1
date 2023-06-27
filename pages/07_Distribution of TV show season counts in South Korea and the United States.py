import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 미국에서 제작된 TV 쇼 데이터 필터링
usa_tv_shows_data = data[(data['country'] == 'United States') & (data['type'] == 'TV Show')]
# 영상 길이 분포 계산
usa_seasons = usa_tv_shows_data['duration'].str.extract('(\d+)').astype(int)
# 한국에서 제작된 TV 쇼 데이터 필터링
sk_tv_shows_data = data[(data['country'] == 'South Korea') & (data['type'] == 'TV Show')]
# 영상 길이 분포 계산
sk_seasons = sk_tv_shows_data['duration'].str.extract('(\d+)').astype(int)

# 그래프 설정
plt.figure(figsize=(10, 6))
sns.distplot(usa_seasons, bins=30, hist=True, kde=True, color='green', label='USA')
sns.distplot(sk_seasons, bins=30, hist=True, kde=True, color='red', label='South Korea')
# 그래프 제목과 축 레이블 설정
plt.title('Distribution of TV Show Durations (Seasons) for Netflix Content')
plt.xlabel('Number of Seasons')
plt.ylabel('Density/Count')
# 범례 추가
plt.legend()

# Streamlit 앱 설정
st.set_page_config(layout="wide")
st.title('TV Show Durations on Netflix')
st.pyplot(plt)
