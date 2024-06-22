import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
#import plotly.express as px
from wordcloud import WordCloud

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_multi_menu import streamlit_multi_menu
from data import SalesData
from homepage import load_homepage

#streamlit run gui.py

# Dữ liệu 
myData = SalesData()
myData.load()
#myData.pre_proccess()
#myData.product_R(myData.Data)
myData.customer_RFM()

st.title("ĐỒ ÁN - PHÂN NHÓM KHÁCH HÀNG")
st.write("<br/>", unsafe_allow_html=True)

menu = ["Home", "Khám Phá Dữ Liệu", "Kết Quả", "Tra Cứu", "Hướng Dẫn"]


with st.sidebar:
    choice = option_menu("",options=menu, 
        icons=["home", "file", "list-task", "search", "info-square"], menu_icon="cast", default_index=0)


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

    if selected_menu != None:        
        if (selected_menu.lower() == "xem"):
            # <li style="font-size:1.3em; font-weight:bold">Tổng quan dữ liệu:
            #     <ul>
            #         Tổng sản phẩm: <b>{myData.Product.shape[0]}</b>         
            #         Tổng sản phẩm: <b>{myData.Product.shape[0]}</b>
            #     </ul>
            # </li>            

            st.write(f"""
                <div style="font-size:1.1em">
                 <ol>
                    <li style="font-size:1.3em; font-weight:bold">Tổng quan dữ liệu:
                        <ul>
                            <span>Thời gian phân tích từ ngày <b>01/01/2014</b> đến <b>30/12/2015</b> </span><br/>
                            <span>Tổng sản phẩm: <b>{myData.Product.shape[0]}</b></span>, tất cả các sản phẩm đều có giao dịch <br/>
                            <span>Tổng số khách hàng có mua hàng: <b>{myData.Transaction["member_number"].nunique()}</b></span>                           
                        </ul>
                    </li>                     
                </ol>
                </div> 
                """
                 , unsafe_allow_html=True)
    
        elif (selected_menu.lower() == "khách hàng"):
            st.write("""<div style="font-size:1.3em; font-weight:bold">1. Số lượng khách hàng mua hàng theo tháng</div>""", unsafe_allow_html=True)
            
            df = myData.Transaction
                        
            df["month"] = df["order_date"].apply(lambda x: x.strftime("%Y-%m-01"))
            df["string_month"] = df["order_date"].apply(lambda x: x.strftime("%Y-%m"))
            df = df.groupby(["month", "string_month", "member_number"]).nunique().reset_index()[["month", "string_month", "member_number", "orderId"]]            
            df = df.groupby(["month", "string_month"])[["member_number", "orderId"]].count().reset_index()
            df = df.sort_values("month")
            df = df.sort_values("month")
            
            x = df["string_month"]
            y = df["member_number"]
                        
            plt.figure(figsize=(12, 6))
            plt.plot(x, y, linestyle='-')
            plt.title("Số lượng khách mua hàng trong tháng")
            plt.xlabel("Năm - Tháng")
            plt.ylabel("Số lượng khách mua hàng")
            plt.xticks(rotation = 45)
            # Show the plot
            st.pyplot(plt)
            st.write("""<div><b>Theo xu hướng số lượng khách hàng tới cửa hàng giảm, 
                    cũng tương đương số lượng đơn hàng giảm</b></div>""", unsafe_allow_html=True)
            
            #-------------------------------------------------------------------------------------
            st.write("""<div style="font-size:1.3em; font-weight:bold">2. Tần suất mua hàng của khách hàng</div>""", unsafe_allow_html=True)
            
            x = myData.RFM["member_number"]
            y = myData.RFM["Recency"]
            plt.figure(figsize=(12, 6))      
            plt.scatter(x, y, alpha=0.5)
            plt.tick_params(labelbottom = False, bottom = False) 
            st.pyplot(plt)
            st.write("")

            plt.figure(figsize=(12, 6))
            plt.boxplot(y)
            st.pyplot(plt)

            st.write("""<div><b>Tần suất mua hàng của khách hàng tập trung từ 100 ngày đến 200 ngày</b></div>""", unsafe_allow_html=True)
            st.write("")
            
            st.write("""<div><b>10 khách hàng có tần suất mua hàng cao nhất</b></div>""", unsafe_allow_html=True)
            st.write(myData.RFM.sort_values("Recency").head(10))
            
            st.write("""<div><b>10 khách hàng có tần suất mua hàng thấp nhất</b></div>""", unsafe_allow_html=True)
            st.write(myData.RFM.sort_values("Recency", ascending=False).head(10))
            
            st.write(f"""<div><b>Số lượng khách hàng có tần suất mua hàng 1 tháng (1 tháng quay lại mua hàng 1 lần): {myData.RFM[myData.RFM["Recency"] < 31]["member_number"].count()}</b></div>""", unsafe_allow_html=True)
            st.write("")
            st.write("Khách hàng thường xuyên của cửa hàng rất ít", unsafe_allow_html=True)
            
        elif (selected_menu.lower() == "sản phẩm"):
            
            text = " ".join(myData.Data["productName"])
            wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
                        
            st.write(f"""<div>Dựa vào kết quả wordcloud những sản phẩm của hàng thường bán là:
                     milk, rolls buns, root vegatables, fruit tropical, yogurt <br/>
                     Tuy nhiên sẽ cần tìm hiểu thêm tần suất các sản phẩm được bán như thế nào?</div>""", unsafe_allow_html=True)            
            st.write()
            
            df = pd.read_csv("output_data/product_r.csv")
            x = df["productName"]
            y = df["Recency"]
            plt.figure(figsize=(12, 6))      
            plt.scatter(x, y, alpha=0.5)
            plt.tick_params(labelbottom = False, bottom = False) 
            st.pyplot(plt)
            st.write("")

            plt.figure(figsize=(12, 6))
            plt.boxplot(y)
            st.pyplot(plt)
            
            plt.figure(figsize=(12, 6))
            sns.distplot(y)            
            st.pyplot(plt)
            
            st.write(f"""<div>Có nhiều sản phẩm được mua mỗi ngày.</div><br/>""", unsafe_allow_html=True)
            text = " ".join(df[df["Recency"]<=2]["productName"])
            wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
            
            st.write(f"""<div>Danh sách sản phẩm được mua với tần suất 7 ngày/ lần</div>""", unsafe_allow_html=True)                            
            text = " ".join(df[df["Recency"]<=7]["productName"])
            wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)
            
            st.write(f"""<div>Danh sách sản phẩm được mua với tần suất 1 tháng / lần</div>""", unsafe_allow_html=True)
                            
            text = " ".join(df[df["Recency"]<=30]["productName"])
            wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            st.pyplot(plt)            
    

