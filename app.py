
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import time

st.set_page_config(page_title="EduFace Detector", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stButton>button {width: 100%; background-color: #4CAF50; color: white; height: 3em; border-radius: 10px;}
    div[data-testid="stMetricValue"] {font-size: 40px;}
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('model_cnn_tubes.h5')
    return model

model = load_model()
class_names = ['Bingung 😐', 'Lelah 🥱', 'Mengerti 💡']

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3069/3069172.png", width=100)
    st.title("Panel Kontrol")
    st.info("Aplikasi ini menggunakan **CNN MobileNetV2**.")
    st.write("---")
    uploaded_file = st.file_uploader("📂 Upload Foto Wajah", type=["jpg", "png", "jpeg"])
    st.write("---")
    st.caption("Dibuat untuk Tugas Besar Deep Learning")

st.title("🎓 Sistem Deteksi Ekspresi Belajar")
st.markdown("#### Kenali kondisi siswa: Apakah mereka *Paham*, *Bingung*, atau *Lelah*?")
st.write("---")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.subheader("📸 Foto Input")
        st.image(image, use_column_width=True, caption="Foto yang diupload")

    with col2:
        st.subheader("🔍 Hasil Analisis")
        if st.button('Mulai Analisis AI ✨'):
            with st.spinner('Sedang memindai wajah...'):
                time.sleep(1) 
                img = image.resize((224, 224))
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = img_array / 255.0

                prediction = model.predict(img_array)
                predicted_index = np.argmax(prediction)
                predicted_label = class_names[predicted_index]
                confidence = prediction[0][predicted_index] * 100

                if 'Mengerti' in predicted_label:
                    st.success(f"Status: **SIAP BELAJAR**")
                    metric_color = "normal"
                elif 'Lelah' in predicted_label:
                    st.warning(f"Status: **BUTUH ISTIRAHAT**")
                    metric_color = "off"
                else: 
                    st.error(f"Status: **BUTUH PENJELASAN ULANG**")
                    metric_color = "inverse"

                st.metric(label="Prediksi Ekspresi", value=predicted_label, delta=f"{confidence:.1f}% Akurat", delta_color=metric_color)
                st.write("Tingkat Keyakinan Model:")
                st.progress(int(confidence))
                with st.expander("📊 Lihat Detail Probabilitas"):
                    st.write("Distribusi probabilitas untuk setiap kelas:")
                    chart_data = {name: float(pred) for name, pred in zip(class_names, prediction[0])}
                    st.bar_chart(chart_data)
else:
    st.info("👈 Silakan upload foto wajah pada menu di sebelah kiri untuk memulai.")
