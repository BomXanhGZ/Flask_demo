# 🚀 Application Setup Guide

## 📌 Backend (Flask)

### 1. Setup & Run

Install dependencies using a Virtual Environment:
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate on Windows
source venv/Scripts/activate

# Install requirements
pip install -r requirements.txt
```

Chạy server backend:
```bash
python wsgi.py
```
API sẽ hoạt động tại: `http://127.0.0.1:5000/api`


### 2. Thao tác Database (Flask-Migrate)
Cấu hình Database được đặt tại `backend/app/settings.py`. Để quản lý database bằng Migrate, sử dụng các lệnh sau trong thư mục `backend`:

- **Khởi tạo migrate** (chỉ cần chạy 1 lần đầu tiên):
  ```bash
  python -m app.manage db init
  ```

  - **Tạo migration file**:
  ```bash
  python -m app.manage db migrate -m "create user table"
  ```

- **Cập nhật database** (apply các thay đổi migration vào DB thật):
  ```bash
  python -m app.manage db upgrade
  ```

---

## 📌 Frontend (Vue.js)

### 1. Cài đặt & Khởi chạy

Cài đặt các gói phụ thuộc:
```bash
cd frontend
npm install
```

Chạy server frontend (Dev mode):
```bash
npm run dev
```
