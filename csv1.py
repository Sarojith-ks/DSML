import pandas as pd
file=pd.read_csv('data.csv')
df=pd.DataFrame(file)

print(df.to_string())
