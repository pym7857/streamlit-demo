# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:25:33 2021

@author: Robert https://github.com/rdzudzar
"""
import streamlit as st

def page_introduction():
    
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    
    st.markdown("<h2 style='text-align: center;'> Welcome To </h2>", 
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> DXAB 👋 </h1>", 
                unsafe_allow_html=True)
    
    image = './images/dxab_main.png'
    st.image(image, use_column_width=True)
     

    st.info("""
            - 누구나 쉽게 짧은 코드로 데이터사이언스 웹앱을 생성할 수 있습니다. 
            - 웹 구성에 필요한 ui들을 메서드 형태로 편리하게 제공하며 배포가 매우 간단합니다.
            """)
    
    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line    

    
    return
