# The data used are in these links
resource_urls= [
    "https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/main/practicals/day4/practical5/data/flu_data.csv",
    "https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/main/practicals/day4/practical5/data/incidence.csv",
     ]

import subprocess
for url in resource_urls:
   subprocess.run(["curl", "-O", url], check=True)
