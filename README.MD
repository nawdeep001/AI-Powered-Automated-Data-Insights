# 📊 AI-Powered Automated Data Insights Dashboard

An intelligent data analytics application that automatically analyzes uploaded CSV datasets and generates statistical summaries, interactive visualizations, and AI-generated business insights.

This project provides two deployment options:

* **Flask Web Application** → Professional dashboard experience
* **Gradio Interface** → Fast experimentation and prototyping

---

# Features

## 📁 Dataset Upload & Processing

* Upload CSV datasets instantly
* Automatic dataset ingestion
* Handles missing values automatically
* Cleans and standardizes column names

## Intelligent Data Cleaning

* Missing value handling
* Automatic date detection
* Column normalization
* Dataset preprocessing

## 📊 Exploratory Data Analysis (EDA)

Automatically generates:

* Dataset shape and metadata
* Numeric and categorical column detection
* Missing value analysis
* Descriptive statistics
* Correlation analysis

## 📈 Interactive Visualizations

Built using Plotly:

* Histograms
* Correlation Heatmaps
* Top Category Analysis
* Interactive charts with zoom/pan support

## 🤖 AI-Powered Business Insights

Using LLM-powered analysis:

* Key Findings
* Business Insights
* Risk Detection
* Actionable Recommendations

---

# 🏗 Project Structure

```text
automated-data-insights/

│

├── app_flask.py

├── app_gradio.py

├── data_insights.py

├── ai_insights.py

├── requirements.txt

│

├── templates/

│   ├── index.html

│   └── results.html

│

├── uploads/

│

└── README.md
```

---

# 🛠 Tech Stack

### Backend

* Python
* Flask
* Gradio

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### AI Layer

* OpenAI API
* GPT Models

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone <repo-url>

cd automated-data-insights
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key

OPENAI_BASE_URL=https://api.openai.com/v1
```

---

# ▶ Running Flask Application

```bash
python app_flask.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# ▶ Running Gradio Application

```bash
python app_gradio.py
```

Open:

```text
http://127.0.0.1:7860
```

---

# 📷 Application Workflow

```text
Upload CSV

↓

Data Cleaning

↓

EDA + Statistics

↓

Plot Generation

↓

AI Analysis

↓

Dashboard Results
```

---

# Example Use Cases

* Business Expense Analysis
* Financial Transaction Monitoring
* Procurement Analytics
* Sales Analytics
* Customer Data Exploration
* Fraud Detection Support
* Vendor Analysis

---

# Future Improvements

* Excel Support
* PDF Report Export
* Multi-file Analysis
* Time Series Analysis
* Anomaly Detection
* RAG-based Dataset Q&A
* Agentic Data Analyst

---