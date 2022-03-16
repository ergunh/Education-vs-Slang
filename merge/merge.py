import pandas as pd


csv_list = []

i = 2

while i <= 52:
    csv_list.append(f'songs_{i}.csv')
    i = i + 1

print(csv_list)



df_master = pd.read_csv('master.csv')


for file in csv_list:
    df = pd.read_csv(file)
    df.to_csv('master.csv', mode = 'a', header = False, index=False)
