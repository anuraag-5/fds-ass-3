import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np

# Step 1: Create dataset
data = {
    "Country": ["France", "Spain", "Germany", "Spain", "Germany", "France", "Spain", "France", "Germany", "France"],
    "Age": [44, 27, 30, 38, 40, 35, np.nan, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, np.nan, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

# 1a) Describe dataset
print("\n--- Dataset Description ---")
print(df.describe(include="all"))

# 1b) Shape
print("\n--- Shape of Dataset ---")
print(df.shape)

# 1c) First 3 rows
print("\n--- First 3 Rows ---")
print(df.head(3))

# 2) Handling Missing Values: replace with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# 3a) OneHot Encoding on Country
onehot_encoder = OneHotEncoder()
country_encoded = onehot_encoder.fit_transform(df[['Country']]).toarray()
country_encoded_df = pd.DataFrame(country_encoded, columns=onehot_encoder.get_feature_names_out(['Country']))

# 3b) Label Encoding on Purchased
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

# Combine processed data
final_df = pd.concat([country_encoded_df, df[['Age', 'Salary', 'Purchased']]], axis=1)

print("\n--- Processed Dataset ---")
print(final_df)
