import numpy as np


def sign_comparator(landmark_pos):
    a_sign = {'thumb_bend': 150.1345282825247, 'index_bend': 49.67054162947563, 'middle_bend': 51.75909429349639, 
              'ring_bend': 60.45780491932875, 'little_bend': 58.64734897306926, 'thumb_spread': 0.08727043481073098, 
              'index_spread': 9.76559738504291, 'middle_spread': 9.81213326338223, 'ring_spread': 10.368177681556897}
    b_sign = {'thumb_bend': 166.42910799909365, 'index_bend': 172.4868685583538, 'middle_bend': 173.7936242089177, 
              'ring_bend': 171.4754673060883, 'little_bend': 173.20322148680177, 'thumb_spread': 3.965156479373877, 
              'index_spread': 6.726115829523096, 'middle_spread': 6.2791132767029865, 'ring_spread': 7.283771842123662}
    c_sign = {'thumb_bend': 176.42871041735094, 'index_bend': 143.09118965913237, 'middle_bend': 132.71312153436693, 
              'ring_bend': 140.6916904467268, 'little_bend': 144.64851797610226, 'thumb_spread': 9.721044445580635, 
              'index_spread': 7.807961967557718, 'middle_spread': 6.157150286303788, 'ring_spread': 6.8206984526476315}
    d_sign = {'thumb_bend': 173.04237159727563, 'index_bend': 176.35414491748634, 'middle_bend': 85.8925258079719, 
              'ring_bend': 40.83429538573027, 'little_bend': 44.10186937663145, 'thumb_spread': 3.7379411923106587, 
              'index_spread': 9.106320139477358, 'middle_spread': 7.6915352107939015, 'ring_spread': 9.290805216716912}
    e_sign = {'thumb_bend': 174.38489426390046, 'index_bend': 22.107654857131124, 'middle_bend': 18.08784651321923, 
              'ring_bend': 26.60922843041949, 'little_bend': 38.29260717471376, 'thumb_spread': 2.577266645006613, 
              'index_spread': 10.508635489097001, 'middle_spread': 9.332876908220305, 'ring_spread': 10.428145145301217}
    f_sign = {'thumb_bend': 161.80676290566825, 'index_bend': 115.98887313998024, 'middle_bend': 158.21672435637097,
              'ring_bend': 161.4905515879745, 'little_bend': 168.51142627311995, 'thumb_spread': 23.392122798870073, 
              'index_spread': 12.347788938756052, 'middle_spread': 9.788689217772957, 'ring_spread': 8.393631032781194}
    

    sign_lst = [(a_sign, 'a'), (b_sign, 'b'), (c_sign, 'c'), (d_sign, 'd'), (e_sign, 'e'), (f_sign, 'f')]
    sol = []
    for signs, names in sign_lst:
        sign_val_lst = np.array(list(signs.values()))        
        lm_val_lst = np.array(list(landmark_pos.values()))
        sol_lst = sign_val_lst - lm_val_lst
        sol_lst = abs(sol_lst)
        sol_lst = np.sum(sol_lst)
        sol_lst_named = [sol_lst, names]
        sol.append(sol_lst_named) 
    sol.sort()
    return sol

if __name__  == "__main__":
    input_sign = {'thumb_bend': 150.42910799909365, 'index_bend': 172.4868685583538, 'middle_bend': 173.7936242089177, 
              'ring_bend': 171.4754673060883, 'little_bend': 173.20322148680177, 'thumb_spread': 3.965156479373877, 
              'index_spread': 6.726115829523096, 'middle_spread': 6.2791132767029865, 'ring_spread': 7.283771842123662}
    print(sign_comparator(input_sign))
