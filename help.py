import streamlit as st

#----------------------------------------------------------------------------------
def load_help():
    st.write("""
        <div style="font-size:1.1em">
         <ol>
            <li style="font-size:1.3em; font-weight:bold">Hướng dẫn sử dụng:
                <ul>
                    <li>Khám phá dữ liệu: cung cấp cho chủ cửa hàng 1 góc nhìn về tình hình kinh doanh</li>
                    <li>Kết quả: dựa vào nguồn dữ liệu cung cấp, hệ thống tiến hành phân nhóm khách hàng <br/>
                        Hiển thị kết quả phân nhóm
                    </li>
                    <li>
                        Tra Cứu: tìm thông tin khách hàng
                    </li>
                </ul>
            </li> 
            <li style="font-size:1.3em; font-weight:bold">Cấu trúc ứng dụng
                <ul>
                    <li><b>homepage.py:</b> viết nội dung trang home</li>
                    <li><b>help.py:</b> viết nội dung trang hướng dẫn</li>
                    <li><b>data.py:</b> xử lý nguồn dữ liệu, phân nhóm khác hàng
                        Dữ liệu sau khi phân nhóm được lưu thành file <i><b>customer_rfm.csv</b></i> trong thư mục output_data
                    </li>
                    <li><b>GUI.py:</b> file chính của giao diện, thiết kế giao diện của web, vẽ biểu đồ</li>
                </ul>
            </li>                        
        </ol>
        </div> 
        """         
         , unsafe_allow_html=True)   