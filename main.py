# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:54:36 2021

@author: Robert https://github.com/rdzudzar
"""
# Awesome Streamlit
import streamlit as st

# Add pages -- see those files for deatils within
from page_explore import page_explore
from page_fit import page_fit
from page_introduction import page_introduction
from page_playground import page_playground
from page_profiler import page_profiler
from page_vis import page_vis
from page_dashboard import page_dashboard
from page_close import page_close

# Use random seed
import numpy as np
np.random.seed(1)


# Set the default elements on the sidebar
#st.set_page_config(page_title='Data Analyser')

logo, name = st.sidebar.columns(2)
with logo:
    image = './images/dx.jpeg'
    st.image(image, use_column_width=True)
with name:
    st.markdown("<h1 style='text-align: left; color: grey;'> \
                DXAB </h1>", unsafe_allow_html=True)

st.sidebar.write(" ")


def main():
    """
    Register pages to Explore and Fit:
        page_introduction - contains page with images and brief explanations
        page_explore - contains various functions that allows exploration of
                        continuous distribution; plotting class and export
        page_fit - contains various functions that allows user to upload
                    their data as a .csv file and fit a distribution to data.
    """

    pages = {
        "🍎소개": page_introduction,
        "🍎탐색": page_introduction,
        "1)통계방법 탐색": page_explore,
        "2)데이터 EDA": page_profiler,
        "3)데이터 분포 시각화": page_fit,
        "🍎시각화 차트": page_vis,
        "🍎모델링": page_playground,
        "🍎대시보드": page_dashboard,
        "참고": page_close,
    }

    st.sidebar.title("메뉴")

    # Radio buttons to select desired option
    page = st.sidebar.radio("원하는 메뉴를 선택해주세요", tuple(pages.keys()))
                                
    # Display the selected page with the session state
    pages[page]()

    # # Write About
    # st.sidebar.header("About")
    # st.sidebar.warning(
    #         """
    #         설명설명
    #         """
    # )


if __name__ == "__main__":
    main()
