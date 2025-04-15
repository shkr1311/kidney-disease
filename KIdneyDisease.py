import pandas as pd

# Load dataset
file_path = "kidney_disease.csv"
df = pd.read_csv(file_path)

# Drop irrelevant column
if 'id' in df.columns:
    df.drop(columns=['id'], inplace=True)

# Convert numerical columns stored as objects
for col in ['pcv', 'wc', 'rc']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Standardize categorical values
def standardize_text(value):
    if isinstance(value, str):
        return value.strip().lower()
    return value

cat_cols = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'classification']
df[cat_cols] = df[cat_cols].applymap(standardize_text)

# Handle missing values
for col in df.columns:
    if df[col].dtype == 'object':  # Categorical
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:  # Numerical  
        df[col].fillna(df[col].median(), inplace=True)

# Save cleaned dataset
cleaned_file_path = "kidney_disease_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to: {cleaned_file_path}")
