import polars as pl

df = pl.read_csv("../final.csv")

result = (
    (
        df.group_by(pl.col("country_of_birth"))
        .agg(
            pl.len().alias("sample_size"),
            (pl.col("position") == "Attack").sum().alias("attackers"),
            (pl.col("position") == "Midfield").sum().alias("midfielders"),
            (pl.col("position") == "Defender").sum().alias("defenders"),
            (pl.col("position") == "Goalkeeper").sum().alias("goalkeepers"),
        )
        .sort("sample_size", descending=True)
    )
    .with_columns(
        (pl.col("attackers") / pl.col("sample_size") * 100)
        .round(2)
        .alias("attackers_ratio"),
        (pl.col("midfielders") / pl.col("sample_size") * 100)
        .round(2)
        .alias("midfielders_ratio"),
        (pl.col("defenders") / pl.col("sample_size") * 100)
        .round(2)
        .alias("defenders_ratio"),
        (pl.col("goalkeepers") / pl.col("sample_size") * 100)
        .round(2)
        .alias("goalkeepers_ratio"),
    )
    .select(
        pl.col("country_of_birth"),
        pl.col("attackers_ratio").alias("attackers_percentage"),
        pl.col("midfielders_ratio").alias("midfielders_percentage"),
        pl.col("defenders_ratio").alias("defenders_percentage"),
        pl.col("goalkeepers_ratio").alias("goalkeepers_percentage"),
    )
)

result.write_csv("position_by_country.csv")
