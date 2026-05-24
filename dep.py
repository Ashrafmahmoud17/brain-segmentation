
import os
import numpy as np
import cv2
from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load model
model = tf.keras.models.load_model("my_modelv1.keras", compile=False)

def preprocess(img):
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def predict_mask(image):
    pred = model.predict(preprocess(image))[0]
    return (pred > 0.5).astype(np.uint8)

def overlay(image, mask):
    mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
    color_mask = np.zeros_like(image)
    color_mask[:, :, 1] = mask * 255
    return cv2.addWeighted(image, 0.7, color_mask, 0.3, 0)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        image = cv2.imread(filepath)

        mask = predict_mask(image)
        over = overlay(image, mask)

        mask_path = os.path.join(RESULT_FOLDER, "mask.png")
        overlay_path = os.path.join(RESULT_FOLDER, "overlay.png")

        cv2.imwrite(mask_path, mask * 255)
        cv2.imwrite(overlay_path, over)

        return render_template(
            "index.html",
            uploaded=filepath,
            mask=mask_path,
            overlay=overlay_path
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

