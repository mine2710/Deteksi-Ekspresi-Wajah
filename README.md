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

## Dataset & Pelatihan
Model dilatih untuk mengenali **3 kelas ekspresi belajar**: Bingung, Lelah, dan Mengerti,
dari citra wajah. Arsitektur menggunakan **transfer learning MobileNetV2** dengan ukuran
input 224×224 dan normalisasi piksel (pembagian 255). Bobot hasil pelatihan disimpan pada
`model_cnn_tubes.h5` dan dimuat langsung oleh aplikasi untuk inferensi.

## Hasil
- Aplikasi memberikan **prediksi kelas** beserta **confidence score** dan **distribusi
  probabilitas** ketiga kelas secara langsung dari foto yang diunggah.
- Setiap prediksi diterjemahkan menjadi rekomendasi tindakan (Siap Belajar / Butuh
  Istirahat / Butuh Penjelasan Ulang) agar hasil model mudah dipahami pengguna non-teknis.

> Catatan: metrik akurasi & screenshot antarmuka dapat ditambahkan di sini bila tersedia.

## Author
**Sofyan Fauzi Dzaki Arif** — [github.com/mine2710](https://github.com/mine2710)
Proyek Tugas Besar Deep Learning — Sains Data, ITERA.
