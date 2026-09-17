# A.Google Colab / Jupyter Notebook (Mount trực tiếp)
## I.cách thực hiện 
### 1.mã code Python:
- Cách thực hiện :
``` PYTHON:
 from google.colab import drive
drive.mount('/content/drive')
```
- - Khi chạy đoạn code này, Google sẽ yêu cầu  xác thực quyền truy cập. Sau khi đồng ý, toàn bộ tài khoản Google Drive của sẽ gắn vào cây thư mục /content/drive/MyDrive/.
## II.Đọc và ghi dữ liệu bằng Python 
### 1.Đọc file CSV bằng Pandas:
-  cách đọc :
```Python
 import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data/dataset.csv')
```
### 2.Ghi/lưu file kết quả 
- Cách lưu:
```Python
 df.to_csv('/content/drive/MyDrive/data/output.csv', index=False)
 ```
### 3.Thao tác file hệ thống: Dùng thư viện os hoặc shutil để tạo thư mục, di chuyển file hoàn toàn như trên máy cá nhân.
# B.Mount hệ thống tệp bằng Rclone (Cho Linux / Windows / Server)
## I.Quy trình thiết lập
### 1.Cài đặt Rclone 
-Chạy lệnh cài đặt trên Linux/macOS:
```Bash
 curl https://rclone.org/install.sh | sudo bash
 ```
### 2.Cấu hình kết nối 
- Gõ rclone config, chọn n (New remote), đặt tên (ví dụ: gdrive), chọn provider là Google Drive và làm theo hướng dẫn cấp quyền OAuth.
### 3.Thực hiện Mount vào ổ đĩa ảo
- Tạo một thư mục trống và mount Google Drive vào đó:
```Bash
 mkdir -p ~/my_gdrive
rclone mount gdrive: ~/my_gdrive --daemon
```
### 4.Đọc và ghi dữ liệu
- Liệt kê file: ls ~/my_gdrive
- Copy file từ máy lên Drive: cp data.json ~/my_gdrive/data/
- Ứng dụng chạy ngầm: Mọi script Python/C++ truy cập đường dẫn ~/my_gdrive đều có thể đọc/ghi trực tiếp lên cloud.
# C.Lập trình qua Google Drive API (Python SDK)
## I.Các bước chuẩn bị:
- Tạo một dự án trên Google Cloud Console.
- Bật dịch vụ Google Drive API.
- Tạo Service Account (cho hệ thống tự chạy) hoặc OAuth 2.0 Client ID (cho người dùng cuối).
- Tải file chứng thực .json về máy.
## II.Code Python cơ bản (PyDrive2):
### 1.Cài đặt thư viện:
- cách cài: 
```Bash
 pip install PyDrive2
 ```
### 2.Đọc/Tải file lên Google Drive:
- cách đọc/tải:
```Python
 from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() #Mở trình duyệt đăng nhập
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'report.txt'})
file1.SetContentString('Nội dung dữ liệu ghi vào Drive')
file1.Upload()

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for f in file_list:
    print(f'Title: {f["title"]}, ID: {f["id"]}')
```    
# D.Dùng Google Drive làm Kho dữ liệu (Data Warehouse / Analytics)
## I. các kho dữ liệu 
- BigQuery (External Table)
- Looker Studio
- DuckDB / Polars (Python)
## II.Ví dụ quy trình BigQuery External Table:
- Bạn lưu 1 file sales_2026.csv trên Google Drive.
- Trên Google BigQuery, bạn chọn Create Table -> Source chọn Drive.
- Dán đường dẫn URI của file Google Drive.
- Chọn định dạng CSV và đặt tên bảng là sales_data.
- Giờ đây bạn có thể gõ SQL trực tiếp:
```SQL
SELECT product_name, SUM(amount) 
FROM `my_project.my_dataset.sales_data` 
GROUP BY product_name;
````