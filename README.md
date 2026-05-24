Brain Tumor Segmentation using Deep Learning
Overview

This project is a Deep Learning-based Brain Tumor Segmentation system built using TensorFlow, Keras, OpenCV, and Flask.
The model predicts tumor regions from MRI brain images and generates segmentation masks with overlay visualization.

The project includes:

Data preprocessing
Custom data generators
U-Net and ResUNet architectures
Dice Coefficient and custom loss functions
Model training and evaluation
Flask web application for inference
Features
Brain tumor segmentation from MRI images
U-Net architecture implementation
ResUNet architecture with ResNet50 backbone
Data augmentation support
Dice Coefficient evaluation metric
Focal Loss + Dice Loss combination
Flask web application interface
Overlay visualization of predicted masks
Model saving/loading support
Technologies Used
Python
TensorFlow / Keras
OpenCV
NumPy
Matplotlib
Flask
Scikit-learn
Project Structure
project/
│
├── static/
│   ├── uploads/
│   └── results/
│
├── templates/
│   └── index.html
│
├── my_modelV1.keras
├── my_modelV2.keras
├── app.py
├── train.py
└── README.md
Dataset

The project uses the Brain Tumor Segmentation Dataset from Kaggle.

Dataset contains:

MRI Images
Ground Truth Masks

Dataset structure:

dataset/
│
├── images/
└── masks/
Data Preprocessing

The preprocessing pipeline includes:

Image resizing to 256x256
Normalization
Mask binarization
Data augmentation:
Horizontal flip
Vertical flip
Model Architectures
1. ResUNet
Encoder: ResNet50 pretrained backbone
Decoder: Upsampling + Skip Connections
Output: Binary segmentation mask
2. U-Net

Classic encoder-decoder segmentation architecture with:

Convolution blocks
Batch normalization
Skip connections
Upsampling layers
Loss Functions
Dice Coefficient

Used as evaluation metric.

Dice=
∣X∣+∣Y∣
2∣X∩Y∣
	​


Combined Loss

The project uses:

Focal Loss
Dice Loss
Model Training
Training Configuration
Parameter	Value
Image Size	256x256
Batch Size	8 / 16
Optimizer	Adam
Learning Rate	1e-4
Epochs	10 - 30

Callbacks used:

EarlyStopping
ReduceLROnPlateau
ModelCheckpoint
Flask Web Application

The Flask app allows users to:

Upload MRI image
Generate tumor segmentation mask
Visualize overlay result
Installation
1. Clone Repository
git clone https://github.com/yourusername/brain-tumor-segmentation.git
cd brain-tumor-segmentation
2. Install Dependencies
pip install -r requirements.txt
Requirements
tensorflow
opencv-python
flask
numpy
matplotlib
scikit-learn
pandas
Running the Application
python app.py

Open browser:

http://127.0.0.1:5000/
Training the Model
python train.py
Example Workflow
Upload MRI image
Model predicts segmentation mask
Binary mask generated
Overlay image displayed
Evaluation

The model is evaluated using:

Dice Coefficient
Visual comparison between:
Original Image
Ground Truth
Predicted Mask
Output Examples

The system generates:

Predicted Mask
Overlay Visualization
Future Improvements
Add multi-class tumor segmentation
Improve model accuracy
Deploy using Docker
Add Streamlit interface
Support real-time prediction
Add attention mechanisms
Author

Ashraf Mahmoud

License

This project is for educational and research purposes.
