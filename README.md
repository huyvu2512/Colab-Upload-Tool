<div align="center">

# 🚀 Colab Upload Tool

**Chuyển trực tiếp video dung lượng lớn từ Google Drive sang YouTube siêu tốc bằng Google Colab.**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![Google Drive API](https://img.shields.io/badge/Google%20Drive%20API-4285F4?logo=googledrive&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube%20Data%20API%20v3-FF0000?logo=youtube&logoColor=white)

🌐 **[Mở trong Colab](https://colab.research.google.com/github/huyvu2512/Colab-Upload-Tool/blob/main/youtube_uploader.ipynb)** · 📦 **[GitHub](https://github.com/huyvu2512/Colab-Upload-Tool)** · 👤 **[Liên hệ](https://beacons.ai/huyvu2512)**

---

### 📊 Thống Kê Dự Án

[![Stars](https://img.shields.io/github/stars/huyvu2512/Colab-Upload-Tool?style=flat-square&label=⭐%20Stars&color=FFCC00)](https://github.com/huyvu2512/Colab-Upload-Tool/stargazers)
[![Forks](https://img.shields.io/github/forks/huyvu2512/Colab-Upload-Tool?style=flat-square&label=🍴%20Forks&color=6e7681)](https://github.com/huyvu2512/Colab-Upload-Tool/forks)
[![Issues](https://img.shields.io/github/issues/huyvu2512/Colab-Upload-Tool?style=flat-square&label=🐛%20Issues&color=f85149)](https://github.com/huyvu2512/Colab-Upload-Tool/issues)
[![Last Commit](https://img.shields.io/github/last-commit/huyvu2512/Colab-Upload-Tool?style=flat-square&label=🕐%20Cập%20nhật&color=3fb950)](https://github.com/huyvu2512/Colab-Upload-Tool/commits/main)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=huyvu2512.Colab-Upload-Tool&left_text=👁%20Lượt%20xem&left_color=6e7681&right_color=FF0000)

</div>

---

## ⚠️ Tuyên bố miễn trách nhiệm

> **Dự án này được xây dựng hoàn toàn vì mục đích tiện ích cá nhân và phi lợi nhuận.**
>
> - Toàn bộ dữ liệu được truyền tải thông qua **Google Drive API** và **YouTube Data API v3** — API chính thức do Google cung cấp.
> - Dự án **không** lưu trữ, phân phối lại hay tái bản bất kỳ nội dung video nào.
> - Mọi nhãn hiệu, thương hiệu, và nội dung liên quan đến YouTube / Google đều thuộc sở hữu của **Google LLC**.

---

## ✨ Tính năng nổi bật

| Tính năng | Mô tả |
|---|---|
| 🚀 **Tốc độ siêu tốc** | Chuyển file giữa máy chủ Google (Drive -> YouTube) với tốc độ lên đến 20-50MB/s |
| 🛡️ **Vượt rào virus scan** | Tự động bỏ qua cảnh báo quét virus của Google Drive cho các file siêu lớn (>10GB) |
| 📊 **Thanh tiến trình** | Theo dõi trực tiếp % hoàn thành, tốc độ mạng và thời gian đếm ngược (ETA) |
| 🔄 **Lưu phiên đăng nhập** | Tự động lưu Token xác thực, không cần đăng nhập lại cho các lần up tiếp theo |
| 🧹 **Dọn dẹp tự động** | Tự động xoá file trên máy chủ Colab sau khi upload thành công để tránh đầy ổ cứng |
| 🔗 **Hỗ trợ mọi link Drive** | Nhận diện thông minh cả link chia sẻ dạng ID và dạng URL chuẩn |

---

## 🖥️ Bắt đầu sử dụng nhanh

> **Chạy ngay trên trình duyệt:** [👉 BẤM VÀO ĐÂY ĐỂ MỞ TRÊN GOOGLE COLAB](https://colab.research.google.com/github/huyvu2512/Colab-Upload-Tool/blob/main/youtube_uploader.ipynb)

### Hướng dẫn các bước:
1. **Lấy API Key:** Truy cập [Google Cloud Console](https://console.cloud.google.com/), tạo một OAuth 2.0 Client ID (chọn loại ứng dụng "Desktop app" hoặc "Web app") và tải về file `client_secrets.json`. Cần bật **YouTube Data API v3** cho dự án này.
2. **Mở Colab:** Bấm vào link trên để mở sổ tay Colab.
3. **Chạy các ô:** Lần lượt chạy các ô code từ trên xuống dưới bằng nút Play (▶️).
4. **Tải cấu hình:** Khi được yêu cầu, hãy upload file `client_secrets.json` của bạn lên Colab.
5. **Dán link Drive & Xác thực:** Nhập link video Google Drive. Lần đầu tiên, tool sẽ yêu cầu bạn cấp quyền truy cập Drive và YouTube. Click vào link, cấp quyền, copy dòng báo lỗi `http://localhost...` dán vào ô nhập liệu để hoàn tất.

---

## 🏗️ Kiến trúc dự án

```
Colab Upload Tool/
├── youtube_uploader.ipynb    # Sổ tay Jupyter chính chạy trên Google Colab
├── README.md                 # Tài liệu hướng dẫn sử dụng (File bạn đang xem)
├── CONTRIBUTING.md           # Hướng dẫn đóng góp mã nguồn
├── SECURITY.md               # Chính sách bảo mật
└── LICENSE                   # Giấy phép phần mềm (MIT)
```

---

## 📬 Liên hệ & đóng góp

- 👤 **Tác giả:** [beacons.ai/huyvu2512](https://beacons.ai/huyvu2512)
- 🐛 **Bug / Feature:** [Mở Issue](https://github.com/huyvu2512/Colab-Upload-Tool/issues)
- 🤝 **Đóng góp:** Xem [CONTRIBUTING.md](CONTRIBUTING.md)
- 🔒 **Bảo mật:** Xem [SECURITY.md](SECURITY.md)

---

## 📄 Giấy phép

Dự án được phân phối theo giấy phép **MIT**. Xem chi tiết tại [LICENSE](LICENSE).
