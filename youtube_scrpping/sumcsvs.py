import os
import pandas as pd
import glob


csv_directory = 'C:\\Users\\Administrator\\Desktop\\scrapedata'


# Use glob to match the pattern '*.csv'
csv_files = glob.glob(os.path.join(csv_directory, '*.csv'))

# Initialize an empty list to store dataframes
dfs = []

# Loop over the list of csv files
for f in csv_files:
    
    # Read the CSV file
    df = pd.read_csv(f, encoding='utf-8')
    
    # Append the dataframe to the list
    dfs.append(df)

# Concatenate all dataframes into one
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged_files.csv', index=False, encoding='utf-8')
