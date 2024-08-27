import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data into a dataframe


# Convert data to dataframe
df = pd.read_csv('samp.csv', sep=";")

# Remove rows with NaN values
df = df.dropna()

# Split dataframe into winners and losers
winners = df[df["winner"] == "Yes"]
losers = df[df["winner"] == "No"]

# Mean, median, and standard deviation of passing rates for winners and losers
winners_mean = winners["passing_quote"].mean()
losers_mean = losers["passing_quote"].mean()
winners_median = winners["passing_quote"].median()
losers_median = losers["passing_quote"].median()
winners_std = winners["passing_quote"].std()
losers_std = losers["passing_quote"].std()

print(f"Winners - Mean: {winners_mean}, Median: {winners_median}, STD: {winners_std}")
print(f"Losers - Mean: {losers_mean}, Median: {losers_median}, STD: {losers_std}")

# Boxplot to visualize passing rates for winners and losers
plt.figure(figsize=(7, 6))
sns.boxplot(x="winner", y="passing_quote", data=df)
plt.title("Passing Rates: Winners vs Losers")
plt.show()

# Determine matches with a winner
winning_games = winners["game_id"].unique()
losing_games = losers["game_id"].unique()

# Calculate the difference in passing rates for matches with a winner and those that ended in a draw
winner_rate_differences = []
for game in winning_games:
    win_rate = winners[winners["game_id"] == game]["passing_quote"].values
    lose_rate = losers[losers["game_id"] == game]["passing_quote"].values
    winner_rate_differences.append(abs(win_rate - lose_rate))

# Visualize the distribution of these differences
plt.figure(figsize=(10, 6))
sns.histplot(winner_rate_differences, kde=True)
plt.title("Distribution of Passing Rate Differences in Matches with a Winner")
plt.xlabel("Difference in Passing Rate")
plt.show()

# Determine the number of draw matches
all_games = df["game_id"].unique()
draw_games = list(set(all_games) - set(winning_games) - set(losing_games))

# Calculate the average passing rates for draw matches
draw_rate_differences = []
for game in draw_games:
    team1_rate = df[df["game_id"] == game]["passing_quote"].values
    team2_rate = df[df["game_id"] == game]["passing_quote"].values
    draw_rate_differences.append(abs(team1_rate - team2_rate))

# Compare the mean differences between winning games and draw games
winner_diff_mean = np.mean(winner_rate_differences)
draw_diff_mean = np.mean(draw_rate_differences)

print(f"Mean Passing Rate Difference in Winning Games: {winner_diff_mean}")
print(f"Mean Passing Rate Difference in Draw Games: {draw_diff_mean}")

# Statistical test to compare the means
from scipy.stats import ttest_ind

ttest_result = ttest_ind(winner_rate_differences, draw_rate_differences)

print(f"t-test result for the difference between winning games and draw games: {ttest_result}")
