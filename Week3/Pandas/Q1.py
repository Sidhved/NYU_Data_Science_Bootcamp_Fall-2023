import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

res = df[['Manufacturer', 'Model', 'Type']]

print(res[: : 20])