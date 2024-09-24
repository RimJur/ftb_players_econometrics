import pandas as pd
from datetime import datetime
import math

df = pd.read_csv("starting.csv")

# Keeping only these countries
selected_country_of_birth = [
    "Argentina",
    "Belgium",
    "Brazil",
    "England",
    "France",
    "Germany",
    "Italy",
    "Netherlands",
    "Portugal",
    "Spain",
]

# Filter the countries
filtered_df = df[df["country_of_birth"].isin(selected_country_of_birth)]


# Drop unwanted columns
filtered_df = filtered_df.drop(
    [
        "player_id",
        "first_name",
        "last_name",
        "current_club_id",
        "player_code",
        "city_of_birth",
        "country_of_citizenship",
        "sub_position",
        "agent_name",
        "image_url",
        "url",
        "foot",
        "height_in_cm",
        "current_club_name",
        "highest_market_value_in_eur",
        "contract_expiration_date",
        "last_season",
    ],
    axis=1,
)


# Remove players without market value and date of birth
filtered_df.dropna(subset="date_of_birth", inplace=True)
filtered_df.dropna(subset="market_value_in_eur", inplace=True)

# Transform date of birth to age
# df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])
# current_date = pd.to_datetime(date.today().__str__())


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


df["age"] = df["date_of_birth"].apply(lambda x: calculate_age(x))
filtered_df.insert(2, "age", df["age"])

filtered_df = filtered_df.drop(["date_of_birth"], axis=1)

# Export
filtered_df.to_excel("filtered.xlsx", index=False)
filtered_df.to_csv("filtered.csv", index=False)
