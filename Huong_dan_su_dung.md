# Hướng dẫn sử dụng Tool Upload Video từ Drive lên YouTube

Do bạn đã có API Client ID (`355324102160-p5931t8lkmg1f3cu9cdm5ujri7u5io3e.apps.googleusercontent.com`), bạn chỉ cần tải file `client_secrets.json` tương ứng từ Google Cloud Console để nạp vào Colab.

## Bước 1: Lấy file `client_secrets.json`
1. Truy cập vào [Google Cloud Console - Credentials](https://console.cloud.google.com/apis/credentials).
2. Đăng nhập bằng tài khoản Google của bạn.
3. Trong phần **OAuth 2.0 Client IDs**, tìm Client ID của bạn (Bắt đầu bằng `355324102160...`).
4. Ở góc phải của dòng đó, bấm vào biểu tượng **Tải xuống (Download)** hình mũi tên trỏ xuống.
5. Đổi tên file vừa tải về thành `client_secrets.json` (để nguyên đuôi `.json`).

## Bước 2: Đưa mã nguồn lên GitHub (Để lấy link chạy nhanh)
1. Đăng nhập vào tài khoản GitHub của bạn và tạo một Repository mới (ví dụ: `colab-youtube-uploader`).
2. Upload file `youtube_uploader.ipynb` từ máy tính lên Repository vừa tạo.
3. Mở file đó trên GitHub, bạn sẽ có đường dẫn dạng: `https://github.com/TenCuaBan/colab-youtube-uploader/blob/main/youtube_uploader.ipynb`
4. Để mở thẳng trong Google Colab, bạn chỉ cần thay đổi tên miền `github.com` thành `colab.research.google.com/github`.
   - **Link Colab sẽ là:** `https://colab.research.google.com/github/TenCuaBan/colab-youtube-uploader/blob/main/youtube_uploader.ipynb`
   - _Lưu link này lại vào Bookmark trình duyệt để lần sau bấm một phát là mở luôn tool._

## Bước 3: Cách chạy Tool trên Colab
1. Mở link Colab bạn vừa tạo.
2. Bấm nút **Connect (Kết nối)** ở góc phải trên cùng.
3. Chạy lần lượt các ô code (bấm nút hình ▶️ ở góc trái mỗi ô):
   - **Cài thư viện**: Đợi báo thành công.
   - **Upload API**: Bấm "Choose Files" và chọn file `client_secrets.json` bạn đã tải ở Bước 1.
   - **Cấu hình Video**: Dán trực tiếp **Đường link chia sẻ Google Drive** của video vào ô. Nếu bạn để trống tiêu đề, nó sẽ tự lấy tên file. Trạng thái mặc định là `private`.
   - **Upload**: Chạy ô cuối cùng. Nó sẽ hiện popup của Colab yêu cầu bạn cấp quyền truy cập Drive (để tải video) và sau đó cấp quyền tải lên YouTube. Sau khi xác thực xong, video sẽ được chuyển lên YouTube với tốc độ siêu nhanh.


**Lưu ý:**
- Vì video được chuyển thẳng từ máy chủ của Google Drive sang Google (YouTube), bạn không cần cắm máy tính. Quá trình tải lên vài GB chỉ mất vài giây đến vài chục giây.
- File `client_secrets.json` chỉ cần tải lên Colab 1 lần cho mỗi phiên làm việc.
