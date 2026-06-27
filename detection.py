from ultralytics import YOLO
import cv2

# Load the pre-trained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to read frame.")
        break

    # Run object detection
    results = model(frame)

    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()

    # Display the output
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()