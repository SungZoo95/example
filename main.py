import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image
import matplotlib.pyplot as plt



st.title("정시 등급 컷 합격예측 서비스:mortar_board:")

st.markdown("-------")


st.subheader("생각하게 된 이유")
st.markdown('''정시등급컷 예측으로는 진학사,메가스터디,대성마이맥등이 있습니다''')
if st.checkbox("정시 합격 예측링크"):
    st.markdown("진학사")
    st.markdown("https://www.jinhak.com/")
    st.markdown("대성마이맥")
    st.markdown("https://www.mimacstudy.com/ex/ipsi/salesBaechi/2022/1011/830593_indexfull.ds")
    st.markdown("메가스터디")
    st.markdown("https://www.megastudy.net/Entinfo/2023_jungsi/exam/ready/0519/main2.asp")

st.markdown('''하지만 가입이 필요하거나 예측의 불확실성이 높아보였고 예측모델을 생성하면 기존 사이트들보다 더욱 
            유의미하고 정확한결과를 얻을 수 있지 않을까 생각하여 구상해봤습니다.''')

st.subheader("제일 중요한 데이터")
st.markdown("아직 찾지 못함")
st.markdown("https://www.kedi.re.kr/khome/main/research/eduNavi.do")
st.markdown("https://kess.kedi.re.kr/post/1012774?itemCode=06&menuId=m_02_06_02")
st.markdown("https://kostat.go.kr/unifSearch/search.es")
st.markdown("https://kess.kedi.re.kr/kessTheme/webzine?itemCode=03&menuId=m_02_03_04")
st.markdown("https://edpolicy.kedi.re.kr/frt/boardList.do?strCurMenuId=10105")
st.markdown("https://www.adiga.kr/PageLinkAll.do?link=/kcue/ast/eip/eis/inf/sjinf/eipSjinfGnrl.do&p_menu_id=PG-EIP-05101")
st.markdown("https://www.data.go.kr/data/15001549/fileData.do#/API%20%EB%AA%A9%EB%A1%9D/getuddi:8e16e52b-b545-4d78-8dbd-9e41e29918e3_201711291453")

st.subheader("과정설명")
st.markdown("데이터 수집(대학 등급별 커트라인)--> 데이터 전처리 --> 딥러닝 모델에 다음 년도 커트라인 예측모델 학습 --> 합격/실패 여부를 판단하는 분류 모형 사용")
