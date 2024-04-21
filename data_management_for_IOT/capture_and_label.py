import cv2
import os  # Add this line to import the os module

# Initialize the camera
cam = cv2.VideoCapture(0)   # 0 is the default camera

def capture_image():
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        return
    img_name = "opencv_frame_{}.png".format(len([l for l in os.listdir('.') if 'opencv_frame' in l]))
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    cam.release()

if __name__ == '__main__':
    capture_image()

