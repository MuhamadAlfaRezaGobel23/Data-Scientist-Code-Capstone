import streamlit as st
import pandas as pd
import os
import hashlib
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from sklearn.decomposition import PCA
import seaborn as sns

sns.set_style("whitegrid")

st.set_page_config(
    page_title="ECOSORT AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open(
r"Dashboard Streamlit/styles/style.css"
) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

if "menu" not in st.session_state:
    st.session_state.menu = "Dataset"
    
# ===== SIDEBAR =====
with st.sidebar:

    st.image(
        r"Dashboard Streamlit/assets/Logo Ecosort.png",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    inactive="#2E5A35"

    dataset_bg="#0B2C13" if st.session_state.menu=="Dataset" else inactive
    dashboard_bg="#0B2C13" if st.session_state.menu=="Dashboard" else inactive

    c1=st.container()
    c2=st.container()

    with c1:
        st.markdown(
        f"""
        <style>
        div[data-testid="stVerticalBlock"] > div:has(#dataset-color)
        + div button{{
            background:{dataset_bg}!important;
        }}
        </style>

        <span id="dataset-color"></span>
        """,
        unsafe_allow_html=True
        )

        if st.button(
            "DataSet",
            key="dataset",
            use_container_width=True
        ):
            st.session_state.menu="Dataset"
            st.rerun()

    with c2:
        st.markdown(
        f"""
        <style>
        div[data-testid="stVerticalBlock"] > div:has(#dashboard-color)
        + div button{{
            background:{dashboard_bg}!important;
        }}
        </style>

        <span id="dashboard-color"></span>
        """,
        unsafe_allow_html=True
        )

        if st.button(
            "Dashboard",
            key="dashboard",
            use_container_width=True
        ):
            st.session_state.menu="Dashboard"
            st.rerun()

# ===== HALAMAN DATASET =====
if st.session_state.menu == "Dataset":

    st.markdown("""
    <div class='main-title'>
        ECOSORT AI
    </div>

    <div class='sub-title'>
        Sistem Cerdas Klasifikasi Sampah dan Rekomendasi Daur Ulang Berbasis Computer Vision
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='deskripsi-box'>
    Sistem ini memanfaatkan pendekatan computer vision untuk melakukan klasifikasi otomatis terhadap jenis sampah serta memberikan rekomendasi metode daur ulang yang sesuai berdasarkan hasil klasifikasi. Sistem ini ditujukan bagi masyarakat umum, rumah tangga, komunitas peduli lingkungan, serta pihak pengelola sampah seperti bank sampah sebagai pengguna dan mitra pendukung dalam proses pengelolaan sampah.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <hr style="
    height:2px;
    border:none;
    background:black;
    margin-top:30px;
    margin-bottom:30px;
    ">
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class='overview-title'>
        Overview Data
    </div>
    """, unsafe_allow_html=True)

    # ================= DATASET 1 =================
    st.markdown("""
    <div class='dataset-title'>
        Data 1 : Waste Classification Dataset
    </div>
    """, unsafe_allow_html=True)

    # ===== METRIC =====
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='metric-box'>
            1.197<br>
            Data Gambar
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-box'>
            6 Kategori<br>
            Sampah
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-box'>
            199/200 Gambar<br>
            Perkategori
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    # ================= CATEGORY BUTTON =================

    if "kategori" not in st.session_state:
        st.session_state.kategori="B3"

    categories=["B3","Glass","Metal",
                "Organic","Paper","Plastic"]

    cols=st.columns(6)

    for i, cat in enumerate(categories):

        active_bg = (
            "#0B2C13"
            if st.session_state.kategori == cat
            else "#2E5A35"
        )

        with cols[i]:

            st.markdown(
            f"""
            <style>
            div[data-testid="stVerticalBlock"] > div:has(#{cat}-color)
            + div button{{
                background:{active_bg}!important;
                color:white!important;
                border:none!important;
                border-radius:10px!important;
                font-weight:700!important;
            }}

            div[data-testid="stVerticalBlock"] > div:has(#{cat}-color)
            + div button:hover{{
                background:#15803D!important;
                color:white!important;
            }}
            </style>

            <span id="{cat}-color"></span>
            """,
            unsafe_allow_html=True
            )

            if st.button(
                cat,
                key=f"cat_{cat}",
                use_container_width=True
            ):
                st.session_state.kategori = cat
                st.rerun()


    # ================= IMAGE DATA =================

    image_data={

    "B3":[
    r"Dashboard Streamlit/assets/B3_001.jpg",
    r"Dashboard Streamlit/assets/B3_030.jpg",
    r"Dashboard Streamlit/assets/B3_091.jpg",
    r"Dashboard Streamlit/assets/B3_152.jpg",
    ],

    "Glass":[
    r"Dashboard Streamlit\assets\Glass_169.jpg",
    r"Dashboard Streamlit\assets\Glass_170.jpg",
    r"Dashboard Streamlit\assets\Glass_171.jpg",
    r"Dashboard Streamlit\assets\Glass_172.jpg",
    ],

    "Metal":[
    r"Dashboard Streamlit\assets\Metal_017.jpg",
    r"Dashboard Streamlit\assets\Metal_077.jpg",
    r"Dashboard Streamlit\assets\Metal_078.jpg",
    r"Dashboard Streamlit\assets\Metal_079.jpg",
    ],

    "Organic":[
    r"Dashboard Streamlit\assets\Organic_001.jpg",
    r"Dashboard Streamlit\assets\Organic_019.jpg",
    r"Dashboard Streamlit\assets\Organic_020.jpg",
    r"Dashboard Streamlit\assets\Organic_021.jpg",
    ],

    "Paper":[
    r"Dashboard Streamlit\assets\Paper_024.jpg",
    r"Dashboard Streamlit\assets\Paper_025.jpg",
    r"Dashboard Streamlit\assets\Paper_026.jpg",
    r"Dashboard Streamlit\assets\Paper_027.jpg",
    ],

    "Plastic":[
    r"Dashboard Streamlit\assets\Plastic_001.jpg",
    r"Dashboard Streamlit\assets\Plastic_002.jpg",
    r"Dashboard Streamlit\assets\Plastic_003.jpg",
    r"Dashboard Streamlit\assets\Plastic_004.jpg",
    ],

    }

    # ================= IMAGE DISPLAY =================

    imgs=image_data[st.session_state.kategori]

    img_cols=st.columns(4)

    for i in range(4):

        with img_cols[i]:

            st.image(
                imgs[i],
                use_container_width=True
            )

    st.markdown("<br>", unsafe_allow_html=True)


    # ===== SOURCE BUTTON pindah bawah gambar =====

    _,btn,_=st.columns([2,1,2])

    with btn:

        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] > div:has(#source-btn)
        + div a{
            background:#0B2C13!important;
            color:white!important;
            border:none!important;
            border-radius:10px!important;
            font-weight:700!important;
            text-align:center!important;
            transition:0.3s!important;
        }

        div[data-testid="stVerticalBlock"] > div:has(#source-btn)
        + div a:hover{
            background:#15803D!important;
            color:white!important;
        }
        </style>

        <span id="source-btn"></span>
        """, unsafe_allow_html=True)

        st.link_button(
            "Lihat Sumber Data",
            "https://www.kaggle.com/datasets/kaanerkez/waste-classfication-dataset",
            use_container_width=True
        )


    # ===== GARIS PEMISAH =====

    st.markdown("""
    <hr style="
    height:2px;
    border:none;
    background:black;
    margin-top:30px;
    margin-bottom:30px;
    ">
    """,unsafe_allow_html=True)

    # ===== DATASET 2 =====
    st.markdown("""
    <div class='dataset-title'>
        Dataset 2 : Jumlah Lokasi Pengangkutan Sampah Kota Surabaya Tahun 2025
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='metric-box'>
            229<br>
            Data
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-box'>
            37<br>
            Kecamatan
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-box'>
            128<br>
            Kelurahan
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    df = pd.read_csv(
    r"Dashboard Streamlit/dataset/data_bank_sampah_clean.csv"
    )

    rows_per_page=10

    if "page" not in st.session_state:
        st.session_state.page=0

    total_rows=len(df)

    total_pages=(total_rows-1)//rows_per_page+1

    start=st.session_state.page*rows_per_page
    end=start+rows_per_page

    st.dataframe(
        df.iloc[start:end],
        use_container_width=True,
        hide_index=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] > div:has(#back-btn)
        + div button{
            background:#0B2C13!important;
            color:white!important;
            border:none!important;
            border-radius:10px!important;
            font-weight:700!important;
            transition:0.3s!important;
        }

        div[data-testid="stVerticalBlock"] > div:has(#back-btn)
        + div button:hover{
            background:#15803D!important;
        }
        </style>

        <span id="back-btn"></span>
        """, unsafe_allow_html=True)
        
        if st.button(
            "Back",
            use_container_width=True,
            disabled=(st.session_state.page == 0)
        ):
            st.session_state.page -= 1
            st.rerun()
        


    with col2:

        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] > div:has(#next-btn)
        + div button{
            background:#0B2C13!important;
            color:white!important;
            border:none!important;
            border-radius:10px!important;
            font-weight:700!important;
            transition:0.3s!important;
        }

        div[data-testid="stVerticalBlock"] > div:has(#next-btn)
        + div button:hover{
            background:#15803D!important;
        }
        </style>

        <span id="next-btn"></span>
        """, unsafe_allow_html=True)
        
        if st.button(
            "Next",
            use_container_width=True,
            disabled=(st.session_state.page >= total_pages - 1)
        ):
            st.session_state.page += 1
            st.rerun()

    with col3:

        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] > div:has(#source-btn)
        + div a{
            background:#0B2C13!important;
            color:white!important;
            border:none!important;
            border-radius:10px!important;
            font-weight:700!important;
            text-align:center!important;
            transition:0.3s!important;
        }

        div[data-testid="stVerticalBlock"] > div:has(#source-btn)
        + div a:hover{
            background:#15803D!important;
            color:white!important;
        }
        </style>

        <span id="source-btn"></span>
        """, unsafe_allow_html=True)

        st.link_button(
            "Lihat Sumber Data",
            "https://ckan.surabaya.go.id/fa_IR/dataset/2900-5187-317/resource/d4b4d976-53cc-449e-8f5b-1138e7d60c52",
            use_container_width=True
        )

# ===== DASHBOARD =====
elif st.session_state.menu == "Dashboard":
    st.markdown("""
    <div class='dashboard-header'>

    <div class='dashboard-title'>
        Dashboard Explanatory Analysis
    </div>

    <div class='dashboard-subtitle'>
        Analisis kualitas dataset dan karakteristik visual
        pada pengembangan model EcoSort AI
    </div>

    <div class='dashboard-line'></div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "Data Quality",
        "Visual Analysis",
        "Feature Analysis"
    ])

    with tab1:
        st.markdown("""
        <div class='question-section'>

        <div class='question-title'>
            Data Quality
        </div>

        <div class='question-line'></div>

        <div class='question-text'>
            Apakah kualitas dataset gambar sampah berdasarkan
            konsistensi ukuran gambar, format file, dan jumlah
            data duplikat sudah memenuhi kebutuhan proses
            training model pada tahap persiapan data?
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        dataset_path = "Dashboard Streamlit/Dataset Capstone"
        clean_path = "Dashboard Streamlit/Dataset_Cleaned"

        # =====================================================
        # VISUALISASI 1 - UKURAN GAMBAR
        # =====================================================
        @st.cache_data
        def load_sizes(dataset_path, clean_path):

            raw_sizes = []
            clean_sizes = []

            # RAW
            for root, dirs, files in os.walk(dataset_path):
                for file in files:

                    path = os.path.join(root, file)

                    try:
                        img = Image.open(path)
                        raw_sizes.append(img.size[0])

                    except:
                        pass

            # CLEAN
            for root, dirs, files in os.walk(clean_path):
                for file in files:

                    path = os.path.join(root, file)

                    try:
                        img = Image.open(path)
                        clean_sizes.append(img.size[0])

                    except:
                        pass

            return raw_sizes, clean_sizes
    
        raw_sizes, clean_sizes = load_sizes(
        dataset_path,
        clean_path)

        # =========================================
        # PLOT
        # =========================================

        fig, ax = plt.subplots(1, 2, figsize=(12,5))

        # WARNA SAMA
        color_hist = "#046205"

        # -----------------------------------------
        # SEBELUM CLEANING
        # -----------------------------------------

        counts1, bins1, patches1 = ax[0].hist(
            raw_sizes,
            bins=20,
            color=color_hist
        )

        ax[0].set_title("Ukuran Gambar Sebelum Cleaning")
        ax[0].set_xlabel("Ukuran Gambar")
        ax[0].set_ylabel("Jumlah")

        # TAMPILKAN NILAI
        for count, patch in zip(counts1, patches1):

            if count > 0:

                ax[0].text(
                    patch.get_x() + patch.get_width()/2,
                    count,
                    int(count),
                    ha='center',
                    va='bottom',
                    fontsize=8,
                    fontweight="bold"
                )

        # -----------------------------------------
        # SESUDAH CLEANING
        # -----------------------------------------

        counts2, bins2, patches2 = ax[1].hist(
            clean_sizes,
            bins=20,
            color=color_hist
        )

        ax[1].set_title("Ukuran Gambar Sesudah Cleaning")
        ax[1].set_xlabel("Ukuran Gambar")
        ax[1].set_ylabel("Jumlah")

        # TAMPILKAN NILAI
        for count, patch in zip(counts2, patches2):

            if count > 0:

                ax[1].text(
                    patch.get_x() + patch.get_width()/2,
                    count,
                    int(count),
                    ha='center',
                    va='bottom',
                    fontsize=8,
                    fontweight="bold"
                )

        plt.tight_layout()
        st.pyplot(fig)

        with st.expander("Insight"):

            st.write("""       
            Visualisasi menunjukkan bahwa dataset sebelum proses cleaning memiliki variasi ukuran gambar yang cukup beragam. Sebagian besar gambar memiliki ukuran besar sekitar 500 piksel, namun masih terdapat beberapa gambar dengan ukuran yang lebih kecil dan tidak konsisten.
            
            Setelah proses cleaning dilakukan, distribusi ukuran gambar menjadi lebih konsisten dengan dominasi ukuran gambar yang seragam. Hal ini menunjukkan bahwa proses cleaning berhasil meningkatkan kualitas dataset dan mempermudah proses preprocessing pada tahap training model.
            Konsistensi ukuran gambar membantu model menerima input yang lebih stabil sehingga proses pembelajaran dapat berjalan lebih optimal.
            """)

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================================
        # VISUALISASI 2 - FORMAT FILE
        # =====================================================
        @st.cache_data
        def load_formats(dataset_path, clean_path):

            raw_formats = {}
            clean_formats = {}

            # RAW
            for root, dirs, files in os.walk(dataset_path):
                for file in files:

                    ext = file.split('.')[-1].lower()

                    raw_formats[ext] = (
                        raw_formats.get(ext, 0) + 1
                    )

            # CLEAN
            for root, dirs, files in os.walk(clean_path):
                for file in files:

                    ext = file.split('.')[-1].lower()

                    clean_formats[ext] = (
                        clean_formats.get(ext, 0) + 1
                    )

            return raw_formats, clean_formats
        
        raw_formats, clean_formats = load_formats(
        dataset_path,
        clean_path
        )

        colors_raw = ['#50B468', '#046205']
        colors_clean = ['#046205', '#50B468']

        fig, ax = plt.subplots(1, 2, figsize=(12,5))

        # PIE RAW
        wedges, texts, autotexts = ax[0].pie(
            raw_formats.values(),
            labels=raw_formats.keys(),
            autopct='%1.1f%%',
            colors=colors_raw
        )

        # ubah warna persen
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax[0].set_title("Format File Sebelum Cleaning")

        # PIE CLEAN
        wedges, texts, autotexts = ax[1].pie(
            clean_formats.values(),
            labels=clean_formats.keys(),
            autopct='%1.1f%%',
            colors=colors_clean
        )

        # ubah warna persen
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax[1].set_title("Format File Sesudah Cleaning")

        plt.tight_layout()

        st.pyplot(fig)

        with st.expander("Insight"):
    
            st.write("""
            Sebelum proses cleaning, dataset masih terdiri dari beberapa format file yaitu JPG dan JPEG. Format JPG mendominasi dataset dengan persentase sekitar 95.5%, sedangkan format JPEG hanya sebagian kecil dari keseluruhan dataset dengan persentase 4.5%. Setelah cleaning dilakukan, seluruh gambar berhasil diseragamkan ke dalam format JPG sehingga dataset menjadi lebih konsisten. Standardisasi format file membantu mengurangi potensi error pada proses loading data dan membuat pipeline preprocessing menjadi lebih stabil dan efisien.
            """)

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================================
        # VISUALISASI 3 - DUPLIKAT
        # =====================================================
        @st.cache_data
        def count_duplicates(dataset_path):

            hashes = {}
            duplicates = 0

            for root, dirs, files in os.walk(dataset_path):
                for file in files:

                    path = os.path.join(root, file)

                    try:
                        with open(path, 'rb') as f:
                            file_hash = hashlib.md5(
                                f.read()
                            ).hexdigest()

                        if file_hash in hashes:
                            duplicates += 1
                        else:
                            hashes[file_hash] = path

                    except:
                        pass

            return duplicates

        raw_duplicates = count_duplicates(dataset_path)
        clean_duplicates = count_duplicates(clean_path)

        fig = plt.figure(figsize=(4,3))

        ax = sns.barplot(
            x=["Sebelum Cleaning", "Sesudah Cleaning"],
            y=[raw_duplicates, clean_duplicates],
            palette=["#046205", "#86EFAC"]   
        )

        plt.title("Perbandingan Jumlah Data Duplikat")
        plt.ylabel("Jumlah Duplikat")

        # Menampilkan nilai di atas bar
        for bar in ax.patches:

            height = bar.get_height()

            ax.text(
                bar.get_x() + bar.get_width()/2,
                height + 0.05,
                f'{int(height)}',
                ha='center',
                fontsize=11,
                fontweight='bold'
            )

        # st.pyplot(fig)
        st.pyplot(fig, use_container_width=False)

        with st.expander("Insight"):

            st.write("""
            Sebelum proses cleaning, dataset masih memiliki 3 data duplikat. Setelah cleaning dilakukan, seluruh data duplikat berhasil dihapus sehingga jumlah data duplikat menjadi 0. Penghapusan data duplikat sangat penting untuk mengurangi risiko overfitting pada model deep learning. Data yang berulang dapat menyebabkan model terlalu menghafal pola tertentu dan menurunkan kemampuan generalisasi terhadap data baru.
            """)
    
    # =========================================================
    # PERTANYAAN 2
    # =========================================================
    with tab2:
        st.markdown("""
        <div class='question-section'>

        <div class='question-title'>
            Visual Analysis
        </div>

        <div class='question-line'></div>

        <div class='question-text'>
        Bagaimana distribusi warna dan tingkat pencahayaan pada setiap kategori sampah memengaruhi kebutuhan preprocessing gambar dalam pengembangan model EcoSort AI?
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        clean_path = "Dataset_Cleaned"

        # =====================================================
        # VISUALISASI 1 - BRIGHTNESS
        # =====================================================
        @st.cache_data
        def load_brightness(clean_path):

            brightness = []

            for root, dirs, files in os.walk(clean_path):
                for file in files:

                    path = os.path.join(root, file)

                    try:
                        img = Image.open(path).convert('L')

                        brightness.append(
                            np.mean(img)
                        )

                    except:
                        pass

            return brightness

        brightness = load_brightness(clean_path)

        fig = plt.figure(figsize=(8,5))

        ax = sns.histplot(
            brightness,
            bins=30,
            kde=True,
            color="#046205"
        )

        # Menampilkan nilai pada setiap batang
        for patch in ax.patches:

            height = patch.get_height()

            if height > 0:

                ax.text(
                    patch.get_x() + patch.get_width()/2,
                    height,
                    f'{int(height)}',
                    ha='center',
                    va='bottom',
                    fontsize=8
                )

        plt.title("Distribusi Brightness Gambar")
        plt.xlabel("Brightness")
        plt.ylabel("Jumlah")
        st.pyplot(fig)

        with st.expander("Insight"):

            st.write("""
            Distribusi brightness menunjukkan bahwa dataset memiliki tingkat pencahayaan yang cukup beragam dengan mayoritas gambar berada pada tingkat brightness menengah hingga tinggi. Rata-rata distribusi brightness berkisar di angka 150 hingga 200, Variasi pencahayaan ini menunjukkan bahwa gambar diambil pada kondisi lingkungan yang berbeda-beda sehingga dataset menjadi lebih representatif terhadap kondisi nyata. Namun, variasi brightness yang terlalu ekstrem tetap perlu ditangani melalui preprocessing seperti normalisasi dan augmentasi brightness agar model lebih robust terhadap perubahan pencahayaan.
            """)

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================================
        # VISUALISASI 2 - DISTRIBUSI WARNA
        # =====================================================
        @st.cache_data
        def load_mean_colors(clean_path):

            mean_colors = []

            for root, dirs, files in os.walk(clean_path):
                for file in files:

                    path = os.path.join(root, file)

                    try:
                        img = cv2.imread(path)

                        mean_color = img.mean(
                            axis=(0,1)
                        )

                        mean_colors.append(mean_color)

                    except:
                        pass

            return np.array(mean_colors)
        
        mean_colors = load_mean_colors(clean_path)

        fig = plt.figure(figsize=(8,5))

        sns.boxplot(
            data=pd.DataFrame({
                "Blue": mean_colors[:,0],
                "Green": mean_colors[:,1],
                "Red": mean_colors[:,2]
            }),
        
                palette={
                "Blue": "blue",
                "Green": "green",
                "Red": "red"
            }
        )

        plt.title("Distribusi Rata-rata Warna")
        plt.ylabel("Pixel Intensity")

        st.pyplot(fig)

        with st.expander("Insight"):

            st.write("""
            Visualisasi distribusi rata-rata warna menunjukkan bahwa kanal warna Red, Green, dan Blue memiliki sebaran intensitas yang cukup beragam. Kanal warna merah dan hijau cenderung memiliki intensitas yang lebih tinggi dibandingkan biru.
            
            Hal ini menunjukkan bahwa dataset memiliki variasi karakteristik visual antar kategori sampah, seperti warna alami pada sampah organik serta warna reflektif pada kategori kaca dan logam. Variasi warna ini dapat membantu model mempelajari pola visual yang lebih kompleks.
            """)

    # =========================================================
    # PERTANYAAN 3
    # =========================================================
    with tab3:
        st.markdown("""
        <div class='question-section'>

        <div class='question-title'>
            Feature Analysis
        </div>

        <div class='question-line'></div>

        <div class='question-text'>
        Bagaimana kemampuan fitur hasil ekstraksi gambar dalam membedakan kategori sampah berdasarkan persebaran fitur PCA pada tahap pengembangan model EcoSort AI?
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================================
        # PCA VISUALIZATION
        # =====================================================
        df_final = pd.read_csv("Dashboard Streamlit/dataset/hasil_ekstraksi_fitur.csv")

        @st.cache_data
        def load_pca(df_final):

            X = df_final.drop(
                columns=["Nama File", "Kategori"]
            )

            pca = PCA(n_components=2)

            hasil_pca = pca.fit_transform(X)

            df_pca = pd.DataFrame({
                "PCA1": hasil_pca[:,0],
                "PCA2": hasil_pca[:,1],
                "Kategori": df_final["Kategori"]
            })

            return df_pca

        # Mapping label
        label_map = {
            0: "B3",
            1: "Glass",
            2: "Metal",
            3: "Organic",
            4: "Paper",
            5: "Plastic"
        }

        df_pca = load_pca(df_final)

        df_pca["Kategori"] = df_pca["Kategori"].map(label_map)

        # Plot
        fig = plt.figure(figsize=(8,5))

        for kategori in df_pca["Kategori"].unique():

            subset = df_pca[
                df_pca["Kategori"] == kategori
            ]

            plt.scatter(
                subset["PCA1"],
                subset["PCA2"],
                label=kategori,
                alpha=0.7
            )

        plt.title("Visualisasi Persebaran Fitur Sampah Menggunakan PCA")
        plt.xlabel("PCA 1")
        plt.ylabel("PCA 2")
        plt.legend()
        plt.tight_layout()
        st.pyplot(fig)

        with st.expander("Insight"):

            st.write("""
            Berdasarkan visualisasi PCA, terlihat bahwa beberapa kategori sampah membentuk pola persebaran yang cukup terpisah, seperti kategori Organic dan Metal, sehingga menunjukkan bahwa fitur hasil ekstraksi gambar mampu menangkap karakteristik visual tertentu dari masing-masing kategori.

            Namun, beberapa kategori seperti Glass, Plastic, dan Paper masih memiliki banyak titik yang saling bertumpuk, yang mengindikasikan adanya kemiripan karakteristik visual antar kategori tersebut sehingga berpotensi menyebabkan model klasifikasi mengalami kesulitan dalam membedakannya secara akurat.
            """)
    
    # =====================================================
    # KESIMPULAN
    # =====================================================
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='question-section'>

    <div class='question-title'>
        Kesimpulan
    </div>

    <div class='question-line'></div>

    <div class='question-text'>
    Berdasarkan hasil explanatory analysis, proses cleaning berhasil meningkatkan kualitas dataset EcoSort AI melalui konsistensi ukuran gambar, standardisasi format file, serta penghapusan data duplikat. Dataset juga menunjukkan variasi brightness dan distribusi warna yang cukup beragam, sehingga mampu merepresentasikan kondisi visual yang lebih realistis.
    <br><br>
    Selain itu, visualisasi PCA menunjukkan bahwa beberapa kategori memiliki karakteristik visual yang cukup terpisah, meskipun masih terdapat beberapa kelas yang memiliki kemiripan visual. Secara keseluruhan, dataset dinilai cukup baik untuk pengembangan model klasifikasi sampah.
    </div>

    </div>
    """, unsafe_allow_html=True)