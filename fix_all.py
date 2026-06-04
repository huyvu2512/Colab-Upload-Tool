import json

with open('ColabTube_Uploader.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# ============================================================
# T2: Force ALL cells to collapsed (hidden code) by default
# ============================================================
# Set cellView: "form" in metadata for all code cells that have #@title
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        cell['metadata']['cellView'] = 'form'

# ============================================================
# T3: Add a new cell AFTER install_deps to mount Drive and restore backup
# Also update upload_secrets to backup to Drive
# Also update token save to backup to Drive
# ============================================================

# --- New Cell: Mount Drive & Restore Backup ---
mount_drive_cell = {
    "cell_type": "code",
    "metadata": {
        "id": "mount_drive_backup",
        "cellView": "form"
    },
    "source": [
        "#@title 💾 Kết nối Google Drive (Sao lưu cấu hình tự động)\n",
        "from google.colab import drive\n",
        "import os\n",
        "import shutil\n",
        "\n",
        "drive.mount('/content/drive')\n",
        "\n",
        "BACKUP_DIR = '/content/drive/MyDrive/ColabTube_Backup'\n",
        "os.makedirs(BACKUP_DIR, exist_ok=True)\n",
        "\n",
        "# Khôi phục file cấu hình từ Drive (nếu có)\n",
        "restored = []\n",
        "for fname in ['client_secrets.json', 'youtube_token.json']:\n",
        "    backup_path = os.path.join(BACKUP_DIR, fname)\n",
        "    if os.path.exists(backup_path) and not os.path.exists(fname):\n",
        "        shutil.copy2(backup_path, fname)\n",
        "        restored.append(fname)\n",
        "\n",
        "if restored:\n",
        "    print(f\"✅ Đã khôi phục từ Drive: {', '.join(restored)}\")\n",
        "    print(\"👉 Bạn có thể BỎ QUA bước tải client_secrets.json bên dưới!\")\n",
        "else:\n",
        "    print(\"✅ Đã kết nối Google Drive thành công.\")\n",
        "    print(\"📁 Thư mục sao lưu: Drive/ColabTube_Backup/\")\n"
    ],
    "execution_count": None,
    "outputs": []
}

# --- Update upload_secrets cell to also backup to Drive ---
upload_secrets_cell = {
    "cell_type": "code",
    "metadata": {
        "id": "upload_secrets",
        "cellView": "form"
    },
    "source": [
        "#@title 🔑 Tải lên file chứng chỉ client_secrets.json (Chạy 1 lần)\n",
        "from google.colab import files\n",
        "import os, shutil\n",
        "\n",
        "BACKUP_DIR = '/content/drive/MyDrive/ColabTube_Backup'\n",
        "\n",
        "if os.path.exists('client_secrets.json'):\n",
        "    print(\"✅ File client_secrets.json đã tồn tại. Bỏ qua bước này.\")\n",
        "else:\n",
        "    print(\"Vui lòng tải lên file client_secrets.json của bạn (Lấy từ Google Cloud Console)\")\n",
        "    uploaded = files.upload()\n",
        "    for fn in uploaded.keys():\n",
        "        if fn != 'client_secrets.json':\n",
        "            os.rename(fn, 'client_secrets.json')\n",
        "    print(\"✅ Đã tải lên thành công file cấu hình API.\")\n",
        "\n",
        "# Sao lưu vào Drive\n",
        "if os.path.exists(BACKUP_DIR) and os.path.exists('client_secrets.json'):\n",
        "    shutil.copy2('client_secrets.json', os.path.join(BACKUP_DIR, 'client_secrets.json'))\n",
        "    print(\"💾 Đã sao lưu client_secrets.json vào Drive/ColabTube_Backup/\")\n"
    ],
    "execution_count": None,
    "outputs": []
}

# Insert mount_drive cell after install_deps (index 1), before upload_secrets (index 2)
nb['cells'].insert(2, mount_drive_cell)
# Replace the old upload_secrets cell (now at index 3)
nb['cells'][3] = upload_secrets_cell

# ============================================================
# T1 + T4: Update yt-dlp section - add Bilibili support + retry logic
# ============================================================
script_cell = nb['cells'][5]  # Was index 4, now 5 after insert
src = script_cell['source']

# Update the header markdown to mention Bilibili
header_cell = nb['cells'][0]
header_cell['source'] = [
    "# 🚀 ColabTube Uploader\n",
    "Công cụ đa năng tải video từ **mọi nguồn** và Upload trực tiếp lên YouTube siêu tốc.\n",
    "\n",
    "**Nguồn hỗ trợ:** Google Drive, YouTube, OK.ru, VK, Facebook, TikTok, **Bilibili**, và link trực tiếp (.mp4).\n",
    "\n",
    "**Hướng dẫn:** Chạy từng ô từ trên xuống dưới bằng nút ▶️ bên trái.\n"
]

# Update config form to mention Bilibili
config_cell = nb['cells'][4]  # Was index 3, now 4
config_cell['source'] = [
    "#@title ⚙️ Cấu hình Video\n",
    "\n",
    "#@markdown Dán đường link Video vào đây. Hỗ trợ: Google Drive, YouTube, OK.ru, VK, Facebook, TikTok, **Bilibili** và link trực tiếp (.mp4).\n",
    "VIDEO_LINK = \"\" #@param {type:\"string\"}\n",
    "TRANG_THAI_VIDEO = \"Riêng tư (private)\" #@param [\"Công khai (public)\", \"Riêng tư (private)\", \"Không công khai (unlisted)\"]\n"
]

# Now rebuild the yt-dlp section with Bilibili support + retry
new_src = []
skip_until_title_config = False

for i, line in enumerate(src):
    if "# --- TẢI TỪ CÁC NGUỒN KHÁC BẰNG YT-DLP ---" in line:
        skip_until_title_config = True
        # Write the new yt-dlp block with Bilibili + retry
        new_src.append("    # --- TẢI TỪ CÁC NGUỒN KHÁC BẰNG YT-DLP ---\n")
        new_src.append("    print(\"🔥 BẮT ĐẦU KÉO VIDEO TỪ NGUỒN BÊN NGOÀI...\")\n")
        new_src.append("    class MyLogger:\n")
        new_src.append("        def debug(self, msg):\n")
        new_src.append("            if 'Extracting URL' in msg:\n")
        new_src.append("                print(f'🔍 Đang trích xuất link video...')\n")
        new_src.append("            elif 'Downloading webpage' in msg or 'Downloading desktop webpage' in msg:\n")
        new_src.append("                print(f'🌐 Đang tải thông tin trang web...')\n")
        new_src.append("            elif 'Downloading m3u8 information' in msg:\n")
        new_src.append("                print(f'📄 Đang tải luồng video...')\n")
        new_src.append("        def info(self, msg):\n")
        new_src.append("            pass\n")
        new_src.append("        def warning(self, msg):\n")
        new_src.append("            print(f'⚠️ Cảnh báo: {msg}')\n")
        new_src.append("        def error(self, msg):\n")
        new_src.append("            print(f'❌ Lỗi tải video: {msg}')\n")
        new_src.append("\n")
        new_src.append("    def my_hook(d):\n")
        new_src.append("        if d['status'] == 'downloading':\n")
        new_src.append("            percent = d.get('_percent_str', '0%').strip()\n")
        new_src.append("            speed = d.get('_speed_str', '0B/s').strip()\n")
        new_src.append("            eta = d.get('_eta_str', 'N/A').strip()\n")
        new_src.append("            percent = re.sub(r'\\x1b\\[[0-9;]*m', '', percent).replace(' ', '')\n")
        new_src.append("            speed = re.sub(r'\\x1b\\[[0-9;]*m', '', speed).replace('MiB/s', 'MB/s').replace('GiB/s', 'GB/s').replace('KiB/s', 'KB/s').replace(' ', '')\n")
        new_src.append("            eta = re.sub(r'\\x1b\\[[0-9;]*m', '', eta)\n")
        new_src.append("            if ':' in eta:\n")
        new_src.append("                parts = eta.split(':')\n")
        new_src.append("                if len(parts) == 3:\n")
        new_src.append("                    eta = f'{int(parts[0])}h {int(parts[1])}m {int(parts[2])}s'\n")
        new_src.append("                elif len(parts) == 2:\n")
        new_src.append("                    eta = f'{int(parts[0])}m {int(parts[1])}s'\n")
        new_src.append("            print(f'\\r⬇️ Đang kéo về: {percent} | Tốc độ: {speed} | Còn lại: {eta}      ', end='')\n")
        new_src.append("        elif d['status'] == 'finished':\n")
        new_src.append("            print('\\n🔄 Đang xử lý file video tải về...')\n")
        new_src.append("\n")
        new_src.append("    ydl_opts = {\n")
        new_src.append("        'outtmpl': '/content/downloaded_video_%(id)s.%(ext)s',\n")
        new_src.append("        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',\n")
        new_src.append("        'merge_output_format': 'mp4',\n")
        new_src.append("        'quiet': True,\n")
        new_src.append("        'no_warnings': True,\n")
        new_src.append("        'logger': MyLogger(),\n")
        new_src.append("        'progress_hooks': [my_hook],\n")
        new_src.append("        'retries': 10,\n")
        new_src.append("        'fragment_retries': 10,\n")
        new_src.append("        'extractor_retries': 5,\n")
        new_src.append("        'file_access_retries': 5,\n")
        new_src.append("        'retry_sleep_functions': {'extractor': lambda n: 2 * n, 'http': lambda n: 2 * n, 'fragment': lambda n: 1},\n")
        new_src.append("        # Bilibili: referer header bắt buộc để không bị chặn\n")
        new_src.append("        'http_headers': {'Referer': 'https://www.bilibili.com/'},\n")
        new_src.append("    }\n")
        new_src.append("\n")
        new_src.append("    # Retry toàn bộ quá trình tải nếu gặp lỗi mạng bất ngờ\n")
        new_src.append("    MAX_RETRIES = 3\n")
        new_src.append("    for attempt in range(1, MAX_RETRIES + 1):\n")
        new_src.append("        try:\n")
        new_src.append("            with yt_dlp.YoutubeDL(ydl_opts) as ydl:\n")
        new_src.append("                info_dict = ydl.extract_info(VIDEO_LINK, download=True)\n")
        new_src.append("                file_name = info_dict.get('title', 'video')\n")
        new_src.append("                downloaded_files = glob.glob('/content/downloaded_video_*')\n")
        new_src.append("                if downloaded_files:\n")
        new_src.append("                    FILE_PATH = downloaded_files[0]\n")
        new_src.append("                else:\n")
        new_src.append("                    raise Exception(\"❌ Không thể tải được video từ link này!\")\n")
        new_src.append("            print(\"\\n✅ Đã tải xong video!\")\n")
        new_src.append("            break  # Tải thành công, thoát vòng lặp\n")
        new_src.append("        except Exception as e:\n")
        new_src.append("            if attempt < MAX_RETRIES:\n")
        new_src.append("                wait = attempt * 3\n")
        new_src.append("                print(f'\\n⚠️ Lỗi lần {attempt}/{MAX_RETRIES}: {str(e)[:100]}')\n")
        new_src.append("                print(f'🔄 Tự động thử lại sau {wait} giây...')\n")
        new_src.append("                time.sleep(wait)\n")
        new_src.append("                # Xóa file tải dở\n")
        new_src.append("                for f in glob.glob('/content/downloaded_video*'):\n")
        new_src.append("                    os.remove(f)\n")
        new_src.append("            else:\n")
        new_src.append("                raise Exception(f\"❌ Đã thử {MAX_RETRIES} lần nhưng không thể tải video!\\n👉 Chi tiết lỗi: {e}\")\n")
        new_src.append("\n")
        continue
    
    if skip_until_title_config:
        if "# 3. Cấu hình tiêu đề mặc định" in line:
            skip_until_title_config = False
            new_src.append(line)
        continue
    
    # T3: Update token save to also backup to Drive
    if "with open(token_file, 'w') as f:" in line:
        new_src.append(line)
        # Find and add the next line (f.write...)
        continue
    if "f.write(youtube_credentials.to_json())" in line:
        new_src.append(line)
        new_src.append("\n")
        new_src.append("# Sao lưu token vào Drive\n")
        new_src.append("BACKUP_DIR = '/content/drive/MyDrive/ColabTube_Backup'\n")
        new_src.append("if os.path.exists(BACKUP_DIR):\n")
        new_src.append("    import shutil\n")
        new_src.append("    shutil.copy2(token_file, os.path.join(BACKUP_DIR, token_file))\n")
        continue
    
    new_src.append(line)

script_cell['source'] = new_src

with open('ColabTube_Uploader.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("Done! All 4 fixes applied.")
