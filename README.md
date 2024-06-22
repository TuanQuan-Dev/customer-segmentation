
# Customer Segmentation




## 1. Giới thiệu đề tài
Chúng tôi phân nhóm cho 3898 khách hàng trong tập dữ liệu thành 3 nhóm:
- REGULARS: Khách hàng thường xuyên mua hàng
- ACTIVE: Khách hàng thỉnh thoảng mua hàng
- NEW: Khách hàng mới

## 2. Hướng dẫn sử dụng
### 2.1. Khám phá dữ liệu
Cung cấp cho chủ cửa hàng 1 góc nhìn về tình hình kinh doanh gồm 3 mục chính:
- Tổng quan: Thời gian nghiên cứu, số lượng khách hàng và sản phẩm
- Khách hàng: Số lượng khách hàng theo tháng, tuần suất mua hàng
- Sản phẩm: Những sản phẩm đặc trưng của shop, số lượng sản phẩm được mua mỗi ngày
![alt text](https://vpwmshmwlfovljzendiw.supabase.co/storage/v1/object/public/FarmerAssociation/StorePicture/Screenshot_2024-06-22_091936.png?t=2024-06-22T02%3A23%3A34.869Z)
### 2.2. Kết quả
Dựa vào nguồn dữ liệu cung cấp, hệ thống tiến hành phân nhóm khách hàng và hiển thị kết quả phân nhóm
![alt text](https://vpwmshmwlfovljzendiw.supabase.co/storage/v1/object/public/FarmerAssociation/StorePicture/Screenshot_2024-06-22_092827.png?t=2024-06-22T02%3A28%3A48.226Z)
### 2.3. Tra cứu
Nhập id (Các id ví dụ: 1000, 1001, 1002, 1003, 1004) của khách hàng vô hệ thống sẽ hiện:  
- Nhóm khách hàng 
- Tần suất mua hàng 
- Số lượt mua hàng 
- Tổng giá trị đơn hàng 
- Sản phẩm khách hàng hay mua
![alt text](https://vpwmshmwlfovljzendiw.supabase.co/storage/v1/object/public/FarmerAssociation/StorePicture/Screenshot_2024-06-22_093121.png?t=2024-06-22T02%3A31%3A47.384Z)






## 3. Cấu trúc ứng dụng
- **homepage.py:** viết nội dung trang home
- **help.py:** viết nội dung trang hướng dẫn
- **data.py:** xử lý nguồn dữ liệu, phân nhóm khác hàng. Dữ liệu sau khi phân nhóm được lưu trong file **customer_rfm.csv** trong thư mục output_data
- **GUI.py:** file chính của giao diện, thiết kế giao diện của web, vẽ biểu đồ