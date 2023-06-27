import streamlit as st
import matplotlib.pyplot as plt
import common

common.page_config()

st.title("Number of Movies and TV shows in South Korea and the United States")

# South Korea 데이터 필터링
sk_data = df[df['country'] == 'South Korea']
sk_data_counts = sk_data['type'].value_counts()

# United States 데이터 필터링
usa_data = df[df['country'] == 'United States']
usa_data_counts = usa_data['type'].value_counts()

# Tab 구성
tab1, tab2, tab3 = st.columns(3)

with tab1:
    fig1, ax1 = plt.subplots()
    ax1.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90,
            wedgeprops={'edgecolor': 'white', 'width': 0.7}, colors=['violet', 'mistyrose'])
    ax1.axis('equal')
    ax1.set_title('Netflix Shows in South Korea')
    st.pyplot(fig1)

with tab2:
    fig2, ax2 = plt.subplots()
    ax2.pie(usa_data_counts, labels=usa_data_counts.index, autopct='%1.1f%%', startangle=90,
            wedgeprops={'edgecolor': 'white', 'width': 0.7}, colors=['green', 'mistyrose'])
    ax2.axis('equal')
    ax2.set_title('Netflix Shows in the United States')
    st.pyplot(fig2)

with tab3:
    fig3, ax3 = plt.subplots()
    ax3.plot(sk_data_counts.index, sk_data_counts, marker='o', linestyle='-', color='violet', label='South Korea')
    ax3.plot(usa_data_counts.index, usa_data_counts, marker='o', linestyle='-', color='green', label='United States')
    ax3.set_xlabel('Type')
    ax3.set_ylabel('Count')
    ax3.set_title('Netflix Shows Comparison')
    ax3.legend()
    st.pyplot(fig3)
