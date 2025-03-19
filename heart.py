import pandas as pd

# Load dataset
heart_file_path = "heart_disease_uci.csv"
df = pd.read_csv(heart_file_path)

# Drop irrelevant column
if 'id' in df.columns:
    df.drop(columns=['id'], inplace=True)

# Convert categorical columns to standardized text
def standardize_text(value):
    if isinstance(value, str):
        return value.strip().lower()
    return value

cat_cols = ['sex', 'cp', 'restecg', 'exang', 'slope', 'thal']
df[cat_cols] = df[cat_cols].apply(lambda x: x.map(standardize_text))

# Convert categorical boolean-like columns
bool_cols = ['fbs', 'exang']
df[bool_cols] = df[bool_cols].astype(str).apply(lambda x: x.map({'true': 1, 'false': 0}))

# Convert `ca` to integer (handling NaN as -1)
df['ca'] = df['ca'].fillna(-1).astype(int)

# Handle missing values
for col in df.columns:
    if df[col].dtype == 'object':  # Categorical
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
    else:  # Numerical
        df[col] = df[col].fillna(df[col].median())

# Convert categorical columns to category type
df[cat_cols] = df[cat_cols].astype('category')

# Save cleaned dataset
cleaned_file_path = "heart_disease_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to: {cleaned_file_path}")
