# EduFace Detector — Deteksi Ekspresi Belajar Siswa (CNN)

Aplikasi web untuk mengklasifikasikan **ekspresi belajar siswa** dari foto wajah
menggunakan model **Convolutional Neural Network (CNN) MobileNetV2** (TensorFlow/Keras),
disajikan lewat antarmuka interaktif **Streamlit**.

Aplikasi mengenali 3 kondisi belajar dan menerjemahkannya menjadi rekomendasi:

| Prediksi | Status |
|----------|--------|
| Mengerti | **Siap Belajar** |
| Lelah    | **Butuh Istirahat** |
| Bingung  | **Butuh Penjelasan Ulang** |

## Fitur
- Upload foto wajah dan dapatkan prediksi ekspresi belajar secara real-time.
- Menampilkan **tingkat keyakinan (confidence)** dan **distribusi probabilitas** tiap kelas.
- Antarmuka web sederhana berbasis Streamlit.

## Teknologi
- Python
- TensorFlow / Keras (arsitektur **MobileNetV2**, input 224×224)
- Streamlit (antarmuka web)
- NumPy, Pillow

## Cara Menjalankan
```bash
git clone https://github.com/mine2710/Deteksi-Ekspresi-Wajah.git
cd Deteksi-Ekspresi-Wajah
pip install -r requirements.txt
streamlit run app.py
```
Aplikasi akan terbuka di browser (default: http://localhost:8501).

## Struktur Proyek
```
Deteksi-Ekspresi-Wajah/
├── app.py               # Aplikasi Streamlit + logika inferensi
├── model_cnn_tubes.h5   # Model CNN (MobileNetV2) terlatih
├── requirements.txt     # Dependency (streamlit, tensorflow-cpu, numpy, Pillow)
└── README.md
```

## Cara Kerja Singkat
1. Foto diunggah lalu di-resize ke 224×224 dan dinormalisasi.
2. Model MobileNetV2 memprediksi probabilitas 3 kelas (Bingung, Lelah, Mengerti).
3. Kelas dengan probabilitas tertinggi ditampilkan beserta confidence dan rekomendasi status.

## Dataset
<!-- ISI: sumber & jumlah citra dataset ekspresi belajar yang dipakai untuk melatih model -->

## Hasil
<!-- ISI: akurasi model pada data uji, mis. 85%. Tambahkan screenshot aplikasi jika ada -->

## Author
**Sofyan Fauzi Dzaki Arif** — [github.com/mine2710](https://github.com/mine2710)
Proyek Tugas Besar Deep Learning — Sains Data, ITERA.
