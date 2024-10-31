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
df = df[df["country_of_birth"].isin(selected_country_of_birth)]

# Drop unwanted columns
df = df.drop(
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

# Remove players without position and market value
df.dropna(subset=["position", "market_value_in_eur"], inplace=True, how='any')

# Export
df.to_csv("intermediate.csv", index=False)
