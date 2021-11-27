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
                
                    - 탐색1 (통계 방법 소개): https://github.com/rdzudzar/DistributionAnalyser
                
                    - 탐색2 (Data Profiler): https://github.com/baligoyem/dataqtor
                
                    - 탐색3 (분포 시각화): https://github.com/rdzudzar/DistributionAnalyser
                
                    - 모델링: https://github.com/ahmedbesbes/playground
                
                    - 대시보드: https://github.com/LarryPrato/projectcontroldashboard
                
                """)
    
    return
