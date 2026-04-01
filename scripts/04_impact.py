import pandas as pd
import os

os.makedirs("outputs/tables", exist_ok=True)

food = pd.read_csv(
    "/Users/harshidagli/Downloads/is537-project/data/raw/food_inspections.csv"
)

food_clean = pd.read_csv(
    "/Users/harshidagli/Downloads/is537-project/data/cleaned/food_clean.csv"
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

# recreate for raw dataset so before/after are comparable
food["critical_flag"] = food["Violations"].apply(is_critical)

def compute_metrics(df):
    total = len(df)
    pass_rate = (df["Results"] == "Pass").mean() if "Pass" in df["Results"].astype(str).unique() else (df["Results"].astype(str).str.upper() == "PASS").mean()
    fail_rate = (df["Results"] == "Fail").mean() if "Fail" in df["Results"].astype(str).unique() else (df["Results"].astype(str).str.upper() == "FAIL").mean()
    critical_rate = df["critical_flag"].mean()

    return pd.Series({
        "total_records": total,
        "pass_rate": pass_rate,
        "fail_rate": fail_rate,
        "critical_violation_rate": critical_rate
    })

before = compute_metrics(food)
after = compute_metrics(food_clean)

comparison = pd.concat([before, after], axis=1)
comparison.columns = ["before_cleaning", "after_cleaning"]

comparison.to_csv("outputs/tables/before_after_comparison.csv")

print(comparison)
print("Impact analysis complete.")