#----------------------------------------------------------------------------------
def RFM():    
            
    st.write(f"""
        <div style="font-size:1.1em">
            Tập khách hàng được phân thành 3 nhóm
        </div> 
        """
        , unsafe_allow_html=True)
    
    df = pd.read_csv("output_data/customer_rfm.csv")
    rfm_agg = df.groupby("RFM_Level").agg({
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": ["mean", "count"]}).round(0)

    rfm_agg.columns = rfm_agg.columns.droplevel()
    rfm_agg.columns = ["RecencyMean", "FrequencyMean", "MonetaryMean", "Count"]
    rfm_agg["Percent"] = round((rfm_agg['Count']/rfm_agg.Count.sum())*100, 2)

    # Reset the index
    rfm_agg = rfm_agg.reset_index()
    
    fig = plt.gcf()
    ax = fig.add_subplot()
    fig.set_size_inches(16, 10)

    colors_dict = {"ACTIVE":"red", "NEW":"green", "REGULARS":"blue" }

    squarify.plot(sizes=rfm_agg["Count"],
                  text_kwargs={"fontsize":12, "weight":"bold", "fontname":"sans serif"},
                  color=colors_dict.values(),
                  label=['{} \n{:.0f} days \n{:.0f} orders \n{:.0f} $ \n{:.0f} customers ({}%)'.format(*rfm_agg.iloc[i])
                          for i in range(0, len(rfm_agg))], alpha=0.5 )

    #plt.title("PHÂN NHÓM KHÁCH HÀNG", fontsize=26, fontweight="bold")
    plt.axis("off")
    
    st.pyplot(plt)
           
    # fig = px.scatter(rfm_agg, x="RecencyMean", y="MonetaryMean", size="FrequencyMean", color="RFM_Level", 
    #      color_discrete_map=colors_dict, hover_name="RFM_Level", size_max=100)        
    # st.plotly_chart(fig)
    
    # Doanh số bán theo từng phân nhóm 
    st.write("""<div style=font-size:1.3em; font-weight:bold>Danh số theo phân nhóm</div>""", unsafe_allow_html=True)  

    plt.figure(figsize=(6, 4))    
    df = myData.RFM.groupby("RFM_Level")["Monetary"].sum().reset_index()
    total = sum(df["Monetary"])
    df["Monetary_percentage"] = round(df["Monetary"] * 100 / total, 0)
    labels = df["RFM_Level"]
    sizes = df["Monetary_percentage"]
    colors = ["red", "green", "blue"]
    
    p, tx, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct="")

    for i, a in enumerate(autotexts):
        a.set_text(f"{sizes[i]} %")
    st.pyplot(plt)
        
        
#----------------------------------------------------------------------------------
def search():
    
    customer = st.text_input("""*** Vui lòng nhập id khách hàng:""")
    if (customer == ""):
        return
    
    st.write("")
    df = myData.RFM[myData.RFM["member_number"] == int(customer)]
    if (df.shape[0] == 0):
        st.warning("ID đã nhập không đúng.")
        return
    
    st.write(f"""<div style=font-size:1.3em; font-weight:bold>Khách hàng này thuộc nhóm <b>{df["RFM_Level"].values[0]}</b><br/>
            Tần suất mua hàng: <b>{df["Recency"].values[0]}</b> <br/>
            Số lượt mua hàng (nếu trong 1 ngày mua nhiều lần chỉ tính 1): <b>{df["Frequency"].values[0]}</b> <br/>
            Tổng giá trị đơn hàng: <b>{df["Monetary"].values[0]}</b> <br/>
            Sản phẩm hay mua
             </div>""", unsafe_allow_html=True) 
        
    df = myData.Data[myData.Data["member_number"] == int(customer)]
    text = " ".join(df["productName"])
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
    
    pass

#----------------------------------------------------------------------------------

CSS()
if choice == "Home":
   load_homepage()
    
    
elif choice.lower() == "khám phá dữ liệu":
    st.header("VỀ ỨNG DỤNG RECOMMENDER SYSTEMS")
    DNA()

elif choice.lower() == "kết quả":
    st.header("KẾT QUẢ PHÂN NHÓM KHÁCH HÀNG")
    RFM() 
    
elif choice.lower() == "tra cứu":
    st.header("TRA CỨU THÔNG TIN KHÁCH HÀNG")
    
    search() 

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
    


