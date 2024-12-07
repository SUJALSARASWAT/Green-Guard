
# 🌱 **Green Guard – AI Weed Detection System**  

**Green Guard** is a machine learning-based system designed to identify and classify different types of weeds using image recognition. By leveraging deep learning and a webcam interface, this project enables quick and accurate weed identification, contributing to efficient agricultural practices.  

---

## 🎯 **Features**  

- **Real-Time Weed Detection:** Captures images directly from the webcam for on-the-spot weed classification.  
- **Accurate Classification:** Classifies weeds into one of the following types:  
  - **Purple Chloris**  
  - **Crowfoot Grass**  
  - **Celosia Argentea L**  
- **User-Friendly Interface:** Simple and intuitive system for farmers, researchers, and agricultural professionals.  
- **Dataset Flexibility:** Utilizes custom weed datasets to enhance model accuracy.  

---

## 💻 **Technologies Used**  

- **Python**  
- **OpenCV**  
- **TensorFlow/Keras**  
- **NumPy**  
- **Google Colab**  

---

## 📋 **Requirements**  

Before running the application, ensure you have the following:  

- Python 3.x  
- pip  

Install the required Python packages:  
```bash  
pip install tensorflow opencv-python numpy  
```  

---

## 🗂️ **Dataset**  

The project uses three datasets for training the model:  

1. **Purple Chloris**  
2. **Crowfoot Grass**  
3. **Celosia Argentea L**  

Place your datasets in the following structure:  

```plaintext  
dataset_dir_path/  
├── Purple_Chloris/  
│   ├── image1.jpg  
│   ├── image2.jpg  
│   └── ...  
├── Crowfoot_Grass/  
│   ├── image1.jpg  
│   ├── image2.jpg  
│   └── ...  
└── Celosia_Argentea_L/  
    ├── image1.jpg  
    ├── image2.jpg  
    └── ...  
```  

---

## 🚀 **Getting Started**  

1. **Clone the Repository:**  
   ```bash  
   git clone https://github.com/your-username/green-guard.git  
   ```  

2. **Change into the Project Directory:**  
   ```bash  
   cd green-guard  
   ```  

3. **Upload Your Dataset:**  
   Ensure your datasets are structured as mentioned above.  

4. **Train the Model:**  
   Train the deep learning model using the dataset:  
   ```python  
   python train_model.py  
   ```  

5. **Run the Application:**  
   Use a webcam to capture images for weed detection:  
   ```python  
   python main.py  
   ```  

---

## 🎮 **Usage Instructions**  

1. Launch the application and allow camera access.  
2. Capture an image of the weed using the on-screen button.  
3. The system will process the image and display the identified weed type.  

---

## 🔧 **File Structure**  

```plaintext  
green-guard/  
├── dataset/                # Weed datasets for training  
├── main.py                 # Main application script  
├── train_model.py          # Script to train the deep learning model  
├── model.h5                # Pre-trained model weights (optional)  
├── requirements.txt        # Python dependencies  
├── README.md               # Project documentation  
└── LICENSE                 # Project license  
```  

---

## 🖌️ **Contributing**  

We welcome contributions to enhance the system's functionality or improve the weed classification model. Fork the repository and submit a pull request with your changes.  

