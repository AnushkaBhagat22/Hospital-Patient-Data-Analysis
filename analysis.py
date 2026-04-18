import pandas as pd

# Load dataset
df = pd.read_csv("patients.csv")

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# Disease frequency
print("\n===== DISEASE COUNT =====")
print(df["disease"].value_counts())

# Doctor workload
print("\n===== DOCTOR WORKLOAD =====")
print(df["doctor"].value_counts())

# Average treatment cost
avg_cost = df["treatment_cost"].mean()
print("\nAverage Treatment Cost:", avg_cost)

# Highest cost case
print("\n===== HIGHEST COST PATIENT =====")
print(df.loc[df["treatment_cost"].idxmax()])

# Age group analysis (extra insight)
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 30, 50, 100],
    labels=["Young", "Adult", "Senior"]
)

print("\n===== AGE GROUP DISTRIBUTION =====")
print(df["age_group"].value_counts())

# Save processed data (optional for Excel use)
df.to_csv("patients_processed.csv", index=False)

print("\nProcessed file saved as 'patients_processed.csv'")