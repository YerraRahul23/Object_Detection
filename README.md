# Object Detection Project

## Description

The **Object Detection** project is designed to identify and locate various objects in images or video streams using advanced computer vision techniques. The core of this project leverages **YOLO (You Only Look Once)**, a cutting-edge object detection algorithm known for its real-time performance. YOLO can detect multiple objects in an image or video frame while maintaining both high speed and accuracy, making it suitable for various real-world applications like surveillance, autonomous driving, and more.

## Key Technologies

- **Python**: The primary programming language used in the project for orchestrating the object detection pipeline, integrating libraries, and processing the output.
  
- **YOLO (You Only Look Once)**: A state-of-the-art, deep learning-based object detection algorithm. YOLO processes the entire image in a single forward pass of the neural network to predict objects and their bounding boxes efficiently, making it fast and highly accurate.

- **OpenCV**: A powerful open-source computer vision library. It is used for image processing tasks, capturing video streams from different sources, and integrating with the YOLO model to detect objects in real time.

## Features

- **Real-time object detection**: The project can detect multiple objects in real-time using video streams or pre-recorded video files.
  
- **High Accuracy**: YOLO's architecture is optimized to ensure high precision in detecting objects, while maintaining the ability to process images quickly.
  
- **Video Stream Integration**: The project can capture video from a camera feed or other video input, analyze frames for object detection, and display results with bounding boxes around detected objects.

## Installation and Setup

### Prerequisites
Ensure you have the following dependencies installed on your system:
- Python 3.10
- OpenCV
- NumPy
- YOLO weights and configuration files (download from [google dive](https://drive.google.com/drive/folders/1syGLNd5ECdplhTAj9Xvsc9DTdAsC9854?usp=sharing))

### Steps to Install
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YerraRahul23/Object_Detection.git
   cd object-detection-project
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
