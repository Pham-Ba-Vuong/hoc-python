# Các công cụ hỗ trợ cho việc xử lý dữ liệu, hiển thị, quản lý phần cứng và tương tác với môi trường Notebook:
## 1.Quản lý File và Tương tác Drive (google.colab.files)
- Tải file từ máy lên Colab:
``` Python
    from google.colab import files
    uploaded = files.upload()
```
- Tải file từ Colab về máy:
``` Python
    files.download('filename.csv')
```
## 2.Tương tác UI / Form Tùy chỉnh (google.colab.widgets & Form)
- Tạo Form nhập dữ liệu: Cho phép tạo giao diện nhập liệu nhanh mà không cần sửa code.
``` Python
    learning_rate = 0.001 
    model_name = "ResNet"
```
-  Tạo các thành phần UI (Grid, Tab, Button):   
``` Python
    from google.colab import output
```
## 3.Hiển thị Dataframe & Dữ liệu nâng cao (google.colab.data_table)
- Bảng dữ liệu tương tác: Biến bảng pandas.DataFrame thành dạng bảng thông minh.
``` Python
   from google.colab import data_table
   data_table.enable_dataframe_formatter()
```  
## 4.Tương tác Phần cứng & Media (google.colab.patches)
-  cv2_imshow (Dành cho OpenCV): Hàm cv2.imshow() chuẩn của OpenCV bị lỗi crash trên Colab. Cần dùng hàm này để thay thế.
``` Python
     from google.colab.patches import cv2_imshow
     cv2_imshow(img)
```   
-  Truy cập Camera / Microphone: Sử dụng JavaScript snippet kết hợp Python để chụp ảnh hoặc ghi âm trực tiếp từ webcam/micro của máy tính.
## 5. Quản lý Runtime & Hệ thống
- Kiểm tra / Quản lý tài nguyên GPU/TPU:
``` Python
    import torch
    print(torch.cuda.is_available()) 
```
- Ngắt kết nối Runtime bằng code:
``` Python
    from google.colab import runtime
    runtime.unassign()
```
## 6. Lệnh Shell Magic hữu ích (! và %)
-  Tải dữ liệu trực tiếp từ Internet qua URL:
```Bash 
   !wget https://example.com/dataset.zip
   !unzip dataset.zip -d /content/dataset   
```
-  Kiểm tra thông số phần cứng GPU được cấp:
```Bash
   !nvidia-smi      
```
-  Chuyển thư mục làm việc (dùng %cd thay vì !cd):
```Bash
    %cd /content/drive/MyDrive/MyProject
    %pwd 
```
## 7.làm việc trực tiếp với Git mà không cần dùng lệnh Terminal:
- Mở file từ GitHub: thay miền [github.com] thành [githubtocolab.com] trên URL của bất kỳ file [.ipynb] nào để mở ngay lập tức trên Colab.
- Lưu file thẳng lên GitHub: Vào File -> Save a copy in GitHub để commit và push file notebook trực tiếp vào repository.
- chèn đoạn "Open in Colab" vào file [README.md] của repo GitHub để mở thẳng code trên Colab
## 8.Đăng nhập / Xác thực dịch vụ Google (google.colab.auth)
- Để truy cập trực tiếp vào các dịch vụ đám mây
```Python
   from google.colab import auth
   auth.authenticate_user() 
   !gcloud config set project MY_PROJECT_ID
```
## 9.UI Hints
- Code Snippets Panel: Ở thanh bên trái (biểu tượng <>), Colab tích hợp sẵn hàng trăm mẫu code chuẩn từ xử lý ảnh, webcam, vẽ đồ thị đến kết nối cơ sở dữ liệu.
- Biểu tượng {x} ở thanh bên trái cho theo dõi danh sách tất cả các biến đang tồn tại trong bộ nhớ, loại dữ liệu, kích thước và dung lượng RAM mà biến đó chiếm dụng.
- Thiết lập thông báo hoàn thành (Terminal Notifications): Vào Tools -> Settings -> Site -> Bật Desktop notifications
   
