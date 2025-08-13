import pandas as pd
import numpy as np

# Step 1: Create dataset (you can also load from CSV)
data = {
    "Country": ["France", "Spain", "Germany", "Spain", "Germany", "France", "Spain", "France", "Germany", "France"],
    "Age": [44, 27, 30, 38, 40, 35, np.nan, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

# a) Describe dataset
print("\n--- Dataset Description ---")
print(df.describe(include="all"))

# b) Shape
print("\n--- Shape of Dataset ---")
print(df.shape)

# c) First 3 rows
print("\n--- First 3 Rows ---")
print(df.head(3))
