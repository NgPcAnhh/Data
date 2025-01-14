## 📝 **Giới Thiệu**  
Dự án này sử dụng dữ liệu lịch sử chứng khoán của **4 mã cổ phiếu** để:  
1. Vẽ biểu đồ nến minh họa biến động giá mở cửa, đóng cửa, giá cao nhất, và thấp nhất.  
2. Biểu diễn khối lượng giao dịch bên dưới biểu đồ nến để cung cấp cái nhìn toàn diện hơn về xu hướng thị trường.  
3. Định hướng áp dụng **Machine Learning** để dự đoán giá cổ phiếu ngắn hạn dựa trên **Volume** và **Close Price**.  

### 📋 **Danh sách mã cổ phiếu**  
- **FPT**: Tập đoàn FPT.  
- **MSN**: Công ty CP Tập đoàn Masan.  
- **VIC**: Tập đoàn Vingroup.  
- **PNJ**: Công ty CP Vàng bạc Đá quý Phú Nhuận.  

---

## 🎯 **Mục Tiêu Dự Án**  
- 📈 **Phân tích dữ liệu lịch sử chứng khoán**:  
  - Vẽ biểu đồ nến minh họa biến động giá.  
  - Minh họa khối lượng giao dịch tương ứng.  

- 🤖 **Định hướng phát triển**:  
  - Sử dụng Machine Learning để **dự đoán giá ngắn hạn** dựa trên:  
    - Giá đóng cửa (`Close`).  
    - Khối lượng giao dịch (`Volume`).  

---

## 🛠️ **Công Cụ và Công Nghệ Sử Dụng**  
- **Ngôn ngữ lập trình**: Python  
- **Thư viện chính**:  
  - 📚 `pandas`: Xử lý và phân tích dữ liệu.  
  - 🎨 `matplotlib`: Trực quan hóa dữ liệu.  
  - 🕹️ `mplfinance`: Vẽ biểu đồ nến.  
  - 🤖 `scikit-learn`: Phát triển mô hình Machine Learning (định hướng tương lai).  

---

## 📂 **Quy Trình Thực Hiện**  

### 1️⃣ **Xử Lý Dữ Liệu**  
- Dữ liệu đầu vào:  
  - File CSV chứa các cột: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`.  
- Các bước xử lý:  
  1. **Đọc dữ liệu**: Sử dụng `pandas` để tải dữ liệu từ file CSV.  
  2. **Định dạng ngày tháng**:  
     - Chuyển cột `Date` sang định dạng `datetime`.  
     - Thiết lập `Date` làm chỉ mục.  
  3. **Kiểm tra dữ liệu**: Loại bỏ các giá trị bị thiếu hoặc không hợp lệ.  

### 2️⃣ **Trực Quan Hóa Dữ Liệu**  
- **Vẽ biểu đồ nến** với các thông tin:  
  - Giá mở cửa (`Open`), giá cao nhất (`High`), giá thấp nhất (`Low`), và giá đóng cửa (`Close`).  
  - Khối lượng giao dịch (`Volume`) được minh họa bên dưới.  
- **Công cụ sử dụng**:  
  - Thư viện `mplfinance` với kiểu hiển thị `candle`.  

### 3️⃣ **Phát Triển Mô Hình Dự Đoán (Định Hướng)**  
- Dựa trên dữ liệu:  
  - **Feature**: `Volume`, `Close`.  
  - **Target**: Giá đóng cửa ngày tiếp theo.  
- Sử dụng các mô hình như:  
  - Hồi quy tuyến tính (`Linear Regression`).  
  - LSTM (Long Short-Term Memory) cho chuỗi thời gian.  

---

## 📊 **Kết Quả Trực Quan Hóa**  

### Biểu đồ nến minh họa (Ví dụ):  
- **Cổ phiếu FPT**:  
![FPT](https://github.com/user-attachments/assets/216cc4b8-258f-4ccf-b9ad-05ac6e3b9550)

- **Cổ phiếu MSN**:  
![MSN](https://github.com/user-attachments/assets/7b659545-23fa-4c4e-a436-5069e0ac4171)

- **Cổ phiếu VIC**:  
![VIC](https://github.com/user-attachments/assets/7c22c7eb-40e3-41cc-b0ab-2815a6f08ec5)

- **Cổ phiếu PNJ**:  
![PNJ](https://github.com/user-attachments/assets/9397efa4-f630-414d-bf5a-023830c42506)

---

## 🔧 **Hướng Dẫn Chạy Dự Án**  

### 1️⃣ **Cài Đặt Môi Trường**  
- Cài đặt các thư viện cần thiết:  
  ```bash
  pip install pandas matplotlib mplfinance scikit-learn
2️⃣ Tải Dữ Liệu
Chuẩn bị dữ liệu chứng khoán của 4 mã cổ phiếu (file CSV).
Đặt file vào thư mục dự án với tên stock_data.csv.
3️⃣ Chạy Mã Python
Tạo file main.py với nội dung:

```python
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

# Read the CSV file 
df = pd.read_csv('VIC (1).csv') # thay tên file để vẽ biểu đồ 

# Convert Date/Time column to datetime
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Set Date/Time as index
df.set_index('Date/Time', inplace=True)

# Create a new DataFrame with OHLC data
ohlc = df[['Open', 'High', 'Low', 'Close']].resample('D').agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last'
}).dropna()  # Drop rows with NaN values

# Reset index to get Date as a column
ohlc.reset_index(inplace=True)

# Convert Date to number for plotting
ohlc['Date_num'] = mdates.date2num(ohlc['Date/Time'])

# Create the main figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Plot candlestick chart
candlestick_ohlc(ax1, ohlc[['Date_num', 'Open', 'High', 'Low', 'Close']].values, width=0.6, colorup='g', colordown='r')

# Set x-axis format
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mdates.AutoDateLocator())

# Rotate x-axis labels
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Set labels and title for candlestick chart
ax1.set_ylabel('Price')
ax1.set_title('VIC Stock Price')

# Plot volume bar chart
volume = df['Volume'].resample('D').sum()
ax2.bar(volume.index, volume.values, color='b', alpha=0.5)

# Set y-axis limits for volume chart
max_volume = volume.max()
ax2.set_ylim(0, max_volume * 1.1)  # Increase upper limit by 10%

# Format y-axis labels to millions
def millions(x, pos):
    return f'{x/1e6:.1f}M'

ax2.yaxis.set_major_formatter(FuncFormatter(millions))

# Set labels for volume chart
ax2.set_ylabel('Volume (Millions)')
ax2.set_xlabel('Date')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
```
*** Lưu ý: Chỉ cần thay tên file bằng các tên file csv muốn trực quan hóa, có thể là file có sẵn hoặc tải data từ trên mạng mà thỏa mãn các trường (Ticker, Date/Time, Open, High, Low, Close, Volume) 
Chạy lệnh:
```bash
python convert_data_stock_chart.py
```
4️⃣ Kết Quả
Biểu đồ nến sẽ hiển thị với khối lượng giao dịch bên dưới.
🔍 Định Hướng Tương Lai
Phát triển mô hình Machine Learning:
Xây dựng mô hình dự đoán giá ngắn hạn.
Kết hợp thêm các yếu tố kỹ thuật như RSI, MACD để cải thiện hiệu quả dự đoán.
Tích hợp dashboard: Hiển thị dữ liệu và dự đoán trực tiếp qua giao diện web.
✨ Thanks for reading! ✨
