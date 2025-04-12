import pandas as pd

df = pd.read_csv('matches.csv')
print(df.head())

total_matches = df.shape[0]
print("\nTotal Matches Played:", total_matches)

total_teams = pd.concat([df['team1'], df['team2']]).nunique()
print("Total Teams Participated:", total_teams)

total_seasons = df['season'].nunique()
print("Total Seasons:", total_seasons)

most_wins = df['winner'].value_counts()
print("\nMost Wins by Team:\n", most_wins)

season_matches = df['season'].value_counts().sort_index()
print("\nMatches Per Season:\n", season_matches)

toss_wins = df['toss_winner'].value_counts()
print("\nToss Wins by Team:\n", toss_wins)

top_venues = df['venue'].value_counts().head(10)
print("\nTop 10 Match Venues:\n", top_venues)

summary = {
    "Most Wins": most_wins.index[0],
    "Most Toss Wins": toss_wins.index[0],
    "Total Seasons": total_seasons,
    "Most Common Venue": top_venues.index[0],
    "Total Matches": total_matches,
    "Total Teams": total_teams
}

summary_df = pd.DataFrame([summary])
summary_df.to_csv('ipl_summary.csv', index=False)

print("\nSummary saved as 'ipl_summary.csv'")
