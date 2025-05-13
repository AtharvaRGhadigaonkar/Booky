# 📚 Booky – The Smart Book Recommendation System

Welcome to **Booky**, your all-in-one intelligent book recommendation engine! Whether you're a casual reader looking for trending titles or a bibliophile searching for content that aligns with your unique taste, Booky has you covered.

---

## 🌟 Features

Booky leverages four powerful recommendation techniques:

1. **Popularity-Based Recommendation**  
   Recommends books that are widely liked, based on rating count or average score.

2. **Content-Based Filtering**  
   Suggests books similar in genre, author, or content description using NLP techniques.

3. **Collaborative Filtering**  
   Utilizes user-book interactions and similarities between users to recommend what others with similar tastes liked.

4. **Hybrid Model**  
   Combines content and collaborative filtering to deliver the most personalized and accurate recommendations.

---

## 🧠 Tech Stack

| Layer        | Technology Used                        |
|--------------|----------------------------------------|
| Language     | Python                                 |
| Libraries    | Pandas, NumPy, Scikit-learn, Flask     |
| Web Framework| Flask (Backend)                        |
| Frontend     | HTML, CSS,                             |
| Data         | Book metadata + user ratings dataset   |
| Deployment   | (Yet to be decided) Render / Heroku    |

---

## 🧩 Use Cases

- **For Readers**: Discover books tailored to your interests and reading history.
- **For Libraries**: Offer personalized recommendations to patrons.
- **For Book Retailers**: Boost user engagement and sales through smart suggestions.
- **For Researchers**: Explore hybrid recommender system design.

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/AtharvaRGhadigaonkar/Booky.git
cd booky
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser to explore Booky!

---

## 🛠️ Folder Structure

```
📁 BOOKY
├── 📁 __pycache__
│   └── 📄 app.cpython-312.pyc
├── 📁 .ipynb_checkpoints
├── 📁 Data
│   ├── 📄 Books.csv
│   ├── 📄 Ratings.csv
│   └── 📄 Users.csv
├── 📁 Models
│   └── 📁 .ipynb_checkpoints
│       └── 📄 Collaborative.ipynb
├── 📁 templates
│   ├── 📄 colab.html
│   ├── 📄 index.html
│   └── 📄 top50.html
├── 📄 app.py
├── 📄 Books.pkl
├── 📄 pop.pkl
├── 📄 pt.pkl
├── 📄 README.md
└── 📄 score.pkl
```

---

## 🧗‍♂️ Challenges Faced

- **Data Cleaning**: Merging user ratings with metadata and dealing with missing values.
- **Scalability**: Collaborative filtering can be computationally heavy with large datasets.
- **Cold Start**: New users or books with no ratings pose a challenge.
- **Hybrid Integration**: Merging models effectively to balance relevance and diversity.

---

## 💡 Future Improvements

- Add login functionality to store individual user preferences.
- Integrate real-time feedback to fine-tune recommendations.
- Deploy with a professional UI using React or Streamlit.
- Add voice-based book discovery.

---

## ✨ Credits

Built with ❤️ by Atharva Ghadigaonkar

---
