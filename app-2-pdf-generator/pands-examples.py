# run this Python code snippet once to create the file
import pandas as pd
data = {'Index': [1, 2, 3, 4, 5],
        'Topic': ['Variables', 'Lists', 'Functions', 'While-loop', 'Methods'],
        'Difficulty': [2, 3, 3, 2, 3]}
df = pd.DataFrame(data)
df.to_csv('test.csv', index=False, header=False) # make header=True to show Headings

# Reading the CSV into a DataFrame

import pandas as pd

############################################################
# Read the CSV. Since your file has no header row,
# we need to tell pandas to assign default column names (0, 1, 2).
df = pd.read_csv('test.csv', header=None)

# Let's rename the columns to be meaningful
df.columns = ['ID', 'Topic Name', 'Rating']

print("--- Initial DataFrame (df) ---")
print(df)

############################################################

## Fetching a Single Column (Series)

# Select the 'Topic Name' column
topics = df['Topic Name']

print("\n--- Topic Names (Series) ---")
print(topics)

############################################################
#Fetching Multiple Columns
# Select both the 'Topic Name' and 'Rating' columns
topics_and_ratings = df[['Topic Name', 'Rating']]

print("\n--- Topics and Ratings (DataFrame) ---")
print(topics_and_ratings)

############################################################
# perform calculations and add new, derived columns to your DataFrame.

# Add a new column based on a calculation involving existing columns
df['Weighted Score'] = df['Rating'] * df['ID']

print("\n--- DataFrame with New Column ---")
print(df)

############################################################
# For Loop on DataFrame

print("--- For Loop using iterrows() ---")
for index, row in df.iterrows():
    # We can access column values using row['Column Name']
    if row['Rating'] > 2:
        print(f"Topic ID {row['ID']} ({row['Topic Name']}) is a high-difficulty topic.")
    elif row['Rating'] <= 2:
        print(f"Topic ID {row['ID']} ({row['Topic Name']}) is a Easy topic.")

############################################################
# Iterating Over a Single Column (Series)
#If you only need the values from one column, you can loop directly over the Pandas Series object.

print("\n--- For Loop over the 'Topic Name' Column ---")
for topic in df['Topic Name']:
    # The variable 'topic' holds the string value directly
    print(f"Processing topic: {topic}")