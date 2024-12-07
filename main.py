# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p1Qa3rdLsE-vJzdpzvr2S4SEnlvzpaSp
"""

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from google.colab import drive
from google.colab import output  # Add this import statement

# Mount Google Drive
drive.mount('/content/drive')

# Specify the path to the directory containing the dataset in your Google Drive
dataset_dir_path = '/content/drive/My Drive/Student Projects_503629076'

# Define the classes
classes = ['PURPLE CHLORIS', 'CROWFOOT GRASS', 'CELOSIA ARGENTEA L']

# Define image dimensions
img_width, img_height = 150, 150

# Load the training data
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
training_set = train_datagen.flow_from_directory(dataset_dir_path, target_size=(img_width, img_height), batch_size=32, class_mode='categorical')

# Define and compile the model
model = Sequential([
    Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(training_set, epochs=25)

# Function to start webcam and capture a single image
def start_webcam():
    js = Javascript('''
        async function startWebcam() {
            const div = document.createElement('div');
            document.body.appendChild(div);

            const video = document.createElement('video');
            video.style.display = 'block';
            const stream = await navigator.mediaDevices.getUserMedia({video: true});

            document.body.appendChild(video);
            video.srcObject = stream;
            await video.play();

            // Add button to capture image
            const btn = document.createElement('button');
            btn.textContent = 'Capture Image';
            div.appendChild(btn);

            // Capture and return a frame when the button is clicked
            btn.onclick = () => {
                const canvas = document.createElement('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);
                div.appendChild(canvas);

                // Call Python function to process the captured frame
                google.colab.kernel.invokeFunction('notebook.capture', [canvas.toDataURL('image/jpeg', 0.8)], {});
                stream.getVideoTracks()[0].stop();
                video.remove();
                btn.remove(); // Remove the button after capturing image
            };
        }
        startWebcam();
    ''')
    display(js)

# Function to process the captured frame
def process_frame(data):
    jpeg_bytes = b64decode(data.split(',')[1])
    frame = cv2.imdecode(np.frombuffer(jpeg_bytes, dtype=np.uint8), -1)
    frame = cv2.resize(frame, (img_width, img_height))
    frame = np.expand_dims(frame, axis=0)
    frame = preprocess_input(frame)
    return frame

# Function to capture frame using JavaScript and process it
def capture_frame(data):
    # Decode and preprocess the captured frame
    processed_frame = process_frame(data)

    # Make prediction using the model
    prediction = model.predict(processed_frame)
    predicted_class = np.argmax(prediction)

    # Print the type of weed
    print("The captured image is a weed of type:", classes[predicted_class])
    return

# Register the Python function to be invoked by JavaScript
output.register_callback('notebook.capture', capture_frame)

# Run the webcam and capture a single image
start_webcam()