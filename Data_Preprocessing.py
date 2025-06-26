import pandas as pd
from datetime import datetime

# Load the data
df = pd.read_excel(r"C:\Users\divya\OneDrive\Documents\Business Intelligence and Analytics System\Project\ecopack_packaging_data_1200_plus.xlsx")

print(f"🔹 Initial rows: {len(df)}")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

# Consistent 'record_date'
df["record_date"] = pd.to_datetime(df["record_date"], errors="coerce", dayfirst=True)

# Drop missing product_id or record_date
before = len(df)
df = df.dropna(subset=["product_id", "record_date"])
print(f"🗑️ Dropped {before - len(df)} rows with missing product_id or record_date")

# Remove future dates
before = len(df)
df = df[df["record_date"] <= pd.to_datetime("today")]
print(f"🗑️ Dropped {before - len(df)} rows with future record_date")

# Clean string fields
df["supplier_id"] = df["supplier_id"].astype(str).str.strip()
df["supplier_name"] = df["supplier_name"].astype(str).str.strip().str.lower()
df["epr_compliant"] = df["epr_compliant"].astype(str).str.strip().str.upper()

# Validate supplier_id (S1–S10)
before = len(df)
valid_supplier_ids = [f"S{i}" for i in range(1, 11)]
df = df[df["supplier_id"].isin(valid_supplier_ids)]
print(f"🗑️ Dropped {before - len(df)} rows with invalid supplier_id")

# Check supplier_id/supplier_name consistency
before = len(df)
supplier_lookup = df.groupby("supplier_id")["supplier_name"].nunique()
inconsistent_suppliers = supplier_lookup[supplier_lookup > 1]
if not inconsistent_suppliers.empty:
    print("⚠️ Inconsistent supplier_name for:", inconsistent_suppliers)
    df = df[~df["supplier_id"].isin(inconsistent_suppliers.index)]
    print(f"🗑️ Dropped {before - len(df)} rows with inconsistent supplier_name for supplier_id")
else:
    print("✅ supplier_id and supplier_name are consistent")

# Validate numeric ranges
before = len(df)
df = df[(df["material_weight_kg"] >= 0) & (df["packaging_cost_usd"] >= 0)]
df = df[(df["recyclable_pct"] >= 0) & (df["recyclable_pct"] <= 100)]
print(f"🗑️ Dropped {before - len(df)} rows failing numeric value checks")

# Validate epr_compliant
before = len(df)
df = df[df["epr_compliant"].isin(["Y", "N"])]
print(f"🗑️ Dropped {before - len(df)} rows with invalid epr_compliant values")

# Impute missing numeric columns
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        print(f"ℹ️ Imputed {df[col].isnull().sum()} missing values in {col}")
        df[col].fillna(df[col].mean(), inplace=True)

# Impute missing categorical columns
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        print(f"ℹ️ Imputed {df[col].isnull().sum()} missing values in {col}")
        df[col].fillna(df[col].mode()[0], inplace=True)

# Convert to category type
categorical_cols = [
    "product_id", "product_name", "supplier_id", "supplier_name",
    "material", "material_type", "epr_compliant"
]
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype("category")

# Format record_date
df["record_date"] = df["record_date"].dt.strftime("%m/%d/%Y")

# Final summary
print("✅ Final row count:", len(df))
print("✅ Missing values per column:\n", df.isnull().sum())
print("✅ Data preview:\n", df.head())

# Save cleaned data
df.to_excel("cleaned_ecopack_data.xlsx", index=False)
