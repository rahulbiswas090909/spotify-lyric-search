import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load dataset
df = pd.read_csv("spotify_small.csv")

# Auto-detect columns
def find_column(keys):
    for col in df.columns:
        for k in keys:
            if k in col.lower():
                return col
    return None

LYRICS_COL = find_column(["lyric", "text"])
SONG_COL   = find_column(["song", "track", "title"])
ARTIST_COL = find_column(["artist"])

print("✅ Detected Columns:")
print("Lyrics :", LYRICS_COL)
print("Song   :", SONG_COL)
print("Artist :", ARTIST_COL)

df = df.dropna(subset=[LYRICS_COL, SONG_COL, ARTIST_COL])

# Preprocess text
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return " ".join(w for w in text.split() if w not in stop_words)

df["clean_lyrics"] = df[LYRICS_COL].apply(preprocess)

# TF-IDF (CORRECT for similarity)
vectorizer = TfidfVectorizer(max_features=8000, ngram_range=(1, 2))
lyric_vectors = vectorizer.fit_transform(df["clean_lyrics"])

# Search function
def search_song(snippet, top_k=3):
    snippet = preprocess(snippet)
    vec = vectorizer.transform([snippet])
    sims = cosine_similarity(vec, lyric_vectors)[0]

    idxs = sims.argsort()[-top_k:][::-1]
    return [
        {
            "Song": df.iloc[i][SONG_COL],
            "Artist": df.iloc[i][ARTIST_COL],
            "Similarity": round(float(sims[i]), 3)
        }
        for i in idxs
    ]

if __name__ == "__main__":
    q = input("Enter lyric snippet: ")
    for r in search_song(q):
        print(r)