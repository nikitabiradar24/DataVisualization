# 📊 Data Visualization API

## 🔍 Description

This project is a Flask-based API that generates data visualizations from structured input data. It processes query results, converts them into a DataFrame, and dynamically generates charts.

---

## ⚙️ Tech Stack

* Python
* Flask
* Pandas
* Matplotlib
* Ollama (for graph suggestion)

---

## 🚀 Features

* Accepts data via API (`/visualize`)
* Converts raw input into DataFrame
* Generates bar charts dynamically
* Suggests graph type using AI (Ollama)
* Returns visualization as image

---

## 📁 Project Structure

* `app.py` → Flask API for visualization
* `query.py` → Data processing & graph logic

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install flask pandas matplotlib flask-cors
```

### 2. Run the server

```bash
python app.py
```

### 3. API Endpoint

```
POST /visualize
```

---

## 📥 Sample Input

```json
{
  "results": "product_category_name purchase_count\ncama_mesa_banho 11115\nbeleza_saude 9670"
}
```

---

## 📤 Output

* Returns a **PNG image** of the generated chart

---

## 🧠 Future Improvements

* Add multiple chart types
* Improve UI integration
* Add real-time dashboard

---

## 👩‍💻 Author

Nikita Narsingrao Biradar
