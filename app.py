import streamlit as st
from PIL import Image
import numpy as np
import pydicom
from model_placeholder import predict_severity, predict_subtype
from clinical_guideline import get_recommendation

# 🌸 Set halaman
st.set_page_config(
    page_title="Breast Cancer AI Detector",
    page_icon="🎗️",
    layout="wide",
)

# 🌸 Judul Utama
st.markdown("<h1 style='color:#C71585;'>🎀 Breast Cancer Detection & Clinical Recommendation</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#555555;'>Upload Mammogram untuk Analisis Keganasan dan Subtipe Molekuler oleh Sistem AI.</p>", unsafe_allow_html=True)

# 📤 Upload File
st.markdown("---")
uploaded_file = st.file_uploader("📤 Upload Gambar", type=["dcm", "jpeg", "jpg", "png"])

if uploaded_file is not None:
    file_type = uploaded_file.type  # MIME type

    if uploaded_file.name.endswith(".dcm"):
        import pydicom
        ds = pydicom.dcmread(uploaded_file)
        image_array = ds.pixel_array
        image = Image.fromarray(image_array).convert("RGB")
    else:
        image = Image.open(uploaded_file).convert("RGB")
    
    # Resize and convert to NumPy array
    image_resized = image.resize((224, 224))
    img_array = np.array(image_resized)

    # Layout 2 kolom
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, caption="📸 Mammogram Image", use_container_width=True)

    with col2:
        severity = predict_severity(img_array)
        st.markdown("### 💡 Prediksi Tingkat Keganasan")
        if severity == 'Malignant':
            st.error(f"**{severity}** - Perlu evaluasi lanjut.")
        elif severity == 'Benign':
            st.warning(f"**{severity}** - Lesi jinak, lanjut observasi.")
        else:
            st.success(f"**{severity}** - Tidak terdeteksi abnormalitas.")

        if severity == 'Malignant':
            subtype = predict_subtype(img_array)
            st.markdown("### 🧬 Subtipe Molekuler")
            st.info(f"**{subtype}**")

            st.markdown("### 📝 Rekomendasi Klinis")
            st.markdown(f"<div style='background-color:#ffe4ec; padding:10px; border-radius:10px;'>{get_recommendation(subtype)}</div>", unsafe_allow_html=True)
