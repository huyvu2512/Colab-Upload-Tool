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
| 🌍 **Hỗ trợ mọi link video** | Tải video từ Google Drive, YouTube, OK.ru, VK, Facebook, TikTok, **Bilibili** và link trực tiếp `.mp4`. Tự động nhận diện nguồn. |
| 🚀 **Tốc độ siêu tốc** | Kéo file và up lên YouTube bằng mạng siêu khủng của máy chủ Google (Lên tới 50-100MB/s) |
| 💾 **Sao lưu Google Drive** | Tự động lưu `client_secrets.json` và token vào Drive. Mở lại Colab sẽ tự động khôi phục, không cần cấu hình lại! |
| 🎨 **Giao diện thân thiện** | Tất cả mã nguồn ẩn mặc định, giao diện Form gọn gàng, Việt Hóa 100%. |
| 🔄 **Tự động thử lại** | Khi tải video từ nguồn ngoài bị lỗi mạng, script tự động thử lại tới 3 lần thay vì dừng ngay. |
| 🛡️ **Bảo mật & Ổn định** | Tự động xử lý lỗi `MismatchingStateError`, bắt lỗi thiếu quyền API và xoá token hỏng. |
| 📊 **Thanh tiến trình** | Theo dõi % hoàn thành, tốc độ chuẩn MB/s và thời gian đếm ngược (ETA) siêu trực quan. |
| 🤖 **Tự động hóa** | Tự đặt tên tiêu đề theo tên file gốc, tự dọn rác ổ đĩa Colab sau khi up thành công. |

---

## 🖥️ Bắt đầu sử dụng nhanh

> **Chạy ngay trên trình duyệt:** [👉 BẤM VÀO ĐÂY ĐỂ MỞ TRÊN GOOGLE COLAB](https://colab.research.google.com/github/huyvu2512/ColabTube-Uploader/blob/main/ColabTube_Uploader.ipynb)

### Hướng dẫn các bước:
1. **Lấy API Key:** Truy cập [Google Cloud Console](https://console.cloud.google.com/), tạo OAuth 2.0 Client ID và tải về `client_secrets.json`. **Bắt buộc** bật **YouTube Data API v3**.
2. **Mở Colab:** Bấm vào link trên để mở sổ tay Colab.
3. **Cài đặt thư viện:** Chạy ô đầu tiên.
4. **Kết nối Drive (MỚI!):** Chạy ô **💾 Kết nối Google Drive**. Lần đầu sẽ yêu cầu cấp quyền. Từ lần sau, nó sẽ tự khôi phục cấu hình cũ từ Drive!
5. **Tải cấu hình:** Upload `client_secrets.json` (chỉ cần lần đầu, lần sau Drive tự khôi phục).
6. **Cấu hình & Tải lên:**
   - Dán BẤT CỨ đường link video nào vào ô `VIDEO_LINK` (hỗ trợ cả **Bilibili**).
   - Bấm **🚀 BẤT ĐẦU TẢI VÀ UPLOAD YOUTUBE**. Xong!

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
