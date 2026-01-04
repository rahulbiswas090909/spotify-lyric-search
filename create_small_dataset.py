import pandas as pd

# Load large dataset
df = pd.read_csv("spotify_data.csv")

# Auto-detect lyrics column
def find_column(keys):
    for col in df.columns:
        for k in keys:
            if k in col.lower():
                return col
    return None

lyrics_col = find_column(["lyric", "text"])
song_col = find_column(["song", "track", "title"])
artist_col = find_column(["artist"])

# Keep only needed columns
df = df[[lyrics_col, song_col, artist_col]].dropna()

# Take random sample (adjust size if needed)
small_df = df.sample(n=2000, random_state=42)

# Save new dataset
small_df.to_csv("spotify_small.csv", index=False)

print("✅ Small dataset created: spotify_small.csv")
print("Rows:", len(small_df))