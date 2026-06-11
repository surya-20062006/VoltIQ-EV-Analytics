# ⚡ VoltIQ - Smart Indian EV Market Analytics Platform

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 📌 Project Overview

**VoltIQ** is a Data Science and Business Intelligence dashboard developed to analyze the Indian Electric Vehicle (EV) market. The project transforms raw EV registration data into meaningful business insights using interactive visualizations and a professional multi-page Streamlit dashboard.

The platform helps users understand EV adoption trends across India through state-wise analysis, vehicle category analysis, sales trends, and business intelligence reporting.

---

# 🎯 Objectives

* Analyze Indian EV market trends.
* Perform data cleaning and preprocessing.
* Conduct Exploratory Data Analysis (EDA).
* Build an interactive Business Intelligence dashboard.
* Generate actionable business insights.
* Visualize EV sales growth across India.

---

# 🚀 Features

## 🏠 Home Dashboard

* KPI Cards
* Total EV Registrations
* Total States
* Vehicle Categories
* Vehicle Types
* Year-wise Sales Trend
* Interactive Filters
* Download Filtered Data
* Business Insights

---

## 📈 Sales Analysis

* Year-wise EV Sales Trend
* Monthly Sales Analysis
* Quarter-wise Sales Analysis
* Sales Table
* Search by Year
* Dynamic Business Insights

---

## 🗺️ State Analysis

* Top 10 EV States
* Bottom 10 EV States
* State Ranking Table
* Search State
* KPI Cards
* State-wise Business Insights

---

## 🚗 Vehicle Analysis

* Vehicle Category Distribution
* Vehicle Type Analysis
* Top Vehicle Classes
* Vehicle Ranking Table
* Search Vehicle Type
* Dynamic Insights

---

## 📊 Business Insights

* Top Performing State
* Best Sales Year
* Dominant Vehicle Category
* EV Growth Analysis
* Future Market Potential

---

## ℹ️ About

* Project Description
* Tech Stack
* Dataset Information
* Developer Details

---

# 📂 Project Structure

```text
VoltIQ/
│
├── data/
│   ├── raw/
│   │   └── ev_sales.csv
│   │
│   └── processed/
│       └── cleaned_ev_sales.csv
│
├── notebooks/
│   └── ev_market_analysis.ipynb
│
├── pages/
│   ├── 1_Sales_Analysis.py
│   ├── 2_State_Analysis.py
│   ├── 3_Vehicle_Analysis.py
│   ├── 4_Business_Insights.py
│   └── 5_About.py
│
├── utils/
│
├── images/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset Information

### Dataset Size

* Total Records: **96,845**
* Total Columns: **8**

### Features

| Column            |
| ----------------- |
| Year              |
| Month_Name        |
| Date              |
| State             |
| Vehicle_Class     |
| Vehicle_Category  |
| Vehicle_Type      |
| EV_Sales_Quantity |

---

# 🔬 Data Science Workflow

## Phase 1 : Project Setup

* Project Structure
* Virtual Environment
* Git Initialization
* GitHub Repository Creation

---

## Phase 2 : Dataset Collection

* Indian EV Sales Dataset
* Dataset Organization

---

## Phase 3 : Data Understanding

* Load Dataset
* Check Shape
* Check Data Types
* Check Missing Values
* Check Duplicates
* Initial Observations

---

## Phase 4 : Data Cleaning

* Remove Duplicates
* Convert Data Types
* Convert Date Format
* Feature Engineering
* Create Quarter Column
* Create Month Number

---

## Phase 5 : Exploratory Data Analysis

* Year-wise Sales
* Monthly Sales
* State Analysis
* Vehicle Category Analysis
* Vehicle Type Analysis
* Business Questions

---

## Phase 6 : Dashboard Development

* Streamlit Setup
* KPI Cards
* Interactive Charts
* Sidebar Filters
* Download Button

---

## Phase 7 : Multi-page Dashboard

* Home
* Sales Analysis
* State Analysis
* Vehicle Analysis
* Business Insights


---

## Phase 8 : Business Intelligence

* Dynamic Insights
* State Ranking
* Vehicle Ranking
* Growth Analysis

---

# 📈 Visualizations

* KPI Cards
* Line Chart
* Bar Chart
* Horizontal Bar Chart
* Donut Chart
* Pie Chart
* Area Chart
* Interactive Plotly Graphs

---

# 🛠 Tech Stack

## Programming Language

* Python

## Libraries

* Pandas
* NumPy
* Plotly
* Streamlit
* Matplotlib
* Seaborn

## Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/surya-20062006/VoltIQ-EV-Analytics.git
```

## Move into Project

```bash
cd VoltIQ-EV-Analytics
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# 📊 Business Insights

* EV registrations have shown significant growth.
* Two-wheelers dominate the Indian EV market.
* Certain states contribute a major share of EV adoption.
* The Indian EV ecosystem has strong future potential.

---


# 🎓 Learning Outcomes

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Business Analytics
* Dashboard Development
* Interactive Data Visualization
* Git & GitHub Workflow
* Streamlit Deployment

---

# 🔮 Future Enhancements

* India EV Adoption Map
* EV Sales Forecasting
* Machine Learning Integration
* Real-time Data Updates
* Advanced Filtering
* Dashboard Export to PDF
* Cloud Deployment

---

