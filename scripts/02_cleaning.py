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

def is_critical_violation(row):
    if pd.isna(row["Violations"]):
        return 0

    violations = str(row["Violations"]).lower()

    # Pre-2018: old Chicago inspection system used codes 1–14 as critical violations
    if pd.notnull(row["Year"]) and row["Year"] < 2018:
        codes = []
        for violation in violations.split("|"):
            first_part = violation.strip().split(".")[0]
            if first_part.isdigit():
                codes.append(int(first_part))

        return 1 if any(code <= 14 for code in codes) else 0

    # Post-2018: "Priority" is the updated serious violation category
    else:
        return 1 if "priority violation" in violations or "priority foundation" in violations else 0


food_clean["critical_flag"] = food_clean.apply(is_critical_violation, axis=1)

food_clean.to_csv("data/cleaned/food_clean.csv", index=False)

print("Cleaning complete. Clean dataset saved.")
print(food_clean[["Inspection ID", "Results", "Violations", "critical_flag"]].head())