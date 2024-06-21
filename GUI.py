import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_multi_menu import streamlit_multi_menu
from data import SalesData


#streamlit run gui.py

# Dữ liệu 
myData = SalesData()
#myData.pre_proccess()
myData.load()
#myData.product_R(myData.Data)

st.title("DỰ ÁN - PHÂN NHÓM KHÁCH HÀNG")
st.write("<br/>", unsafe_allow_html=True)

menu = ["Home", "Khám Thác Dữ Liệu", "Chua ghi"]


with st.sidebar:
    choice = option_menu("",options=menu, 
        icons=["home", "gear", "gear", "file"], menu_icon="cast", default_index=0)


#----------------------------------------------------------------------------------
def CSS():
    st.markdown("""<style>
                    .item {border: solid 1px; height:350px; margin-bottom:10px; font-size:1em; padding:3px}
                    .title {font-weight: bold; font-size:1.3em;}
                    .review {font-weight: bold;}
                    .star {font-weight: bold;}
                    .level {font-weight: bold;}
                </style>""", unsafe_allow_html=True)
           

#----------------------------------------------------------------------------------
def DNA():
    #st.header("KHAI THÁC DỮ LIỆU") 
      
    sub_menus = {"Tổng Quan":["Xem"],
             "Khách Hàng":["Khách Hàng"], 
             "Sản Phẩm":["Sản Phẩm"]}
    
    sub_menu_icons = {
        "Tổng Quan": ["trending_up"], 
        "Khách Hàng": ["directions_car", "garage"], 
        "Sản Phẩm": ["restaurant", "local_cafe", "kitchen"]}
    
    selected_menu = streamlit_multi_menu(menu_titles=list(sub_menus.keys()), sub_menus=sub_menus,
                            use_container_width=True)

   
            
    
        
#----------------------------------------------------------------------------------

CSS()
if choice == "Home":
    st.header("HOME")
    
    
elif choice.lower() == "khám thác dữ liệu":
    st.header("VỀ ỨNG DỤNG RECOMMENDER SYSTEMS")
    DNA()   

elif choice.lower() == "read-me":
    st.header("VỀ ỨNG DỤNG RECOMMENDER SYSTEMS")
    
    st.write("""
            <div style="font-size:1.2em">
                Hệ thống được chia làm 2 phần:<br/>
                <ol>
                    <li><b>Người dùng chưa có tài khoản (Content-based filtering)</b>
                        <div style="font-size:1.1em">
                            <ul>
                                <li>
                                    Khi người sử dụng không nhập gì vào ô tìm kiếm, hệ thống tự gợi ý 6 khóa học cho học viên
                                </li>
                                <li>
                                    Nếu nhập vào ô tìm kiếm, hệ thống sẽ gợi ý các khóa học liên quan tới từ gợi ý trên. 
                                    Như tên khóa học, đơn vị đào tạo, trình độ, kết quả khóa học
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li><b>Người dùng đã có tài khoản (Collaborative filtering)</b>
                        <div style="font-size:1.1em">
                            Hệ thống dựa vào lịch sử đánh giá của học viên về các khóa đã học để đề xuất cho học viên các khóa học phù hợp                                                            
                        </div>
                    </li>
                    <li><b>Các thành viên trong nhóm</b>
                        <ul>
                            <li>Thái Tuấn Quân</li>
                            <li>Lê Thị Hương Quỳnh</li>
                            <li>Huỳnh Chí Tài</li>
                        </ul>
                    </li>
                </ol>
            </div> 
            """, unsafe_allow_html=True)
    


