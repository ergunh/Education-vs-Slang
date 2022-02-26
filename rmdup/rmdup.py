import pandas as pd

# MUST ENTER COMMAND INTO TERMINA/ INSTALL PANDAS:   pip install pandas


# change the csv name to your file youre using

df = pd.read_csv('master.csv')


# change "Track Name" to which ever column you want to sort
df.sort_values("Track Name", inplace = True)

 # change "Track Name" to whihc column doubles you want to remove
df_clean = df.drop_duplicates(subset=['Track Name'])


# change "master_3.csv" to what ever you want to name the new file with removed duplicates
df_clean.to_csv('master_3.csv', mode = 'a', header = False, index=False)
