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

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

tab1, tab2, tab3 = st.tabs(["South Korea", "United States"," EX"])
with tab1:
  # 그래프 설정
sk_movies_data = data[(data['country'] == 'South Korea') & (data['type'] == 'Movie')]

# 영상 길이 분포 계산
duration = sk_movies_data['duration'].str.replace(' min', '').astype(int)

# 그래프 설정
plt.figure(figsize=(10, 6))
sns.distplot(duration, bins=30, hist=True, kde=True, color='red')

# 그래프 제목과 축 레이블 설정
plt.title('Distribution of Movie Durations for Netflix Content in the South Korea')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')

# 그래프 출력
plt.show()
st.pyplot(plt)

with tab2:

## 미국에서 제작된 영화 데이터 필터링
usa_movies_data = data[(data['country'] == 'United States') & (data['type'] == 'Movie')]

# 영상 길이 분포 계산
duration = usa_movies_data['duration'].str.replace(' min', '').astype(int)

# 그래프 설정
plt.figure(figsize=(10, 6))
sns.distplot(duration, bins=30, hist=True, kde=True, color='green')

# 그래프 제목과 축 레이블 설정
plt.title('Distribution of Movie Durations for Netflix Content in the United States')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')

# 그래프 출력
plt.show()
st.pyplot(plt)

with tab3:
# 그래프 설정
plt.figure(figsize=(10, 6))
# 한국에서 제작된 영화 데이터 필터링
sk_movies_data = data[(data['country'] == 'South Korea') & (data['type'] == 'Movie')]
# 영상 길이 분포 계산
duration_sk = sk_movies_data['duration'].str.replace(' min', '').astype(int)
# 한국 영화 데이터 그래프 (막대 그래프)
plt.hist(duration_sk, bins=30, density=True, alpha=0.5, color='red', label='South Korea')
sns.kdeplot(duration_sk, color='red', label='South Korea')
# 미국에서 제작된 영화 데이터 필터링
usa_movies_data = data[(data['country'] == 'United States') & (data['type'] == 'Movie')]
# 영상 길이 분포 계산
duration_usa = usa_movies_data['duration'].str.replace(' min', '').astype(int)
# 미국 영화 데이터 그래프 (막대 그래프)
plt.hist(duration_usa, bins=30, density=True, alpha=0.5, color='green', label='United States')
sns.kdeplot(duration_usa, color='green', label='United States')
# 그래프 제목과 축 레이블 설정
plt.title('Distribution of Movie Durations for Netflix Content')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')
# 범례 추가
plt.legend()
# 그래프 출력
plt.show()
st.pyplot(plt)