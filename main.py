import pandas as pd
# Load the cleaned dataset
cleaned_file_path = "kidney_disease_cleaned.csv"
df_cleaned = pd.read_csv(cleaned_file_path)

# Check for missing values
missing_values = df_cleaned.isnull().sum()

# Check data types
data_types = df_cleaned.dtypes

# Display results
missing_values, data_types
