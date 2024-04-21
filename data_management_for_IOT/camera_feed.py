# from flask import Flask, Response
# import picamera
# import picamera.array
# import face_recognition
# import numpy as np
# import time
# import io
# import pickle

# app = Flask(__name__)

# # Load the trained model for face recognition
# with open('trained_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# def generate_frames():
#     with picamera.PiCamera() as camera:
#         camera.resolution = (640, 480)
#         time.sleep(2)
#         stream = io.BytesIO()

#         # Create a camera array for processing frames
#         with picamera.array.PiRGBArray(camera) as stream:
#             for _ in camera.capture_continuous(stream, format="bgr", use_video_port=True):
#                 # Convert the image into a numpy array
#                 image = stream.array
#                 # Convert the image from BGR to RGB
#                 rgb_image = image[:, :, ::-1]

#                 # Find all the faces and face encodings in the current frame
#                 face_locations = face_recognition.face_locations(rgb_image)
#                 face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

#                 # Check each face found in the frame
#                 for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#                     matches = face_recognition.compare_faces(model['encodings'], face_encoding)
#                     name = "Unknown"

#                     if True in matches:
#                         first_match_index = matches.index(True)
#                         name = model['names'][first_match_index]

#                     # Draw a rectangle around the face
#                     cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
#                     # Label the face
#                     cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

#                 # Convert the result to JPEG before sending it over the network
#                 ret, buffer = cv2.imencode('.jpg', image)
#                 frame = buffer.tobytes()

#                 # Reset the stream for the next frame
#                 stream.seek(0)
#                 stream.truncate()

#                 yield (b'--frame\r\n'
#                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video')
# def video():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)










from flask import Flask, render_template, Response
import cv2
import time
import face_recognition
import pickle

app = Flask(__name__)
camera = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lbpcascade_frontalface.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Load trained model
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

def get_name():
    return "Rishav"

def generate_frames():
    while True:
        time.sleep(0.1)  # Adjust sleep time to control frame rate
        success, frame = camera.read()
        if not success:
            print("Unable to read")
            break
        else:
            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(40, 40))

            # Draw rectangles around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text_position = (x + 6, y + h + 20)
                cv2.putText(frame, get_name(), text_position, cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)







# from flask import Flask, Response
# import cv2
# import face_recognition
# import pickle
# import time

# app = Flask(__name__)
# # camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)  # GStreamer
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # Reduced resolution for better performance
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# # Load the trained model for face recognition
# with open('trained_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# def generate_frames():
#     while True:
#         time.sleep(0.2)  # Adjusted sleep time for potential performance improvement
#         success, frame = camera.read()
#         if not success:
#             print("Unable to read from camera.")
#             continue  # Continue trying to get the next frame
        
#         # Convert frame to RGB for face_recognition library
#         rgb_frame = frame[:, :, ::-1]

#         # Find all face locations and encodings in the current frame
#         face_locations = face_recognition.face_locations(rgb_frame, model='cnn')  # Using CNN model for better accuracy
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         # Process each face found in the frame
#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             matches = face_recognition.compare_faces(model['encodings'], face_encoding)
#             name = "Unknown"
            
#             if True in matches:
#                 first_match_index = matches.index(True)
#                 name = model['names'][first_match_index]

#             # Draw a rectangle around the face
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             # Draw a label with a name below the face
#             cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

#         # Convert the result to JPEG before sending it over the network
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video')
# def video():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
