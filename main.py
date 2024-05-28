from ultralytics import YOLO  # Import the YOLO class from the ultralytics module
import cv2  # OpenCV library for video processing
import numpy as np  # NumPy for numerical operations
import pickle  # Pickle for object serialization (though not used in this snippet)
import cvzone  # CVZone for additional OpenCV utilities
import math  # Math library for mathematical operations

# Load the YOLO model for pose estimation
model = YOLO("yolov8n-pose.pt")

# Open the video file
cap = cv2.VideoCapture("VID_20240415_114845.mp4")
data = []

# Loop to read frames from the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if there are no frames left to read

    frame = cv2.resize(frame, (600, 500))  # Resize the frame for processing
    result = model.predict(frame)  # Predict pose using the YOLO model
    boxes = result[0].boxes.xyxy.cpu().numpy().astype(int)  # Extract bounding boxes
    keypoint = result[0].keypoints.data.cpu().numpy().astype("float")  # Extract keypoints

    # Loop through detected keypoints
    for idd, lm in enumerate(keypoint):
        x1, y1, x2, y2 = boxes[idd]
        x2 = x2 - x1
        y2 = y2 - y1
        distance = np.sqrt(int(lm[0][1])**2 + int(lm[16][1])**2)  # Calculate distance

        # Check keypoint positions to determine rectangle color
        if int(lm[6][0]) + 20 > int(lm[0][0]) or int(lm[0][0]) > (int(lm[5][0]) - 20):
            cvzone.cornerRect(frame, (x1, y1, x2, y2), colorC=(0, 0, 255))  # Draw red rectangle
        else:
            cvzone.cornerRect(frame, (x1, y1, x2, y2))  # Draw default rectangle

    # Display the frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):  # Exit if 'q' key is pressed
        break

cap.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
