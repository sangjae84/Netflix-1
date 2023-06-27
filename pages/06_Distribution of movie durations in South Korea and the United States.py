import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_config():
    st.set_page_config(layout="wide")

def get_sales():
    # 데이터를 가져오는 함수
    pass

# Streamlit 앱 설정
page_config()

# 데이터 가져오기
data = get_sales()

# Tab 구성
tabs = ["South Korea", "United States", "EX"]
selected_tab = st.sidebar.selectbox("Select a Country", tabs)

if selected_tab == "South Korea":
    # 한국에서 제작된 영화 데이터 필터링
    sk_movies_data = data[(data['country'] == 'South Korea') & (data['type'] == 'Movie')]
    # 영상 길이 분포 계산
    duration = sk_movies_data['duration'].str.replace(' min', '').astype(int)

    # 그래프 설정
    plt.figure(figsize=(10, 6))
    sns.distplot(duration, bins=30, hist=True, kde=True, color='red')

    # 그래프 제목과 축 레이블 설정
    plt.title('Distribution of Movie Durations for Netflix Content in South Korea')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Density')

    # 그래프 출력
    st.pyplot(plt)

elif selected_tab == "United States":
    # 미국에서 제작된 영화 데이터 필터링
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
    st.pyplot(plt)

else:  # EX 탭
    # 한국에서 제작된 영화 데이터 필터링
    sk_movies_data = data[(data['country'] == 'South Korea') & (data['type'] == 'Movie')]
    # 영상 길이 분포 계산
    duration_sk = sk_movies_data['duration'].str.replace(' min', '').astype(int)

    # 미국에서 제작된 영화 데이터 필터링
    usa_movies_data = data[(data['country'] == 'United States') & (data['type'] == 'Movie')]
    # 영상 길이 분포 계산
    duration_usa = usa_movies_data['duration'].str.replace(' min', '').astype(int)

    # 그래프 설정
    plt.figure(figsize=(10, 6))
    sns.distplot(duration_sk, bins=30, hist=True, kde=True, color='red', label='South Korea')
    sns.distplot(duration_usa, bins=30, hist=True, kde=True, color='green', label='United States')

    # 그래프 제목과
    plt.title('Distribution of Movie Durations for Netflix Content')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Density')
# 범례 추가
    plt.legend()

# 그래프 출력
    st.pyplot(plt)