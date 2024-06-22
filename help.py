import streamlit as st

#----------------------------------------------------------------------------------
def load_help():
    st.write("""
        <div style="font-size:1.1em">
         <ol>
            <li style="font-size:1.3em; font-weight:bold">Hướng dẫn sử dụng:
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