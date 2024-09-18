import pandas as pd

# Load the dataset
df = pd.read_csv("players.csv")

# Define the categories you want to keep
selected_country_of_birth = [
    "England",
    "Argentine",
    "Spain",
    "Brazil",
    "Germany",
    "France",
]

# Filter the DataFrame
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
        "current_club_domestic_competition_id",
        "current_club_name",
    ],
    axis=1,
)

# Save to CSV with specific formatting (handle quotes and delimiters)
filtered_df.to_csv("filtered_dataset.csv", index=False)
