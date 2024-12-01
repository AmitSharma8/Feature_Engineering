import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warings 
warnings.filterwarnings("ignore")

# Download a file from Github
url = "https://raw.githubusercontent.com/AmitSharma8/Feature_Engineering/loan.csv"
response = requests.get(url)
output_path = "loan"        # local file path
with open(output_path, "wb") as file:  # Write the content to a local file
    file.write(response.content)
    
data = pd.read_csv('loan')
