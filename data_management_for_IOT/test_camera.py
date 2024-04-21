import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    print("Camera is working.")
    cv2.imshow("Test Frame", frame)
    cv2.waitKey(0)  # Press any key to close the window
    cv2.destroyAllWindows()
else:
    print("Camera failed to capture frame.")
cap.release()
