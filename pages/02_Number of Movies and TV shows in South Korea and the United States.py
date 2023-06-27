import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common

common.page_config()

st.title("Number of Movies and TV shows in South Korea and the United States")

df = common.get_sales()

tab1, tab2, tab3 = st.tabs(["South Korea", "United States", "Comparison"])

#''type' 열 기준으로 데이터 분류
sk_data_counts = sk_data['type'].value_counts()
 #색상 설정
colors = ['violet', 'mistyrose']

with tab1:
   #도덧 차트 그리기
   plt.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
   plt.axis('equal')
   plt.title('Netflix Shows in the South Korea')
   plt.show()

#''type' 열 기준으로 데이터 분류
usa_data_counts = usa_data['type'].value_counts()
#색상 설정
colors = ['green', 'mistyrose']
  
with tab2:   
  #도덧 차트 그리기
  plt.pie(usa_data_counts, labels=usa_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
  plt.axis('equal')
  plt.title('Netflix Shows in the United States')
  plt.show()

with tab3:
   # 'type' 열 기준으로 데이터 분류
  sk_data_counts = sk_data['type'].value_counts()
  usa_data_counts = usa_data['type'].value_counts()
  # 그래프 영역 설정
  fig, ax = plt.subplots()
  # South Korea 그래프 그리기
  ax.plot(sk_data_counts.index, sk_data_counts, marker='o', linestyle='-', color='violet', label='South Korea')
  # United States 그래프 그리기
  ax.plot(usa_data_counts.index, usa_data_counts, marker='o', linestyle='-', color='green', label='United States')
  # 축과 제목 설정
  plt.xlabel('Type')
  plt.ylabel('Count')
  plt.title('Netflix Shows Comparison')
  plt.legend()
  # 그래프 출력
  plt.show()
