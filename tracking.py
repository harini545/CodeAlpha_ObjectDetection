from ultralytics import YOLO
import cv2
import time

# Load model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access webcam.")
    exit()

# Video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

if fps == 0:
    fps = 30

# Save output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "output/tracked_output.mp4",
    fourcc,
    fps,
    (width, height)
)

prev_time = time.time()

print("Recording... Press 'q' to quit.")

while True:

    success, frame = cap.read()

    if not success:
        break

    # Track objects
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml"
    )

    annotated_frame = results[0].plot()

    # FPS Calculation
    current_time = time.time()
    fps_value = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps_value)}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    # Count objects
    object_counts = {}

    if results[0].boxes is not None:

        for cls in results[0].boxes.cls:

            name = model.names[int(cls)]

            object_counts[name] = object_counts.get(name, 0) + 1

    # Display object counts
    y = 70

    cv2.putText(
        annotated_frame,
        "Objects Detected",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,0),
        2
    )

    y += 30

    for obj, count in object_counts.items():

        cv2.putText(
            annotated_frame,
            f"{obj}: {count}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

        y += 25

    out.write(annotated_frame)

    cv2.imshow("YOLOv8 Object Detection and Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved successfully!")