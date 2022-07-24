import cv2
import time
import mediapipe as mp
import numpy as np
import pandas as pd
import os

PATH_FOR_CSV = r'C:\Users\graeb\OneDrive\Pulpit\sign_csv'

class handDetector():
    def __init__(self, mode=False, maxHands=2,modelC=1, detectionCon=0.7, trackCon=0.6):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelC, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        if self.result.multi_hand_landmarks:
            for handLand in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLand, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, draw=True):
        PosList = []
        x_lst = []
        y_lst = []
        self.result = self.hands.process(img)
        # img.flags.writeable = True
        if self.result.multi_hand_landmarks:
            for hands in self.result.multi_hand_landmarks:
                for id, lm in enumerate(hands.landmark):
                    h, w, c = img.shape
                    d = img.shape[0]
                    cx, cy, cz = int(lm.x * w), int(lm.y * h), float(lm.z * d)
                    x_lst.append(cx)
                    y_lst.append(cy)
                    PosList.append([id, cx, cy, cz])
                    
                if draw:
                    ld_corner = (min(x_lst)-10, min(y_lst)-10)
                    rt_corner = (max(x_lst)+10, max(y_lst)+10)
                    cv2.rectangle(img, ld_corner, rt_corner, (0,255,0), 4)
                    
        return PosList
    
    def signDetection(self, image, draw=False):
        joints = {'thumb_bend': [4,3,2], 'index_bend': [8,7,5], 'middle_bend': [12,11,9], 'ring_bend': [16,15,13], 'little_bend': [20,19,17], 
                  'thumb_spread': [1,6,5], 'index_spread': [6,0,10], 'middle_spread': [10,0,14], 'ring_spread': [14,0,18]}
        angles = {}
        if self.result.multi_hand_landmarks:
            for hand in self.result.multi_hand_landmarks:
                for joint in joints:
                    a = np.array([hand.landmark[joints[joint][0]].x, hand.landmark[joints[joint][0]].y]) # First coord
                    b = np.array([hand.landmark[joints[joint][1]].x, hand.landmark[joints[joint][1]].y]) # Second coord
                    c = np.array([hand.landmark[joints[joint][2]].x, hand.landmark[joints[joint][2]].y]) # Third coord
                    
                    radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
                    angle = np.abs(radians*180.0/np.pi)
                    
                    if angle > 180.0:
                        angle = 360-angle
                
                    angles[joint] = angle
                    angle_str = str(round(angle, 2))
                    text = (f'{angle_str} // {joint}')
                    if draw:   
                        cv2.putText(image, text, tuple(np.multiply(b, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (55, 55, 255), 2, cv2.LINE_AA)  
                return angles
    # def Label(self):
    #     label = input("Give label = ")
    #     return label     
    
    def SavingCSV(self, label, angles, path):
        df = pd.DataFrame(index=label,data=angles)
        df.to_csv(path, mode='a', header=False)
        time.sleep(0.2)   
        print(f'saved  ')
 

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        joint_list = [[1,0,5],[8,7,5]]
        success, frame = cap.read()
        frame = detector.findHands(frame)
        pos_list = detector.findPosition(frame)
        print(pos_list)
        # angles = detector.signDetection(frame)
        # print(angles)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # cv2.putText(frame, str(np.round(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 3)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(5) == ord('q'):
            break


if __name__ == "__main__":
    main()