import cv2
import numpy as np

cap = cv2.VideoCapture('sample.mp4')  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
        param1=50, param2=30, minRadius=10, maxRadius=100
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :1]:  
            center = (i[0], i[1])
            x, y = center
            print(f"Координаты: {x}, {y}")

            cv2.circle(frame, center, i[2], (0, 255, 0), 2)
            cv2.circle(frame, center, 2, (0, 0, 255), 3)

    cv2.imshow('TARGET', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()