import cv2
import numpy as np
from HandDetectorModule import handDetector
import time
from sign_comparator import sign_comparator


def main():
  pTime = 0
  cTime = 0
  cap = cv2.VideoCapture(0)
  detector = handDetector(detectionCon=0.7, trackCon=0.6)

  while True:
    success, frame = cap.read()
    frame = detector.findHands(frame)
    pos_list = detector.findPosition(frame)
    angles = detector.signDetection(frame)
    if angles:
      predicted_class = sign_comparator(angles)
      cv2.putText(frame, str(predicted_class[0][1]), (10, 150), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 0), 3)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(np.round(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 3)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(5) == ord('q'):
        break


if __name__ == '__main__':
  main()