# 📊 Phân Tích Điểm Thi Các Vùng Ở Việt Nam

## 📝 **Giới Thiệu**  
Dự án này thực hiện việc **thu thập**, **làm sạch**, và **phân tích dữ liệu điểm thi** từ 5 vùng ngẫu nhiên tại Việt Nam. Mục tiêu là so sánh và trực quan hóa sự khác biệt về kết quả điểm thi giữa các vùng thông qua các biểu đồ.

---

## 🎯 **Mục Tiêu Dự Án**  
- 🌐 **Crawl dữ liệu điểm thi** từ các vùng được chọn.  
- 📂 **Xây dựng mẫu số chung** để đồng nhất dữ liệu giữa các vùng.  
- 🛠️ **Làm sạch dữ liệu**: Loại bỏ dữ liệu không hợp lệ và xử lý giá trị khuyết thiếu.  
- 📈 **Trực quan hóa**: Tạo các biểu đồ minh họa kết quả điểm thi.

---

## 🛠️ **Công Cụ và Công Nghệ Sử Dụng**  
- **Ngôn ngữ lập trình**: Python  
- **Thư viện chính**:  
  - 🔍 `BeautifulSoup`, `requests` để crawl dữ liệu.  
  - 🧮 `pandas`, `numpy` để xử lý dữ liệu.  
  - 📊 `matplotlib`, `seaborn` để trực quan hóa dữ liệu.  
- **Quy trình làm sạch dữ liệu**:  
  - Loại bỏ dữ liệu không hợp lệ.  
  - Xử lý ngoại lệ và giá trị khuyết thiếu.  
  - Chuẩn hóa định dạng dữ liệu.

---

## 📂 **Quy Trình Thực Hiện**  
1. 🎯 **Chọn vùng và crawl dữ liệu**  
   - Lựa chọn ngẫu nhiên 5 vùng từ các miền khác nhau ở Việt Nam.  
   - Sử dụng Python để crawl dữ liệu từ các trang web.  

2. 🛠️ **Làm sạch dữ liệu**  
   - Loại bỏ dữ liệu trùng lặp hoặc không hợp lệ.  
   - Chuẩn hóa các trường thông tin như mã vùng, tên môn thi, và kết quả điểm.  

3. 📊 **Trực quan hóa và so sánh**  
   - Sử dụng biểu đồ cột, biểu đồ tròn, và biểu đồ đường để minh họa.  
   - So sánh các yếu tố như:  
     - Điểm trung bình.  
     - Phân bố điểm.  
     - Mức độ dao động giữa các vùng.  

---

## 🔍 **Kết Quả Dự Kiến**  
- ✅ Biểu đồ minh họa sự khác biệt điểm thi giữa các vùng.  
- 📌 Phân tích chuyên sâu giúp nhận diện các yếu tố ảnh hưởng đến kết quả thi. 

### 📈 Hình ảnh trực quan hóa dữ liệu:
#### Biểu đồ số lượng thí sinh tham gia từng môn:
![SLthisinhthamgiatungmon](https://github.com/user-attachments/assets/861cb090-897e-4ba5-bda3-79232cbb6d16)
![phổ_điểm_các_môn](https://github.com/user-attachments/assets/3c010c71-d39f-4f53-8d46-71125fb4b087)
![Tỷ lệ thí sinh không thi theo số môn](https://github.com/user-attachments/assets/de67a5ea-6fae-462f-9600-e80fa562cc56)

---

✨ **Thanks for reading!** ✨
