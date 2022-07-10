import numpy as np
import sklearn as sk
import pandas as pd
from sklearn.neighbors import kneighbors

def sign_comparator(landmark_pos):

    path = r'C:\Users\graeb\OneDrive\Pulpit\sign_csv\test.csv'
    features = ['thumb_bend', 'index_bend', 'middle_bend', 'ring_bend', 'little_bend', 'thumb_spread', 'index_spread', 'middle_spread', 'ring_spread']
    df = pd.read_csv(path)
    



if __name__  == "__main__":
    input_sign = {'thumb_bend': 150.42910799909365, 'index_bend': 172.4868685583538, 'middle_bend': 173.7936242089177, 
              'ring_bend': 171.4754673060883, 'little_bend': 173.20322148680177, 'thumb_spread': 3.965156479373877, 
              'index_spread': 6.726115829523096, 'middle_spread': 6.2791132767029865, 'ring_spread': 7.283771842123662}
    print(sign_comparator(input_sign))
