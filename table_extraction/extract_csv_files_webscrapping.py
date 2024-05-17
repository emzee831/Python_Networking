import pandas as pd 

df_premier23 = pd.read_csv('https://football-data.co.uk/mmz4281/2324/E0.csv')


print(df_premier23)

# renaming columns
df_premier23.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)

print(df_premier23)
