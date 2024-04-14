import cv2
import time

def detect_faces_from_camera():
    # Load the pre-trained Haar Cascade model for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Start video capture from the default camera
    cap = cv2.VideoCapture(0)

    # Check if the video capture has been initialized correctly
    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    index = 0  # Initialize the image index
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Save the captured image with an index
            cv2.imwrite(f'detected_faces_{index}.jpg', frame)
            index += 1  # Increment the index for the next image

            print(f"Captured image {index} with {len(faces)} faces detected.")

            time.sleep(5)  # Wait for 5 seconds before capturing the next image

    finally:
        # When everything is done, release the capture
        cap.release()

detect_faces_from_camera()
