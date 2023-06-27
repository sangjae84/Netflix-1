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

with tab1:
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
# 그래프 제목과 축 레이블 설정
plt.title('Distribution of Movie Durations for Netflix Content')
plt.xlabel('Duration (minutes)')
plt.ylabel('Density')
# 범례 추가
plt.legend()
# 그래프 출력
plt.show()
st.pyplot(plt)
