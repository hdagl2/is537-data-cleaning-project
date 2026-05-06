import pandas as pd
import os

os.makedirs("outputs/tables", exist_ok=True)

licenses = pd.read_csv(
    "/Users/harshidagli/Downloads/is537-project/data/raw/business_license.csv",
    low_memory=False
)

food_clean = pd.read_csv(
    "/Users/harshidagli/Downloads/is537-project/data/cleaned/food_clean.csv"
)

# Normalize license fields for matching
food_clean["license"] = food_clean["License #"].astype(str).str.replace(".0", "", regex=False).str.strip()
licenses["license"] = licenses["LICENSE NUMBER"].astype(str).str.replace(".0", "", regex=False).str.strip()

# Optional: normalize text fields for checking consistency after matching
food_clean["DBA Name"] = food_clean["DBA Name"].astype(str).str.upper().str.strip()
food_clean["Address"] = food_clean["Address"].astype(str).str.upper().str.strip()

licenses["LEGAL NAME"] = licenses["LEGAL NAME"].astype(str).str.upper().str.strip()
licenses["DOING BUSINESS AS NAME"] = licenses["DOING BUSINESS AS NAME"].astype(str).str.upper().str.strip()
licenses["ADDRESS"] = licenses["ADDRESS"].astype(str).str.upper().str.strip()
licenses = licenses.drop_duplicates(subset=["license"])
# Match on license number first
matched = food_clean.merge(
    licenses,
    on="license",
    how="left",
    suffixes=("_inspection", "_license")
)

# A successful match means we found a business license record
match_rate = matched["LICENSE NUMBER"].notnull().mean()
print("License match rate:", match_rate)

# Save full matched file
matched.to_csv("outputs/tables/matched_data.csv", index=False)

# Save unmatched inspection records
unmatched = matched[matched["LICENSE NUMBER"].isnull()]
unmatched.to_csv("outputs/tables/unmatched_businesses.csv", index=False)

# Save a small summary file for your final report
summary = pd.DataFrame({
    "metric": [
        "total_inspection_records",
        "matched_records",
        "unmatched_records",
        "license_match_rate"
    ],
    "value": [
        len(matched),
        matched["LICENSE NUMBER"].notnull().sum(),
        matched["LICENSE NUMBER"].isnull().sum(),
        match_rate
    ]
})

summary.to_csv("outputs/tables/license_match_summary.csv", index=False)

print("Matching complete. Files saved in outputs/tables/")
print(summary)



