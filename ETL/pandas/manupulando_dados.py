import pandas as pd
url = 'https://raw.githubusercontent.com/mesfind/datasets/master/banking.csv'
df1 = pd.read_csv(url, delimiter=";")
print(df1.head())