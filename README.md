# Cheating Detection System in Exams using YOLOv8 Pose Estimation

This project uses **YOLOv8 pose estimation** to detect possible **cheating behaviors** during exams by analyzing body and head movements of students. It monitors human posture, gaze direction, and detects suspicious patterns such as side glances, leaning, or signaling.

![YOLOv8](https://img.shields.io/badge/YOLOv8-Pose-green)
![OpenCV](https://img.shields.io/badge/OpenCV-RealTime-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)

---

## 📽️ Demo

> The system uses video input to monitor students and highlights suspected cheating behavior.

https://www.linkedin.com/posts/abdelrahman-helal-3630a4259_cheetingabrdetectionabrsystem-activity-7187054143990022144-fX1l?utm_source=share&utm_medium=member_android

---

## 🔍 Features

- ✅ Real-time student monitoring
- ✅ Head and body keypoint tracking via YOLOv8-pose
- ✅ Detects side glances and unnatural postures
- ✅ Highlights suspicious individuals with red rectangles
- ✅ Frame-by-frame video processing
- ✅ Easy to customize detection logic

---

## 📂 Repository Structure


Cheeting_Detection_System/

├── detect_cheating.py # Main detection script

├── sample_video.mp4 # (Optional) Sample exam footage

├── requirements.txt # Project dependencies

└── README.md # Project documentation



---

## 🧠 How It Works

- Loads a lightweight YOLOv8-pose model (`yolov8n-pose.pt`)
- Processes each video frame to:
  - Detect persons
  - Extract keypoints (head, shoulders, etc.)
  - Analyze head position relative to shoulders
- Draws **red box** if student is frequently turning head sideways

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AbdelRahmanHelal1/Cheeting_Detection_System.git
```
```bash
cd Cheeting_Detection_System
```

# 2. Create and activate virtual environment (optional)

```bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
# 3. Install dependencies

```bash

pip install -r requirements.txt

```

# ▶️ Run the System

```bash
python detect_cheating.py

```
# You can edit the video path inside the script:

python
Copy
Edit

 cap = cv2.VideoCapture("sample_video.mp4")  # or 0 for webcam

# ⚙️ Detection Logic (Simplified)

if head_x > left_shoulder_x + threshold or head_x < right_shoulder_x - threshold:
    mark_as_suspicious()

You can fine-tune the detection by modifying keypoint indices and thresholds in the code.

🧑‍💻 Author

Abdelrahman Helal

🎓 Faculty of Artificial
Intelligence – Menoufia University

💼 Computer Vision & AI Developer

🔗 LinkedIn
