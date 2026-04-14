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
* Generates charts dynamically
* Suggests graph type using AI
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

---

## ⚠️ How to Use (IMPORTANT)

This project does NOT have a frontend UI.

👉 To generate visualization, you must use **Postman** or any API testing tool.

---

## 📬 Using Postman

### Step 1:

* Open Postman
* Select **POST** method

### Step 2:

Enter URL:

```
http://localhost:5000/visualize
```

### Step 3:

Go to **Body → raw → JSON**

### Step 4:

Paste sample input:

```json
{
  "results": "product_category_name purchase_count\ncama_mesa_banho 11115\nbeleza_saude 9670"
}
```

### Step 5:

Click **Send**

---

## 📤 Output

* Returns a **PNG image** of the generated chart

---

## 🧠 Future Improvements

* Add frontend UI
* Support multiple chart types
* Real-time dashboard

---

## 👩‍💻 Author

Nikita Narsingrao Biradar
