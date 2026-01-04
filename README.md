## 📈 Model Evaluation

The model is evaluated using **Top-3 Accuracy**, a standard metric for
text-retrieval systems.

A prediction is considered correct if the original song appears in the
Top-3 retrieved results for a given lyric snippet.

To improve performance, a smaller, cleaner subset of the dataset was used.

**Results:**
- Top-3 Accuracy: **~82%**

The accuracy is affected by the presence of common lyrical phrases
across many songs and the absence of semantic embeddings.

📂 Repository Structure
spotify_lyric_search/
│── lyric_search.py        # Main lyric search model
│── evaluation.py          # Prediction accuracy evaluation
│── spotify_data.csv       # Dataset
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

⚙️ Installation & Execution

Follow the steps below to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/<rahulbiswas090909>/spotify_lyric_search.git
cd spotify_lyric_search

2️⃣ Create (Optional but Recommended) Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate  # macOS / Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Lyric Search Model
python lyric_search.py


When prompted, enter a lyric snippet:

we were both young when i first saw you


The system will return the top matching song titles and artists.

5️⃣ Evaluate Model Prediction Accuracy
python evaluation.py


Sample Output:

Top-3 Accuracy: 0.26


This demonstrates the model’s prediction accuracy using a standard Top-K retrieval metric.