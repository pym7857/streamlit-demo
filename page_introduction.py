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
    st.markdown("<h1 style='text-align: center;'> DXAB π </h1>", 
                unsafe_allow_html=True)
    
    image = './images/dxab_main.png'
    st.image(image, use_column_width=True)
     

    st.info("""
            - λκ΅¬λ μ½κ² μ§§μ μ½λλ‘ λ°μ΄ν°μ¬μ΄μΈμ€ μΉμ±μ μμ±ν  μ μμ΅λλ€. 
            - μΉ κ΅¬μ±μ νμν uiλ€μ λ©μλ ννλ‘ νΈλ¦¬νκ² μ κ³΅νλ©° λ°°ν¬κ° λ§€μ° κ°λ¨ν©λλ€.
            """)
    
    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line    

    
    return
