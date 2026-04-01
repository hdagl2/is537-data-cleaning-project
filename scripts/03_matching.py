import pandas as pd
food = pd.read_csv("/Users/harshidagli/Downloads/is537-project/data/raw/food_inspections.csv")
licenses = pd.read_csv("/Users/harshidagli/Downloads/is537-project/data/raw/business_license.csv")
food_clean = pd.read_csv("/Users/harshidagli/Downloads/is537-project/data/cleaned/food_clean.csv")

merged = food_clean.merge(
    licenses,
    left_on='DBA Name',
    right_on='LEGAL NAME',
    how='left'
)

match_rate = merged['License #'].notnull().mean()
print("Match rate:", match_rate)

merged.to_csv("outputs/tables/matched_data.csv", index=False)

unmatched = merged[merged['License #'].isnull()]
unmatched.to_csv("outputs/tables/unmatched_businesses.csv", index=False)



