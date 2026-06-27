# 🎯 Object Detection and Tracking using YOLOv8

## 📌 Project Overview

Object Detection and Tracking is a real-time computer vision application developed as part of the **CodeAlpha Artificial Intelligence Internship (Task 04)**.

The application uses the **YOLOv8 (You Only Look Once)** deep learning model to detect multiple objects in live webcam footage and **ByteTrack** to assign unique IDs, enabling continuous tracking across video frames. It also displays the detection confidence, real-time FPS (Frames Per Second), object count, and saves the processed video automatically.

This project demonstrates practical applications of computer vision, deep learning, and real-time object tracking using Python and OpenCV.

---

## 🚀 Features

- 🎥 Real-time object detection using YOLOv8
- 📦 Multiple object tracking with ByteTrack
- 🏷️ Unique tracking IDs for detected objects
- 📊 Live object counting
- ⚡ FPS (Frames Per Second) display
- 🎯 Bounding boxes with class labels and confidence scores
- 💾 Automatic recording and saving of processed video
- 🖥️ Simple and interactive OpenCV interface

---

## 🛠️ Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- ByteTrack
- NumPy
- PyTorch

---

## 📂 Project Structure

```
CodeAlpha_ObjectDetection/
│
├── output/
│   └── tracked_output.mp4
│
├── detection.py
├── tracking.py
├── requirements.txt
├── README.md
├── .gitignore
└── yolov8n.pt (Downloaded Automatically)
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/CodeAlpha_ObjectDetection.git
cd CodeAlpha_ObjectDetection
```

### 2️⃣ Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Object Detection

```bash
python detection.py
```

### Run Object Detection with Tracking

```bash
python tracking.py
```

The application will:

- Open your webcam
- Detect multiple objects in real time
- Track each object with a unique ID
- Display FPS and object count
- Save the processed video inside the `output` folder

Press **Q** to exit the application.

---

## 📷 Sample Output

The application detects and tracks objects such as:

- 👤 Person
- 💻 Laptop
- 📱 Cell Phone
- 🪑 Chair
- 🧴 Bottle
- 🖥️ Monitor
- 🖱️ Mouse
- 📚 Book

Each detected object is displayed with:

- Bounding Box
- Class Label
- Confidence Score
- Tracking ID

---

## 📊 Project Highlights

- Real-time AI-powered object detection
- Persistent object tracking across frames
- Live object counting
- FPS monitoring
- Automatic video recording
- Lightweight YOLOv8 Nano model for fast performance

---

## 🔮 Future Enhancements

- Support for custom-trained YOLO models
- Line crossing and people counting
- Object speed estimation
- Face recognition integration
- GUI using Streamlit or PyQt
- IP camera and CCTV support

---

## 👩‍💻 Author

**Sriharini Guntupalli**

Artificial Intelligence & Machine Learning Enthusiast

GitHub: https://github.com/harini545

---

## 📜 License

This project is developed for educational and internship purposes under the **CodeAlpha AI Internship**.