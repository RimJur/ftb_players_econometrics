import polars as pl

df = pl.read_csv("../final.csv", has_header=True)

result = (
    df.group_by(pl.col("country_of_birth"))
    .agg(pl.len().alias("sample_size"), pl.col("age").mean().round(2).alias("avg_age"))
    .sort("sample_size", descending=True)
    .select(pl.col("country_of_birth"), pl.col("avg_age"))
)

result.write_csv("age_by_country.csv")
