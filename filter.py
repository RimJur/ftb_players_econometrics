import pandas as pd

df = pd.read_csv("players.csv")

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

# TODO: transform birth date to age

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

# Remove players without market value
filtered_df.dropna(subset="market_value_in_eur", inplace=True)

# Export
filtered_df.to_excel("filtered_dataset.xlsx", index=False)
filtered_df.to_csv("filtered_dataset.csv", index=False)
