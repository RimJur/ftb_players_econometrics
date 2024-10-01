# Hypothesis

English football players have higher value on transfermarket compared to players from:

1. Argentina.
2. Belgium.
3. Brazil.
4. (_England_).
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

## Initial dataset:

- 2809 players with missing country_of_birth
- 47 players with missing date_of_birth
- 194 players with missing position
- 0 players with missing current_club_domesting_competition_id
- 1619 players with missing market_value_in_eur

- 654 players with missing both country_of_birth + market_value_in_eur
- 92 players with missing both position + market_value_in_eur

- Overall players 32400
- Players with selected country_of_birth and after removal of players with missing data 14340

## Data cleaning

1. Remove excess columns.
2. Remove the players that does not have position + market_value_in_eur. (-92)
3. Filter to selected country_of_birth values and remove players without the country_of_birth. (-17567)
4. Fill in the missing data.
5. Calculate age for the players and delete the date_of_birth column.

Data source: [Kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores), scrapped from [https://www.transfermarkt.com/](https://www.transfermarkt.com/)
