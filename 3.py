import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Dataset (with missing values already filled)
data = {
    "Country": ["France", "Spain", "Germany", "Spain", "Germany", "France", "Spain", "France", "Germany", "France"],
    "Age": [44, 27, 30, 38, 40, 35, 39.888888888888886, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, 63777.77777777778, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)

# OneHot Encoding for Country
onehot_encoder = OneHotEncoder(handle_unknown='ignore')
country_encoded = onehot_encoder.fit_transform(df[['Country']]).toarray()
country_df = pd.DataFrame(country_encoded, columns=onehot_encoder.get_feature_names_out(['Country']))

# Label Encoding for Purchased
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

print("\n--- Label Encoded ---")
print(df)

print("\n--- One-Hot Encoded ---")
print(country_encoded)

# Join the encoded columns with the original DataFrame
final_df = df.join(country_df)
print("\n--- After Joining ---")
print(final_df)
