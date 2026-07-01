# 🎬 Movie Review Sentiment Analysis using Simple RNN

A Deep Learning-based sentiment analysis application that classifies movie reviews as **Positive** or **Negative** using a **Simple Recurrent Neural Network (RNN)** built with TensorFlow/Keras. The project also includes a user-friendly **Streamlit** web application for real-time sentiment prediction.

---

## 📌 Project Overview

Sentiment Analysis is one of the most popular Natural Language Processing (NLP) tasks. This project leverages a Simple RNN model to understand the sequential nature of text and predict the sentiment of movie reviews.

The model is trained on the **IMDB Movie Review Dataset** and deployed using **Streamlit**.

---

## Streamlit Link :https://2kwrydjofhnqelh7d4fgoh.streamlit.app/

## 🚀 Features

- Predicts sentiment of custom movie reviews.
- Deep Learning model built using TensorFlow/Keras.
- Text preprocessing and sequence padding.
- Interactive Streamlit web interface.
- Trained on the IMDB dataset.
- Fast real-time predictions.

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Streamlit
- IMDB Dataset

---

## 📂 Project Structure

```
Movie-review_sentiment_analysis-Rnn/
│
├── app.py                     # Streamlit application
├── Model_training.ipynb       # Model training notebook
├── simple_rnn_imdb.h5         # Trained RNN model
├── requirements.txt           # Dependencies
├── runtime.txt                # Python version (for deployment)
└── README.md
```

---

## 🧠 Model Architecture

```
Input Review
      │
      ▼
Embedding Layer
      │
      ▼
Simple RNN Layer
      │
      ▼
Dense Layer (Sigmoid)
      │
      ▼
Positive / Negative
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/urbeena/Movie-review_sentiment_analysis-Rnn.git
```

Move into the project directory

```bash
cd Movie-review_sentiment_analysis-Rnn
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Dataset

The project uses the **IMDB Movie Review Dataset** available in TensorFlow/Keras.

- 50,000 Movie Reviews
- Binary Classification
- Positive & Negative Reviews

---

## 🔄 Workflow

1. Load IMDB Dataset
2. Text Preprocessing
3. Word Encoding
4. Sequence Padding
5. Build Simple RNN Model
6. Train the Model
7. Save Trained Model
8. Deploy with Streamlit

---

## 📸 Sample Prediction

**Input**

```
The movie was absolutely fantastic with brilliant acting.
```

**Prediction**

```
Positive 😊
```

---

**Input**

```
Worst movie I have ever watched.
```

**Prediction**

```
Negative 😞
```

---

## 📈 Future Improvements

- Replace Simple RNN with LSTM
- Implement Bidirectional LSTM
- Add GRU model comparison
- Attention Mechanism
- Transformer-based sentiment analysis
- Docker deployment
- Cloud deployment

---




## 👩‍💻 Author

**Urbeena Rashid**


---

## ⭐ If you found this project useful, don't forget to give it a star!
