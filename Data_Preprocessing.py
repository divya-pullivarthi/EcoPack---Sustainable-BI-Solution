import pandas as pd
from datetime import datetime

# Load the data
df = pd.read_excel(r"C:\Users\divya\OneDrive\Documents\Business Intelligence and Analytics System\Project\ecopack_packaging_data_1200_plus.xlsx")

# 1. Clean column names: lowercase + replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

# 2. Convert 'record_date' to datetime (handle mixed formats)
def parse_mixed_date(date_str):
    try:
        return pd.to_datetime(date_str, format="%d-%m-%Y")
    except:
        try:
            return pd.to_datetime(date_str, format="%m/%d/%Y")
        except:
            return pd.NaT

df["record_date"] = df["record_date"].apply(parse_mixed_date)

# 3. Format record_date as MM/DD/YYYY string
df["record_date"] = df["record_date"].dt.strftime("%m/%d/%Y")

# 4. Drop rows with missing critical fields
df = df.dropna(subset=["product_id", "record_date"])

# 5. Impute missing numeric columns using mean
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)

# 6. Impute missing categorical columns using mode
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)

# 7. Convert selected columns to 'category' dtype
categorical_cols = [
    "product_id", "product_name", "supplier_id", "supplier_name",
    "material", "material_type", "epr_compliant"
]
for col in categorical_cols:
    df[col] = df[col].astype("category")

# 8. Final check and preview
print("Final missing values:\n", df.isnull().sum())
print(df.info())
print(df.head())

# 9. Save the cleaned dataset
df.to_excel("cleaned_ecopack_data.xlsx", index=False)
