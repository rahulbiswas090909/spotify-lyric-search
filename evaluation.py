from lyric_search import df, search_song
import random

def evaluate_top_k(k=3, samples=100):
    correct = 0
    tested = 0

    for _ in range(samples):
        row = df.sample(1).iloc[0]
        words = row["clean_lyrics"].split()
        if len(words) < 8:
            continue

        snippet = " ".join(words[:8])
        results = search_song(snippet, top_k=k)
        predicted = [r["Song"] for r in results]

        if row[[c for c in row.index if c.lower() in ["song", "track", "title"]][0]] in predicted:
            correct += 1
        tested += 1

    return correct / tested if tested else 0

if __name__ == "__main__":
    acc = evaluate_top_k(k=3, samples=100)
    print(f"✅ Top-3 Accuracy: {acc:.2f}")