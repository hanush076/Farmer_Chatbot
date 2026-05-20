# 👨‍🌾 Farmer-Chatbot: An Agricultural Query System

A smart, terminal-based agricultural chatbot powered by a custom dataset and lightweight NLP pipeline, designed to answer real-world farmer queries and provide expert advice on farming practices.

---

## 📝 Project Overview

The **Farmer-Chatbot** is a natural language processing (NLP) project focused on building a smart assistant for agriculture-related queries. It acts as a knowledge base, providing quick and accurate responses to questions asked by farmers.

The chatbot operates via a **command-line interface** (`terminal_chatbot.py`) for easy and direct use.

---

## 💡 Key Features

- **🌾 Agricultural NLP:** Specializes in farming-related topics like pests, crops, soil, and irrigation.
- **📚 Knowledge Base Integration:** Uses a structured `knowledge_base.json` file for retrieving context-based answers.
- **🧠 Custom Dataset:** Built from real-world farmer queries and expert responses (`processed_training_data.json`).
- **🛠️ Fuzzy + Rule-Based Matching:** Uses `fuzzywuzzy` for approximate text matching and `nltk` for text preprocessing.

---

## 🧠 Model Details

- **Approach:**
  - Text preprocessing with `nltk` (e.g., tokenization, lowercasing, stopword removal)
  - Semantic similarity matching using `fuzzywuzzy`'s `fuzz.ratio` or `fuzz.token_sort_ratio`
  - Returns the most similar question from the knowledge base and its corresponding answer
- **Libraries Used:** `nltk`, `fuzzywuzzy`, `python-Levenshtein` (for performance boost), and basic Python
- **Training Dataset:** Based on [Farmers Call Query Data (Kaggle)](https://www.kaggle.com/datasets/daskoushik/farmers-call-query-data-qa), preprocessed into `processed_training_data.json`

---

## 📁 Files and Structure

| File/Folder | Purpose |
|-------------|---------|
| `terminal_chatbot.py` | Main chatbot script |
| `requirements.txt`    | Python package dependencies |
| `dataset/`            | Contains zipped versions of raw and processed data |

---

## 🚀 Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sunn-y103/Farmer-Chatbot.git
    cd Farmer-Chatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download NLTK data (first-time only):**
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

4. **Run the chatbot:**
    ```bash
    python terminal_chatbot.py
    ```

---

## 📦 Future Improvements

- Voice and web interface
- Regional language support
- Advanced intent classification and ranking

---

## 🙌 Acknowledgments

- Dataset: [Farmers Call Query Data (Kaggle)](https://www.kaggle.com/datasets/daskoushik/farmers-call-query-data-qa)
- Model is uploaded on Hugging Face: [Hugging Face Model](https://huggingface.co/Sunny6727/knowledge_base/tree/main)
- NLP Tools: `nltk`, `fuzzywuzzy`, `Levenshtein`
