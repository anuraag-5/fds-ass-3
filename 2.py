import pandas as pd
import numpy as np

# Load the same dataset again
data = {
    "Country": ["France", "Spain", "Germany", "Spain", "Germany", "France", "Spain", "France", "Germany", "France"],
    "Age": [44, 27, 30, 38, 40, 35, np.nan, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)

# Replace missing values with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("\n--- Dataset After Filling Missing Values ---")
print(df)
