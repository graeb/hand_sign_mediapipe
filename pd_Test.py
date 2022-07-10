import pandas as pd
import os

def concString(*args):
    mega_string = ","
    for arg in args:
        mega_string += arg+","
    return mega_string[0:-1]

PATH_FOR_CSV = os.path.join(os.getcwd(), 'test.csv')
features = {'thumb_bend': 161.1, 'index_bend': 115.98887313998024, 'middle_bend': 158.21672435637097,
              'ring_bend': 161.2, 'little_bend': 168.51142627311995, 'thumb_spread': 23.392122798870073, 
              'index_spread': 12.3, 'middle_spread': 9.788689217772957, 'ring_spread': 8.393631032781194}
signs = {'sign': 1.1} #['a','b','c','d','e','f']
signs.update(features)
df = pd.DataFrame(data = signs, index=range(len(signs)//10))
print(concString(*df.columns))
with open(PATH_FOR_CSV, 'r') as read:
    column_names_from_file = read.readline()

if column_names_from_file[0:-1] == concString(*df.columns):
    print(column_names_from_file)
    print("it works!")
    print(features.keys())
else:
    print("no stonks")
    print(column_names_from_file)
    print(concString(*df.columns))
    print(f"Types {type(column_names_from_file[0:-1])} compared to {type(concString(*df.columns))}")
    print(f"Lengths {len(column_names_from_file[0:-1])} compared to {len(concString(*df.columns))}")
    print(features.keys())
