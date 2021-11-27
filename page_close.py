# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:25:33 2021

@author: Robert https://github.com/rdzudzar
"""
import streamlit as st

def page_close():
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
     
    st.markdown("<h2 style='text-align: center;'> 참고 자료 </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> 링크 📌 </h1>", 
                unsafe_allow_html=True)

    
    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line    



    make_line()
 
    st.info('참고 링크')
        
    st.markdown("""
                
                - Streamlit Gallery:
                
                    - 통계방법 탐색: https://github.com/rdzudzar/DistributionAnalyser
                
                    - 데이터 EDA: https://github.com/baligoyem/dataqtor
                
                    - 데이터 분포 시각화: https://github.com/rdzudzar/DistributionAnalyser
                    
                    - 시각화 차트: https://share.streamlit.io/discdiver/data-viz-streamlit/main/app.py
                
                    - 모델링: https://github.com/ahmedbesbes/playground
                
                    - 대시보드: https://github.com/LarryPrato/projectcontroldashboard
                
                """)
    
    return
