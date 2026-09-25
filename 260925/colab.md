# I.Google Colab Tutorial | Markdown | Rich Text Documentation | Image Upload
## 1.Rich Text
- Tiêu đề (Headings): 
```markdown
   # H1, ## H2, ### H3
```
-   In đậm / Nghiêng:
```markdown
   **Đậm**, *Ngiêng*
```   
-   Gạch ngang:
```markdown
   ~~Gạch ngang~~
```
-   Blockquote:
```markdown
   > Nội dung trích dẫn
```   
## 2.LaTeX
- Sử dụng kí hiệu $ cho công thức inline hoặc $$ cho công thức nằm riêng biệt trên một dòng:
```markdown 
   Công thức tính sai số bình phương trung bình:
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
```
# II.Google Colab Tutorial | How to save, (Google Drive - Github), Download & share Colab File
## 1.Save Options
- toàn bộ các thao tác lưu trữ nằm tại menu File ở góc trên bên trái
## 2.Download
- 1.Mở menu File:Di chuột đến menu File ở thanh công cụ phía trên
- 2.Chọn định dạng tải về có 2 loại:
- - Download .ipynb
- - Download .py
## 3.Share
 - Nhấn vào nút Share (Chia sẻ) ở góc trên bên phải màn hình.
#  III.Google Colab Tutorial | System Level Command from Colab
## 1.Dấu ! và Lệnh %
```Python
# 1. Chạy lệnh shell đơn
!ls -la

# 2. Thay đổi thư mục làm việc 
%cd /content/sample_data
!pwd
```
## 2.File Management
```Python
# Tạo thư mục mới
!mkdir my_project

# Tải tệp từ internet về máy chủ Colab
!wget https://.... 

# Giải nén tệp zip 
!unzip -q dataset.zip -d /content/my_project/

# Xem 10 dòng đầu của tệp text/CSV
!head -n 10 countries-aggregated.csv
```
## 3.Cài đặt Gói & Công cụ Hệ thống
```Python
# 1. Cập nhật trình quản lý gói
!apt-get update -qq

# 2. Cài đặt công cụ hệ thống 
!apt-get install -y tree ffmpeg

# 3. Cài đặt thư viện Python
!pip install --upgrade pandas
```
# IV.Google Colab Tutorial | Colab magic command : Line magic, Cell magic
## 1.Line Magic Commands (%)
- Line magic chỉ áp dụng cho dòng chứa nó.
```Python
# 1. Quản lý thư mục làm việc 
%cd /content/sample_data

# 2. Xem thư mục hiện tại
%pwd

# 3. Liệt kê các biến đang lưu trong bộ nhớ Python
%who

# 4. Liệt kê  thông tin và kiểu dữ liệu của các biến
%whos

# 5. Đo thời gian thực thi của 1 dòng lệnh
%time x = [i**2 for i in range(1000000)]

# 6. Đo thời gian trung bình 
%timeit sum(range(1000))
```
## 2. Cell Magic Commands (%%)
- Cell magic áp dụng cho toàn bộ nội dung bên trong ô Code đó.
- - Ghi nội dung vào tệp (%%writefile)
```Python
%%writefile config.py
# Tệp cấu hình tự động tạo từ Colab
BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 10
```
- -  Chạy kịch bản Shell/Bash (%%bash)
``` Bash
%%bash
echo "Khởi tạo thư mục dự án..."
mkdir -p src/data src/models
touch src/config.py
ls -R src/
```
## 3. Quản lý và Tra cứu Magic Commands
- Liệt kê tất cả danh sách lệnh Magic có sẵn:
```Python
%lsmagic
```
- Xem hướng dẫn chi tiết của một lệnh bất kỳ:
Thêm dấu ? phía sau tên lệnh.
```Python
%timeit?
```
# V.Google Colab Tutorial | How to Execute external Python (.py) File
- 1.Thực thi tệp .py bằng lệnh Shell
```Python
# Chạy tệp script Python
!python my_script.py

# Truyền thêm tham số (arguments) vào file script nếu cần
!python train.py --epochs 50 --batch_size 32\
```
- 2.Thực thi và tải nội dung tệp bằng Magic Command
```Python
# Chạy file script
%run my_script.py

# Sau khi chạy %run, bạn có thể gọi trực tiếp các hàm/biến đã khai báo trong my_script.py
result = my_function_from_script()
print(result)
```
## 3.Xem hoặc Chỉnh sửa trực tiếp tệp .py trong Colab
- Tải nội dung tệp .py vào ô Code
```Python
%load my_script.py
```
- Xem nội dung tệp mà không chạy
```Python
!cat my_script.py
```
# VI.Google Colab Tutorial | How to Install Third party package on Google Colab
## 1.Cài đặt bằng pip
```Python
# Cài đặt một thư viện cơ bản
!pip install transformers

# Cài đặt phiên bản cụ thể của thư viện
!pip install pandas==2.1.0

# Cập nhật thư viện lên phiên bản mới nhất
!pip install --upgrade scikit-learn

# Cài đặt nhiều thư viện cùng lúc
!pip install langchain openai chromadb
```

