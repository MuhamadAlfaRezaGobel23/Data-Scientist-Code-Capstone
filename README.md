# EcoSort AI

## Sistem Cerdas Klasifikasi Sampah dan Rekomendasi Daur Ulang Berbasis Computer Vision

EcoSort AI merupakan proyek Capstone yang dikembangkan untuk membantu masyarakat melakukan klasifikasi sampah secara otomatis menggunakan teknologi Computer Vision serta memberikan rekomendasi pengelolaan sampah yang sesuai.

Sistem ini menggabungkan:

* Klasifikasi sampah berbasis AI
* Analisis data dan visualisasi interaktif
* Informasi lokasi bank sampah
* Artikel edukasi pengelolaan sampah
* Dashboard berbasis Streamlit

Proyek ini dikembangkan dalam tema **Sustainable Living & Responsible Consumption**. 


# 🎯 Tujuan Proyek

* Menyiapkan dataset gambar sampah yang berkualitas
* Melakukan cleaning dan preprocessing data
* Melakukan feature engineering
* Membuat dashboard analisis interaktif
* Mendukung pengembangan sistem klasifikasi sampah otomatis
* Menyediakan informasi pengelolaan sampah dan bank sampah terdekat 


# ✨ Fitur Utama

### Data Preparation

* Data Gathering
* Data Assessing
* Data Cleaning

### Data Analysis

* Exploratory Data Analysis (EDA)
* Explanatory Analysis
* PCA Visualization

### Feature Engineering

* Ekstraksi fitur menggunakan ResNet50

### A/B Testing

* Evaluasi preprocessing gambar
* Evaluasi sistem rekomendasi bank sampah

### Dashboard

* Dataset Information
* Dashboard Analysis
* Visualisasi interaktif Streamlit


# 📂 Struktur Repository

```text
EcoSort-AI/
│
├── AB TESTING/
├── Dashboard Streamlit/
├── Dataset/
├── Laporan Teknis Komprehensif/
│
├── artikel_capstone.json
├── artikel_capstone_ecosort.json
├── cleaning.ipynb
├── data_bank_sampah_clean.csv
├── data_bank_sampah_clean.json
├── Dataset_Artikel_Daur_Ulang.ipynb
├── hasil_ekstraksi_fitur.json
├── proses_data_bank_sampah.ipynb
├── scraping_artikel.py
│
└── README.md
```


# 📁 Penjelasan Folder

## AB TESTING

Berisi implementasi dan evaluasi A/B Testing untuk:

* Dataset klasifikasi sampah
* Sistem rekomendasi bank sampah


## Dashboard Streamlit

Berisi source code dashboard interaktif EcoSort AI.

Struktur:

```text
Dashboard Streamlit/
│
├── Dataset Capstone/
├── Dataset Cleaned/
├── assets/
├── dataset/
├── styles/
│
├── dashboard capstone.py
├── requirements.txt
```

### Dataset Capstone

Dataset mentah (raw dataset) sebelum cleaning.

### Dataset Cleaned

Dataset hasil preprocessing yang digunakan untuk analisis dan dashboard.

### assets

Logo, gambar, ikon, dan aset visual dashboard.

### dataset

Dataset pendukung visualisasi dashboard.

### styles

CSS custom untuk Streamlit.

### dashboard capstone.py

File utama aplikasi Streamlit.

### requirements.txt

Daftar dependency aplikasi.


## Dataset

Berisi seluruh dataset yang digunakan selama pengembangan proyek.

Meliputi:

* Dataset gambar sampah
* Dataset bank sampah
* Dataset artikel edukasi


## Laporan Teknis Komprehensif

Dokumentasi lengkap proyek mulai dari data understanding hingga deployment.


# 📄 Penjelasan File

## cleaning.ipynb

Notebook untuk:

* Deteksi file corrupt
* Penghapusan data duplikat
* Resize gambar
* Normalisasi
* Denoising


## proses_data_bank_sampah.ipynb

Preprocessing dataset bank sampah.


## Dataset_Artikel_Daur_Ulang.ipynb

Pengolahan artikel edukasi dan daur ulang.


## scraping_artikel.py

Web scraping artikel dari sumber edukasi lingkungan.


## hasil_ekstraksi_fitur.json

Hasil feature extraction menggunakan ResNet50.

Setiap gambar menghasilkan 2048 fitur numerik. 


# 🔄 Workflow Project

```text
Gathering Data
      ↓
Assessing Data
      ↓
Cleaning Data
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
A/B Testing
      ↓
Dashboard Streamlit
      ↓
Deployment
```


# 📊 Dataset

## Dataset Klasifikasi Sampah

Kategori:

* B3
* Glass
* Metal
* Organic
* Paper
* Plastic

Jumlah data awal:

* 1200 gambar

Jumlah data setelah cleaning:

* 1197 gambar  


## Dataset Bank Sampah

* 229 lokasi
* 37 kecamatan
* 128 kelurahan

Digunakan untuk sistem rekomendasi bank sampah. 


## Dataset Artikel Edukasi

* 70 artikel
* 6 kategori

Digunakan untuk fitur rekomendasi artikel. 


# 🛠️ Teknologi yang Digunakan

| Teknologi    | Fungsi                    |
| ------------ | ------------------------- |
| Python       | Bahasa utama              |
| Streamlit    | Dashboard                 |
| Pandas       | Data Processing           |
| NumPy        | Numerical Computing       |
| Matplotlib   | Visualization             |
| Seaborn      | Statistical Visualization |
| OpenCV       | Image Processing          |
| Pillow       | Image Handling            |
| Scikit-Learn | PCA dan Analisis          |
| ResNet50     | Feature Extraction        |


# 🚀 Instalasi

## Clone Repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

```bash
cd REPOSITORY
```

## Membuat Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

## Install Dependency

```bash
pip install -r requirements.txt
```


# ▶️ Menjalankan Dashboard

Masuk ke folder Dashboard Streamlit:

```bash
cd "Dashboard Streamlit"
```

Jalankan aplikasi:

```bash
streamlit run "Dashboard Streamlit/dashboard_capstone.py"
```

Buka browser:

```text
http://localhost:8501
```


# 👥 Tim Pengembang

### Data Scientist

* Muhammad Aqsa Firdaus
* Muhamad Alfa Reza Gobel

### AI Engineer

* Maysahayu Artika Maharani
* Putri Manika Rukmamaya

### Full Stack Developer

* Muhammad Dafa Alvin Zuhdi
* Cathrine Natalia Koeswandono


# 📄 Lisensi

Proyek ini dikembangkan untuk kebutuhan Capstone Project dan tujuan edukasi.
