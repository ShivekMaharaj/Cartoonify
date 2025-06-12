import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import io

st.set_page_config(page_title="Cartoonify", layout="wide", page_icon='🖼️')

st.markdown("""
    <style>
    /* Global App Styling */
    .main-header {
        text-align: center;

    }
    .main-header h1 {
        font-size: 4em;
        color: #343A40;
        margin-bottom: 5px;
    }
    .main-header p {
        font-size: 1.1em;
        color: #6C757D;
        margin-top: 0;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #5C7AEA;
        color: white;
        padding: 0.5em 1em;
        border-radius: 8px;
        font-weight: 600;
        border: none;
    }

    .stDownloadButton>button {
        background-color: #20C997;
        color: white;
        padding: 0.5em 1.2em;
        border-radius: 8px;
        font-weight: 600;
        border: none;
    }

    .stDownloadButton>button:hover {
        background-color: #1AA179;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>🎨 Cartoonify</h1>
        <p>Turn your image into a cartoon-style artwork with precision controls and zero coding.</p>
    </div>
""", unsafe_allow_html=True)

DEFAULTS = {
    "boost_color": False,
    "soft_edges": False,
    "d": 9,
    "sigmaColor": 250,
    "sigmaSpace": 250,
    "median_ksize": 7,
    "blockSize": 9,
    "C": 2
}

if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = False

def reset_params():
    for key, val in DEFAULTS.items():
        st.session_state[key] = val
    st.session_state.reset_trigger = True

st.sidebar.title("🛠️ Controls")

if st.sidebar.button("🔄 Reset to Defaults"):
    reset_params()

st.sidebar.markdown("### ✨ Enhancements")
boost_color = st.sidebar.checkbox("Boost Color Saturation", value=st.session_state.get("boost_color", DEFAULTS["boost_color"]), key="boost_color")
soft_edges = st.sidebar.checkbox("Apply Soft Edges", value=st.session_state.get("soft_edges", DEFAULTS["soft_edges"]), key="soft_edges")

st.sidebar.markdown("### 🎛️ Bilateral Filter")
d = st.sidebar.slider("Diameter (d)", 1, 25, DEFAULTS["d"], step=2, key="d")
sigmaColor = st.sidebar.slider("Sigma Color", 1, 300, DEFAULTS["sigmaColor"], key="sigmaColor")
sigmaSpace = st.sidebar.slider("Sigma Space", 1, 300, DEFAULTS["sigmaSpace"], key="sigmaSpace")

st.sidebar.markdown("### 🌀 Median Blur")
median_ksize = st.sidebar.slider("Kernel Size", 1, 15, DEFAULTS["median_ksize"], step=2, key="median_ksize")

st.sidebar.markdown("### 📏 Adaptive Threshold")
blockSize = st.sidebar.slider("Block Size", 3, 51, DEFAULTS["blockSize"], step=2, key="blockSize")
C = st.sidebar.slider("C (threshold subtractor)", -20, 20, DEFAULTS["C"], key="C")

st.sidebar.markdown("### ❓ How It Works")
with st.sidebar.expander("Cartoonify Explained"):
    st.markdown("""
- **Color Smoothing** is applied using a bilateral filter to give a painted look.
- **Edges** are extracted using adaptive thresholding.
- You can control every stage in the process.
- Inspired by anime-style cel shading and classic digital art workflows.
""")

@st.cache_data
def load_image(img_bytes):
    image = np.array(Image.open(io.BytesIO(img_bytes)))
    if image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return image

def cartoonify(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, median_ksize)
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, blockSize=blockSize, C=C)

    color = cv2.bilateralFilter(img, d=d, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)

    if soft_edges:
        color = cv2.edgePreservingFilter(color, flags=1, sigma_s=64, sigma_r=0.2)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    if boost_color:
        pil = Image.fromarray(cartoon)
        enhancer = ImageEnhance.Color(pil)
        cartoon = np.array(enhancer.enhance(1.5))

    return cartoon

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    original = load_image(uploaded_file.read())
    cartooned = cartoonify(original.copy())

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📸 Original Image")
        st.image(original, use_column_width=True)
    with col2:
        st.subheader("🎨 Cartoonified Image")
        st.image(cartooned, use_column_width=True)

    result = Image.fromarray(cartooned)
    buf = io.BytesIO()
    result.save(buf, format="PNG")
    st.download_button(
        label="📥 Download Your Cartoon",
        data=buf.getvalue(),
        file_name="cartoonified.png",
        mime="image/png",
        use_container_width=True
    )

st.markdown("""
    <hr style="margin-top: 40px;">
    <div style="text-align: center; color: #999; font-size: 0.9em;">
        Built by <a href='https://www.linkedin.com/in/shivek-maharaj/' target='_blank' style='color: #5C7AEA;'>Shivek Maharaj</a>
    </div>
""", unsafe_allow_html=True)
