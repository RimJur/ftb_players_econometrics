# Hypothesis

English football players have higher value on transfermarket compared to players from:

1. Argentina.
2. Belgium.
3. Brazil.
4. (*England*).
5. France.
6. Germany.
7. Italy.
8. Netherlands.
9. Portugal.
10. Spain.

## Variables:

- Dependent:
  - market_value_in_eur
- Independent:
  - country_of_birth
  - position
  - date of birth (age)
  - current_club_domestic_competition_id (league)

## Data cleaning

1. Removed the players without market value determined. There was small amount of them, so there should not be a significant effect to the end values.
2. Removed the players without date of birth value.
3. Calculate age for the players.
4. Delete the date_of_birth column.

Data source: [Kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores), scrapped from [https://www.transfermarkt.com/](https://www.transfermarkt.com/)
