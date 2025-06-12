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

## 🖼️ Sample Input

*Here’s an example of an original photo you could upload:*

![sample input](sample_input.png)

---

## 📸 Sample Result

*And here’s the cartoonified output you’ll get:*

![cartoon sample](sample_output.png)

---

## 🖼️ How It Works

1. **Bilateral Filtering** smooths colors while preserving edges.  
2. **Adaptive Thresholding** detects comic-style outlines.  
3. **Bitwise Masking** combines the smoothed color regions with crisp edges.  
4. Optional **enhancers** add finishing polish (soft edges, color boost).

---

## 🙌 Created by
[Shivek Maharaj](https://www.linkedin.com/in/shivek-maharaj/)
