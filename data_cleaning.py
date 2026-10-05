import pandas as pd

df = pd.read_csv("data/titanic_raw.tsv", sep="\t")

# Standardize text
for c in ["Name", "Sex", "Ticket", "Cabin", "Embarked"]:
    df[c] = df[c].apply(lambda x: x.strip() if isinstance(x, str) else x)

df["Sex"] = df["Sex"].str.lower().map({"male": "Male", "female": "Female"})
df["Embarked"] = df["Embarked"].str.upper()

# Correct numeric data types
for c in ["PassengerId", "Survived", "Pclass", "SibSp", "Parch"]:
    df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
for c in ["Age", "Fare"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Handle missing values
age_group_median = df.groupby(["Pclass", "Sex"])["Age"].transform("median")
df["Age"] = df["Age"].fillna(age_group_median)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["PassengerId"], keep="first")

df.to_csv("data/titanic_cleaned.csv", index=False)
print("Cleaned dataset saved to data/titanic_cleaned.csv")
