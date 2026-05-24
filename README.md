# 🧠 Brain Tumor Segmentation — Web App

A Flask-based web application for **brain tumor segmentation** using a deep learning model (U-Net / ResU-Net) trained on MRI brain scans. Upload an MRI image and get back a predicted tumor mask with a color overlay.

---

## 📁 Project Structure

```
project/
├── app.py                  # Flask application
├── my_modelV2.keras        # Trained segmentation model
├── static/
│   ├── uploads/            # Uploaded MRI images
│   └── results/            # Generated masks and overlays
├── templates/
│   └── index.html          # Frontend HTML template
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/brain-tumor-segmentation.git
cd brain-tumor-segmentation
```

### 2. Install dependencies

```bash
pip install flask tensorflow opencv-python numpy
```

### 3. Add your trained model

Place your trained `.keras` or `.h5` model file in the root directory and update the path in `app.py`:

```python
model = tf.keras.models.load_model("my_modelV2.keras", compile=False)
```

### 4. Run the app

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000`

---

## 🧩 How It Works

1. **Upload** an MRI brain scan image (`.jpg`, `.png`)
2. The image is **preprocessed** → resized to 256×256 and normalized
3. The model **predicts** a binary segmentation mask
4. The mask is **thresholded** at 0.5 and overlaid on the original image in green
5. Results are displayed: original image, mask, and overlay

---

## 🏗️ Model Architecture

Two models were trained and evaluated:

| Version | Architecture | Loss Function | Notes |
|---------|-------------|---------------|-------|
| V1 | ResU-Net (ResNet50 backbone) | BCE + Dice Loss | Pretrained ImageNet weights |
| V2 | U-Net (from scratch) | Focal Loss + Dice Loss | With augmentation |

### Training Details

| Parameter | Value |
|-----------|-------|
| Input size | 256 × 256 × 3 |
| Batch size | 8 |
| Optimizer | Adam (lr = 1e-4) |
| Epochs | up to 30 (early stopping) |
| Train / Val / Test split | 80% / 10% / 10% |

### Loss Functions

- **Dice Loss** — measures overlap between predicted and ground truth masks
- **Focal Loss** — handles class imbalance (tumor pixels are rare)
- **Combined Loss** = Focal Loss + (1 − Dice Coefficient)

---

## 📊 Dataset

- **Source:** [Brain Tumor Segmentation — Kaggle](https://www.kaggle.com/datasets/nikhilroxtomar/brain-tumor-segmentation)
- **Format:** paired MRI images + binary segmentation masks
- **Augmentation:** horizontal flip, vertical flip (training only)

---

## 📦 Dependencies

```
flask
tensorflow >= 2.x
opencv-python
numpy
matplotlib
scikit-learn
```



---

## 👤 Author

**Ashraf Mohamed**  
Student ID: 223101103  
New Mansoura University — Neural Networks & Deep Learning  
Academic Year 2024–2025
