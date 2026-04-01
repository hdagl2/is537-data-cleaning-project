import pandas as pd
import os

os.makedirs("data/cleaned", exist_ok=True)
os.makedirs("outputs/tables", exist_ok=True)

food = pd.read_csv(
    "/Users/harshidagli/Downloads/is537-project/data/raw/food_inspections.csv"
)

licenses = pd.read_csv(
    "/Users/harshidagli/Downloads/is537-project/data/raw/business_license.csv",
    low_memory=False
)

food["DBA Name"] = food["DBA Name"].str.upper().str.strip()
food["Address"] = food["Address"].str.upper().str.strip()

licenses["LEGAL NAME"] = licenses["LEGAL NAME"].str.upper().str.strip()
licenses["ADDRESS"] = licenses["ADDRESS"].str.upper().str.strip()

food_clean = food.drop_duplicates(subset=["Inspection ID"]).copy()

food_clean["Inspection Date"] = pd.to_datetime(food_clean["Inspection Date"], errors="coerce")
food_clean["Year"] = food_clean["Inspection Date"].dt.year

food_clean["period"] = food_clean["Year"].apply(
    lambda x: "pre_2018" if pd.notnull(x) and x < 2018 else "post_2018"
)

def is_critical(violations):
    if pd.isna(violations):
        return 0
    v = str(violations).lower()
    keywords = [
        "critical",
        "priority",
        "priority foundation"
    ]
    return 1 if any(k in v for k in keywords) else 0

food_clean["critical_flag"] = food_clean["Violations"].apply(is_critical)

food_clean.to_csv("data/cleaned/food_clean.csv", index=False)

print("Cleaning complete. Clean dataset saved.")
print(food_clean[["Inspection ID", "Results", "Violations", "critical_flag"]].head())