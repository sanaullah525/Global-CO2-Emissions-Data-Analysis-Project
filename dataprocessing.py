# Importing all the necessary libraries for data processing.

import pandas as pd
import numpy as np
import openpyxl


df= pd.read_excel(r"C:\Users\dell\Desktop\CO2-dataset.xlsx")
print(df.head())

# Displaying the structure and basic info about data.
print(df.info())