
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
from streamlit_option_menu import option_menu

#streamlit run gui.py


st.title("DỰ ÁN - PHÂN NHÓM KHÁCH HÀNG")
st.write("<br/><br/>", unsafe_allow_html=True)

menu = ["Home", "Content-based", "Collaborative"]


with st.sidebar:
    choice = option_menu("",options=["Home", "Content-based", "Collaborative", "Read-me"], 
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
def homepage():
    st.write("""
        <div style="font-size:1.1em">
         <ol>
            <li style="font-size:1.3em; font-weight:bold">Phân tích nhu cầu:
                <ul>
                    <li>Tạo ra các chiến dịch tiếp thị hiệu quả</li>
                    <li>Giữ chân khách hàng: tạo chính sách đặc biệt cho khách hàng         
                        quan trọng và thu hút lại khách hàng đã mua hàng trong quá khứ.</li>
                    <li>
                        Cải tiến dịch vụ: hiểu rõ nhu cầu khách hàng để điều chỉnh và tối
                        ưu hóa dịch vụ, nâng cao sự hài lòng.
                    </li>
                    <li>
                        Tăng doanh thu: tập trung nguồn lực vào phân khúc khách hàng
                        có lợi nhuận cao, dẫn đến tăng doanh thu và giảm chi phí bán hàng.
                    </li>
                </ul>
            </li> 
            <li style="font-size:1.3em; font-weight:bold">Thực hiện
                <ul>
                Thu thập và phân tích dữ liệu mua hàng của khách hàng <br/>
                Xác định các tiêu chí để phân nhóm khách hàng.                
                </ul>
            </li>
            </li> 
            <li style="font-size:1.3em; font-weight:bold">Lợi ích<br/>                
                <ul>
                    <li>Tiếp thị tốt hơn
                        <div>
                            Khách hàng đã được phân nhóm cho phép cửa hàng đưa ra các chiến dịch tiếp thị quảng
                            cáo tập trung hơn, đúng vào yêu cầu của khách hàng
                        <div>
                    </li>
                    <li>Khả năng mở rộng
                        <div>
                            Cửa hàng hiểu rõ hơn về những sản phẩm mà khách hàng quan tâm. Từ đó mở rộng sản phẩm và dịch vụ 
                            mới phù hợp với đối tượng mục tiêu
                        </div>
                    </li>
                    <li>Giữ chân khách hàng
                        <div>
                            Xác định được khách hàng tiềm năng, giữ chân họ bằng những chương trình tiếp thị hiệu quả
                        </div>
                    </li>
                </ul>
            </li>
        </ol>
        </div> 
        """         
         , unsafe_allow_html=True)              

#----------------------------------------------------------------------------------
def Contentbased():
    st.header("CONTENT-BASED FILTERING") 
       

    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()

    st.pyplot(plt.gcf())
    pass
        
               
#----------------------------------------------------------------------------------
def Collaborative():
    st.header("COLLABORATIVE FILTERING")       
    pass
        
#----------------------------------------------------------------------------------

CSS()
if choice == 'Home':
    homepage()
    
elif choice.lower() == 'content-based':
    Contentbased()
    

elif choice.lower() == "collaborative":
    Collaborative()
    #optUser = st.selectbox("**Please select user:**", mysurprise.user())    

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
    


