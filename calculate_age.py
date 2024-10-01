import pandas as pd
from datetime import datetime
import math

df = pd.read_csv("intermediate.csv")

def calculate_age(born):
    if born:
        if isinstance(born, type("string")):
            born = datetime.fromisoformat(born)
            today = datetime.today()
            age_date = today - born
            age_days = age_date.days
            age_years = math.floor(age_days / 365.25)
            return age_years
    return


df["age"] = df["date_of_birth"].apply(calculate_age)
df.insert(2, "age", df["age"])

df = df.drop(["date_of_birth"], axis=1)

# Export
df.to_csv("final.csv", index=False)