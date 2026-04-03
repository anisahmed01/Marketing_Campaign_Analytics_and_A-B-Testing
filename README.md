# Marketing Campaign Analytics: A/B Testing & Conversion Optimization  
**SQL | Python | Power BI | Statistics**

---

## 📌 Overview
Built an end-to-end analytics pipeline to evaluate cross-channel marketing performance across Facebook and Instagram campaigns.  
The project focuses on optimizing budget allocation to maximize conversions while minimizing cost per acquisition (CPA).

---

## 🔄 Data Pipeline
Raw Data → Data Cleaning → Feature Engineering → SQL Analysis → Statistical Testing → Dashboard  

---

## 🗄️ Dataset
- 1000 records of campaign-level data  
- Metrics: Views, Clicks, Conversions, Costs (Facebook & Instagram)  
- Cleaned dataset: 939 records after preprocessing  

---

## 🛠️ Tools & Technologies
- **Python:** pandas, numpy, scipy, matplotlib, seaborn  
- **SQL (SQLite):** Aggregation & campaign analysis  
- **Statistics:** A/B Testing (t-test), Linear Regression  
- **Matplotlib & Seaborn:** Dashboard & reporting  

---

## 📊 Key Metrics Engineered
- Total Spend, Total Clicks, Total Conversions  
- Overall CTR & Conversion Rate  
- Cost Per Click (CPC)  
- Cost Per Acquisition (CPA)  

---

## 🔍 Key Insights

### 📈 Platform Performance
- Facebook outperforms Instagram in volume:
  - Conversions: **64.8K vs 45.5K**
  - Clicks: **683K vs 533K**
- A/B test confirms **statistically higher CTR on Facebook (p < 0.05)**

---

### 🎯 Campaign Performance
- Best campaigns:
  - **FB_A (CPA ≈ $10.08)**
  - **IG_X (CPA ≈ $10.12)**
- Underperforming:
  - **FB_C, IG_Z (CPA > $13)**

---

### 💰 Cost & Efficiency
- Strong correlation:
  - Spend vs Conversions → **0.93**
- Clicks drive conversions:
  - Regression R² = **0.79**

---

### ⚠️ Risk Detection
- Identified **high CPA outliers (> $35)**  
- Indicates inefficient “bleed days” in ad spend  

---

## 📊 Statistical Analysis

### A/B Testing (CTR Comparison)
- T-statistic: **7.40**  
- P-value: **< 0.001**  
👉 Facebook significantly outperforms Instagram in engagement  

---

### Regression Analysis
- Predictor: Total Clicks  
- R²: **0.792**  
👉 Clicks are a strong driver of conversions  

---

## 📊 Dashboard
- Campaign performance tracking  
- Platform comparison  
- CPA & ROI analysis  

---
## 📁 Repository Structure

```
Marketing-Campaign-Analytics-A-B-Testing-Conversion-Optimization-SQL-Python-Statistics/
│
├── Dashboard_images         # images of Dashboard
│
├── data                     # raw csv data 
│   
│
├── sql/
│   └── campaign_analysis.sql      # SQL queries for aggregation & insights
│
├── src/
│   └── data_generation.py         # Script to generate synthetic dataset
│
│
├── Marketing_Campaign_Analytics_A_B_Testing_&_Conversion_Optimization.ipynb     # # Full analysis (EDA, A/B testing, regression)

│
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

---

## 🚀 Business Recommendations

- Reallocate **~20% budget from Instagram to Facebook**  
- Implement **CPA threshold (e.g., $20)** to control spend  
- Optimize or pause **FB_C and IG_Z campaigns**  
- Focus on improving **conversion quality, not just CTR**

---

## 🎯 Key Takeaways
- Built end-to-end analytics pipeline  
- Applied statistical methods for decision-making  
- Translated data into actionable business strategy  

---
## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
Core Libraries
pandas
numpy
matplotlib
seaborn
scipy
sqlalchemy
```
---
## ⚙️ How to Run

1. ### Clone the repository:
```
git clone https://https://github.com/anisahmed01/Marketing-Campaign-Analytics-A-B-Testing-Conversion-Optimization-SQL-Python-Statistics
```
2. ### Install dependencies:
```
pip install -r requirements.txt
```
3. ### Run data generation:
```
python src/data_generation.py
```
4. ### Open Notebook
```
jupyter notebook notebooks/marketing_analysis.ipynb
```
---

## 🧠 Methodology

- Data Cleaning & Preprocessing  
- Feature Engineering  
- SQL Aggregation  
- Exploratory Data Analysis (EDA)  
- A/B Testing (t-test)  
- Regression Analysis  
- Business Insight Generation

---
## ⚠️ Assumptions

- Dataset is synthetically generated with realistic constraints  
- All monetary values are assumed in USD  
- Campaign performance differences are simulated based on realistic CTR and conversion ranges
---
# 👤 Author
Anis Ahmed
