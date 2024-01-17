# %%
# this worked but took sometime for 1 file
import pandas as pd
import re
# from itertools import islice

def load_data(file_path):
    current_movie_id = None
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            
            if ':' in line:
                current_movie_id = int(line.strip()[:-1])
            else:
                customer_id, rating, date = line.strip().split(',')
                data.append([current_movie_id, int(customer_id), int(rating), date])
        
    # Create a DataFrame
    columns = ['MovieID', 'CustomerID', 'Rating', 'Date']
    df = pd.DataFrame(data, columns=columns)

    # Parse 'Date' column as datetime
    df['Date'] = pd.to_datetime(df['Date'])

    return df

file_path = 'data/combined_data_1.txt'
df = load_data(file_path)

print(df.head())

# %%
# this worked but took sometime for 9 minutes so wasnt sure how much more
import pandas as pd
import re

def load_data(file_paths):
    all_data = []

    for file_path in file_paths:
        current_movie_id = None
        data = []

        with open(file_path, 'r') as file:
            for line in file:
                if ':' in line:
                    current_movie_id = int(line.strip()[:-1])
                else:
                    customer_id, rating, date = line.strip().split(',')
                    data.append([current_movie_id, int(customer_id), int(rating), date])

        all_data.append(pd.DataFrame(data, columns=['MovieID', 'CustomerID', 'Rating', 'Date']))

    # Concatenate all DataFrames into one
    final_data = pd.concat(all_data, ignore_index=True)

    # Parse 'Date' column as datetime
    final_data['Date'] = pd.to_datetime(final_data['Date'])

    return final_data

file_paths = ['data/combined_data_1.txt', 'data/combined_data_2.txt', 'data/combined_data_3.txt', 'data/combined_data_4.txt']
df = load_data(file_paths)

print(df.head())

# %%
# 2 minutes per file
import re
import csv
import pandas as pd
import os

def process_data(input_files, output_file):
    pattern_movie_id = r'^(\d+):\s*$'
    pattern_data = r'^(\d+),\s*([\d.]+),\s*(\d{4}-\d{2}-\d{2})$'

    with open(output_file, 'w', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(['CustId', 'Rating', 'Date', 'MovieId'])
    
        for file in input_files:

            data = []
            
            movie_id = None
            print(file)

            with open(file, 'r') as f:
                for line in f:
                    line = line.strip()

                    match_movie_id = re.match(pattern_movie_id, line)
                    match_data = re.match(pattern_data, line)
                    
                    
                    if match_movie_id:
                        movie_id = match_movie_id.group(1)
                    elif match_data:
                        cust_id = match_data.group(1)
                        rating = match_data.group(2)
                        date = match_data.group(3)
                        data.append([cust_id, rating, date, movie_id])
                    else:
                        raise Exception('Found neither MovieId nor Data')

            writer.writerows(data)


    print("CSV file created successfully.")

# Example usage
input_files = ['data/combined_data_1.txt', 'data/combined_data_2.txt', 'data/combined_data_3.txt', 'data/combined_data_4.txt']

output_file = 'Netflix_User_Ratings.csv'

process_data(input_files, output_file)

# %%
# columns_now = ['CustId', 'Rating', 'Date', 'MovieId']
df = pd.read_csv(output_file)
print(df.shape) # (100480507, 4)

# %%
unique_users = len(df['CustId'].unique())
unique_movies = len(df['MovieId'].unique())
print(unique_users, unique_movies) # 480189 17770

# %%
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Rating')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# %%
import pandas as pd

df_movie_titles = pd.read_csv('data/movie_titles.csv', names=['Movie_Id', 'Release_Year', 'Title1', 'Title2','Title3','Title4'], encoding='ISO-8859-1', delimiter=',')
df_movie_titles['Movie_Title'] = df_movie_titles['Title1'].fillna('') + ' ' + df_movie_titles['Title2'].fillna('') + ' ' + df_movie_titles['Title3'].fillna('') + ' ' + df_movie_titles['Title4'].fillna('')
df_movie_titles['Release_Year'] = df_movie_titles['Release_Year'].astype('Int64')
print(df_movie_titles.head())
df_movie_titles.to_csv("movie_titles_recreated.csv", index=False)

#%%
# df_movie_titles.head()
# print(df_movie_titles['Movie_Id'])
print()
# print(df_movie_titles['Release_Year'])
print()
# print(df_movie_titles['Title1'])

# %%
print(df_movie_titles.iloc[939:954].to_string(index=False))

# %%
