import pandas as pd

# 1.Read Original Data
def originalData(text):
    df = pd.read_csv(text)
    print("The original data is:")
    print(df)
    return df

# 2.Show missing data
def missingData(df):
    print("\nMissing datas are in the rows:")
    print(df[df.isnull().any(axis=1)])

# 3. Delete blank rows
def cleanAndSave(df):
    df_cleaned = df.dropna()
    df_cleaned.to_csv("cleaned_customers.csv", index=False)
    print("\nThe process succeeded.")

# === Application ===
file_name = "customers.csv"
df = originalData(file_name)
missingData(df)
cleanAndSave(df)
