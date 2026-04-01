import pandas as pd

food = pd.read_csv("/Users/harshidagli/Downloads/is537-project/data/raw/food_inspections.csv")
licenses = pd.read_csv("/Users/harshidagli/Downloads/is537-project/data/raw/business_license.csv")

print(food.shape)
print(food.columns)

print(licenses.shape)
print(licenses.columns)

food_missing = food.isnull().sum().sort_values(ascending=False)
licenses_missing = licenses.isnull().sum().sort_values(ascending=False)

food_missing.to_csv("/Users/harshidagli/Downloads/is537-project/outputs/tables/food_missing.csv")
licenses_missing.to_csv("/Users/harshidagli/Downloads/is537-project/outputs/tables/licenses_missing.csv")

print("Duplicate inspection IDs:", food['Inspection ID'].duplicated().sum())

dup_combo = food.duplicated(subset=['DBA Name', 'Address', 'Inspection Date'])
print("Possible duplicates:", dup_combo.sum())

print(food['Results'].value_counts())

food['Results'].value_counts().to_csv("/Users/harshidagli/Downloads/is537-project/outputs/tables/results_distribution.csv")

food['Inspection Date'] = pd.to_datetime(food['Inspection Date'])
food['year'] = food['Inspection Date'].dt.year

food['year'].value_counts().sort_index().to_csv("/Users/harshidagli/Downloads/is537-project/outputs/tables/year_distribution.csv")

print(food['Violations'].dropna().head(10))

def is_critical(Violations):
    if pd.isna(Violations):
        return 0
    return 1 if "critical" in Violations.lower() else 0

food['critical_flag'] = food['Violations'].apply(is_critical)