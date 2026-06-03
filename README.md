<div align="center">

# 🚀 ColabTube Uploader

**Công cụ đa năng tải video từ mọi nguồn (Drive, YouTube, OK.ru, VK...) và Upload trực tiếp lên YouTube siêu tốc bằng Google Colab.**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?logo=youtube&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube%20Data%20API%20v3-FF0000?logo=youtube&logoColor=white)

🌐 **[Mở trong Colab](https://colab.research.google.com/github/huyvu2512/ColabTube-Uploader/blob/main/ColabTube_Uploader.ipynb)** · 📦 **[GitHub](https://github.com/huyvu2512/ColabTube-Uploader)** · 👤 **[Liên hệ](https://beacons.ai/huyvu2512)**

---

### 📊 Thống Kê Dự Án

[![Stars](https://img.shields.io/github/stars/huyvu2512/ColabTube-Uploader?style=flat-square&label=⭐%20Stars&color=FFCC00)](https://github.com/huyvu2512/ColabTube-Uploader/stargazers)
[![Forks](https://img.shields.io/github/forks/huyvu2512/ColabTube-Uploader?style=flat-square&label=🍴%20Forks&color=6e7681)](https://github.com/huyvu2512/ColabTube-Uploader/forks)
[![Issues](https://img.shields.io/github/issues/huyvu2512/ColabTube-Uploader?style=flat-square&label=🐛%20Issues&color=f85149)](https://github.com/huyvu2512/ColabTube-Uploader/issues)
[![Last Commit](https://img.shields.io/github/last-commit/huyvu2512/ColabTube-Uploader?style=flat-square&label=🕐%20Cập%20nhật&color=3fb950)](https://github.com/huyvu2512/ColabTube-Uploader/commits/main)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=huyvu2512.ColabTube-Uploader&left_text=👁%20Lượt%20xem&left_color=6e7681&right_color=FF0000)

</div>

---

## ⚠️ Tuyên bố miễn trách nhiệm

> **Dự án này được xây dựng hoàn toàn vì mục đích tiện ích cá nhân và phi lợi nhuận.**
>
> - Toàn bộ dữ liệu được truyền tải thông qua **Google Drive API**, **yt-dlp** và **YouTube Data API v3**.
> - Dự án **không** lưu trữ, phân phối lại hay tái bản bất kỳ nội dung video nào.
> - Người dùng tự chịu trách nhiệm về bản quyền nội dung video tải xuống và tải lên.

---

## ✨ Tính năng nổi bật

| Tính năng | Mô tả |
|---|---|
| 🌍 **Hỗ trợ mọi link video** | Tải video từ Google Drive, YouTube, OK.ru, VK, Facebook, TikTok và các link trực tiếp `.mp4`. Tự động nhận diện nguồn tải. |
| 🚀 **Tốc độ siêu tốc** | Kéo file và up lên YouTube bằng mạng siêu khủng của máy chủ Google (Lên tới 50-100MB/s) |
| 🎨 **Giao diện thân thiện** | Code phức tạp được giấu gọn gàng đằng sau giao diện Form, toàn bộ quá trình được Việt Hóa 100%. |
| 🛡️ **Bảo mật & Ổn định** | Tự động xử lý lỗi `MismatchingStateError` của Google, tự động bắt lỗi thiếu quyền API và xoá token hỏng. |
| 📊 **Thanh tiến trình** | Theo dõi trực tiếp % hoàn thành, tốc độ mạng chuẩn MB/s và thời gian đếm ngược (ETA) siêu trực quan. |
| 🤖 **Tự động hóa** | Tự động đặt tên tiêu đề theo tên file gốc, tự động dọn rác ổ đĩa Colab sau khi up thành công. |

---

## 🖥️ Bắt đầu sử dụng nhanh

> **Chạy ngay trên trình duyệt:** [👉 BẤM VÀO ĐÂY ĐỂ MỞ TRÊN GOOGLE COLAB](https://colab.research.google.com/github/huyvu2512/ColabTube-Uploader/blob/main/ColabTube_Uploader.ipynb)

### Hướng dẫn các bước:
1. **Lấy API Key:** Truy cập [Google Cloud Console](https://console.cloud.google.com/), tạo một OAuth 2.0 Client ID và tải về file `client_secrets.json`. **Bắt buộc** bật **YouTube Data API v3** cho dự án này.
2. **Mở Colab:** Bấm vào link trên để mở sổ tay Colab.
3. **Cài đặt thư viện:** Bấm chạy ô cài đặt đầu tiên.
4. **Tải cấu hình:** Chạy ô số 2 và upload file `client_secrets.json` của bạn lên Colab.
5. **Cấu hình & Tải lên:** 
   - Dán BẤT CỨ đường link video nào vào ô `VIDEO_LINK`.
   - Bấm ô cuối cùng **🚀 BẤT ĐẦU TẢI VÀ UPLOAD YOUTUBE**. Script sẽ tự động xác thực YouTube, tải video về Colab và đẩy thẳng lên kênh YouTube của bạn!

---

## 🏗️ Kiến trúc dự án

```
ColabTube Uploader/
├── ColabTube_Uploader.ipynb  # Sổ tay Jupyter chính chạy trên Google Colab
├── README.md                 # Tài liệu hướng dẫn sử dụng (File bạn đang xem)
├── CONTRIBUTING.md           # Hướng dẫn đóng góp mã nguồn
├── SECURITY.md               # Chính sách bảo mật
└── LICENSE                   # Giấy phép phần mềm (MIT)
```

---

## 📬 Liên hệ & đóng góp

- 👤 **Tác giả:** [beacons.ai/huyvu2512](https://beacons.ai/huyvu2512)
- 🐛 **Bug / Feature:** [Mở Issue](https://github.com/huyvu2512/ColabTube-Uploader/issues)
- 🤝 **Đóng góp:** Xem [CONTRIBUTING.md](CONTRIBUTING.md)
- 🔒 **Bảo mật:** Xem [SECURITY.md](SECURITY.md)

---

## 📄 Giấy phép

Dự án được phân phối theo giấy phép **MIT**. Xem chi tiết tại [LICENSE](LICENSE).
