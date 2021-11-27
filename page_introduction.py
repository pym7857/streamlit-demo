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
     

    st.info("""
            - 설명설명
            - 설명설명2
            """)
    
    def make_line():
        """ Line divider between images. """
            
        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                unsafe_allow_html=True)

        return line    

    
    return
