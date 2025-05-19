# The data used are in these links
resource_urls= [
    "https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/main/practicals/day4/practical5/data/flu_data.csv",
    "https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/main/practicals/day4/practical5/data/incidence.csv",
     ]

import subprocess
for url in resource_urls:
   subprocess.run(["curl", "-O", url], check=True)

import pandas as pd
df = pd.read_csv('flu_data.csv')

# Convert the dates to datetime format
df.Date = pd.to_datetime(df.date)

# Use date as index
df = df.set_index("date")
