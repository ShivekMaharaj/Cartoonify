# 🎨 Cartoonify

Cartoonify is a clean, interactive Streamlit app that transforms your images into cartoon-style artworks using OpenCV, NumPy, and Pillow. You can upload any image and fine-tune the effect in real-time.

👉 **Live Demo**: [Click here to try it out](https://shivekmaharaj-cartoonify.streamlit.app)  
📦 **Built With**: Python · Streamlit · OpenCV · PIL · NumPy

---

## ✨ Features
- Upload any JPG or PNG image
- Real-time sliders for edge detection, blur, and filtering
- Optional enhancements (soft edges, saturation boost)
- Side-by-side result viewer
- Downloadable output

---

## 🖼️ How It Works

1. **Bilateral Filtering** smooths colors while preserving edges.
2. **Adaptive Thresholding** detects comic-style edges.
3. **Bitwise Masking** combines colors + edges.
4. Optional **enhancers** add finishing polish.

---

## 📸 Sample Result

![cartoon sample](sample_output.png)

---

## 🙌 Created by
[Shivek Maharaj](https://www.linkedin.com/in/shivek-maharaj/)
