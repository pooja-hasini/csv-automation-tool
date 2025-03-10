import pandas as pd
# Load CSV
df = pd.read_csv("data.csv")
# Calculate average marks per student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
# Find toppers
topper = df.loc[df["Average"].idxmax()]
print("Top Scorer:", topper["Name"])
print("Average Marks:\n", df[["Name", "Average"]])
# Subject-wise toppers
for subject in ["Math", "Science", "English"]:
    top = df.loc[df[subject].idxmax()]
    print(f"Topper in {subject}: {top['Name']} ({top[subject]} marks)")
