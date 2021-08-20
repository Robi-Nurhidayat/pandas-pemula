import pandas as pd

df = pd.read_csv('./data/pokemon_data.csv')

print(df.head(3))

# reading data in pandas



# read headers
print('read header\n')

print(df.columns)

# read each column
print('read each column\n')
print(df[['Name','HP','Sp. Atk']].head(3))

# read each row
print('read each row')
print(df.head(2))

# user iloc

print(df.iloc[1:3])

# read a specific location (R,C)
print('read a specific location')
print(df.iloc[1,2])