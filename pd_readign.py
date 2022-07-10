import pandas as pd

path = r'C:\Users\graeb\OneDrive\Pulpit\sign_csv\test.csv'
df = pd.read_csv(path)
print(df.head(3))
print(df[['label']])