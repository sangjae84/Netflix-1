import streamlit as st
import common

common.page_config()

st.title("Netflix : South Korea and USA")
st.caption("""
"Netflix Movies and TV Shows" 데이터셋:
Netflix에서 스트리밍되는 영화와 TV 쇼에 대한 정보를 포함하고 있는 데이터셋입니다. 
이 데이터셋은 Netflix의 다양한 지역에서 제공되는 콘텐츠에 대한 정보를 담고 있으며, 
영화와 TV 쇼의 제목, 감독, 배우, 장르, 관람등급, 국가, 영상 길이, 개봉일 등의 속성을 포함하고 있습니다.

이 데이터셋을 사용하여 한국과 미국의 Netflix 영화와 TV 쇼에 대한 다양한 분석 및 시각화를 수행했습니다. 
""")
st.image("img/welcome.png")
