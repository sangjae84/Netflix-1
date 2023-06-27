import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common

common.page_config()

st.title("Number of Movies and TV shows in South Korea and the United States")

df = common.get_sales()

tab1, tab2, tab3 = st.tabs(["South Korea", "United States", "Comparison"])

# Load South Korea and United States data
sk_data = common.load_sk_data()  # Load South Korea data
usa_data = common.load_usa_data()  # Load United States data

with tab1:
    # ''type' 열 기준으로 데이터 분류
    sk_data_counts = sk_data['type'].value_counts()

    # 색상 설정
    colors = ['violet', 'mistyrose']

    # 도넛 차트 그리기
    fig, ax = plt.subplots()
    ax.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90,
           wedgeprops={'edgecolor': 'white', 'width': 0.7}, colors=colors)
    ax.axis('equal')
    ax.set_title('Netflix Shows in South Korea')
    st.pyplot(fig)

with tab2:
    # ''type' 열 기준으로 데이터 분류
    usa_data_counts = usa_data['type'].value_counts()

    # 색상 설정
    colors = ['green', 'mistyrose']

    # 도넛 차트 그리기
    fig, ax = plt.subplots()
    ax.pie(usa_data_counts, labels=usa_data_counts.index, autopct='%1.1f%%', startangle=90,
           wedgeprops={'edgecolor': 'white', 'width': 0.7}, colors=colors)
    ax.axis('equal')
    ax.set_title('Netflix Shows in the United States')
    st.pyplot(fig)

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
    ax.set_xlabel('Type')
    ax.set_ylabel('Count')
    ax.set_title('Netflix Shows Comparison')
    ax.legend()

    # 그래프 출력
    st.pyplot(fig)
