# 📈 Retail Demand Forecasting & Inventory Optimization

> An end-to-end machine learning system that forecasts future retail demand and supports inventory planning using historical sales patterns, time-series feature engineering, XGBoost, SQL, Streamlit, FastAPI, and Docker.

---

# 🚀 Live Project

### 🌐 Live Streamlit Dashboard

👉 **[Open Live Dashboard](https://nithin-demand-forecasting-2026.streamlit.app)**

Interactive dashboard for selecting a product family and viewing demand forecasts, inventory recommendations, safety stock, demand risk, and future demand visualization.

### 🔌 Live FastAPI Backend

👉 **[Open FastAPI](https://nithin-retail-demand-api.onrender.com)**

Production-deployed REST API that provides demand forecasting and inventory recommendation results.

### 📚 Swagger API Documentation

👉 **[Open Swagger Docs](https://nithin-retail-demand-api.onrender.com/docs)**

Interactive API documentation for testing the forecasting endpoints.

### 💻 GitHub Repository

👉 **[View Source Code](https://github.com/Nithin10180/Retail-demand-forecasting)**


## 🔗 Project Links
Resource	Link
🚀 Live Streamlit Dashboard	https://nithin-demand-forecasting-2026.streamlit.app
🔌 Live FastAPI Backend	https://nithin-retail-demand-api.onrender.com
📚 Swagger API Documentation	https://nithin-retail-demand-api.onrender.com/docs
💻 GitHub Repository	https://github.com/Nithin10180/Retail-demand-forecasting


---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-MySQL-orange?logo=mysql)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-red)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b?logo=streamlit)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

</p>

---

# 📌 Project Overview

Retail businesses need to estimate future product demand so that inventory can be planned effectively.

Ordering too much inventory can increase holding and storage costs, while ordering too little can lead to stock-outs and missed sales opportunities.

This project builds an **end-to-end Retail Demand Forecasting and Inventory Optimization System** that uses historical retail sales data to predict future demand and support inventory planning decisions.

The project covers the complete machine learning lifecycle:

```text
Raw Retail Data
       ↓
SQL Data Preparation
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Time-Series Features
       ↓
Machine Learning
       ↓
Demand Forecasting
       ↓
Inventory Recommendation
       ↓
FastAPI
       ↓
Streamlit Dashboard
       ↓
Docker
       ↓
Cloud Deployment
```

# 🎯 Problem Statement

Retail demand changes over time due to factors such as:

Historical sales patterns
Weekly seasonality
Monthly patterns
Promotions
Holidays
Store-level differences
Product-family behavior
External factors

Retailers therefore need a reliable way to estimate future demand before making inventory decisions.

The objective of this project is to:

Predict future product demand from historical sales patterns and use those predictions to support better inventory planning decisions.

🎯 Project Objectives
Forecast future retail demand for individual product families.
Analyze historical sales patterns and trends.
Perform SQL-based data preparation and analysis.
Perform exploratory data analysis.
Create time-series forecasting features.
Compare multiple machine learning models.
Generate 7-day future demand forecasts.
Calculate safety stock.
Calculate recommended inventory levels.
Identify demand risk.
Build an interactive Streamlit dashboard.
Develop a FastAPI REST API.
Containerize the backend using Docker.
Deploy the complete application to the cloud.
🏗️ End-to-End Architecture
```text
                  ┌─────────────────────────┐
                  │     Retail Sales Data   │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │       SQL / MySQL       │
                  │ Data Preparation        │
                  │ Aggregation & JOINs     │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ EDA & Data Cleaning      │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Time-Series Feature      │
                  │ Engineering              │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Machine Learning Models  │
                  │                          │
                  │ Linear Regression        │
                  │ Random Forest            │
                  │ XGBoost                  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   7-Day Demand Forecast  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Inventory Planning       │
                  │                          │
                  │ Safety Stock             │
                  │ Recommended Stock        │
                  │ Demand Risk              │
                  └────────────┬────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
           ┌─────────────────┐   ┌─────────────────┐
           │ Streamlit       │   │ FastAPI         │
           │ Dashboard       │   │ REST API        │
           └────────┬────────┘   └────────┬────────┘
                    │                     │
                    ▼                     ▼
           Streamlit Cloud              Render
```

# 📊 Dataset

The project uses historical retail sales data containing information such as:

date
store_nbr
family
sales
onpromotion

Additional supporting information was used for the analytical workflow, including:

Store transactions
Holiday information
Oil price information
Dataset Coverage
Attribute	Value
Start Date	2013-01-01
End Date	2017-08-15
Stores	54
Product Families	33
Total Historical Sales	1,073,645,177.20

The original large raw dataset is not included in this repository.

# 🗄️ SQL Data Engineering

SQL was used as an important part of the data preparation and analytics workflow.

SQL operations included
Creating relational tables
Loading retail data into MySQL
Aggregating daily sales
Aggregating sales by store
Aggregating sales by product family
Calculating transaction totals
Analyzing promotion activity
Joining sales with transaction data
Joining sales with oil-price data
Joining sales with holiday information
Creating analytical datasets for machine learning
Example Business Questions

The SQL analysis helps answer questions such as:

Which product families generate the highest sales?
Which stores generate the highest sales?
How do promotions relate to sales?
What are the daily sales patterns?
How does demand vary by product family?
How do holidays affect demand?
What external factors are associated with sales?

SQL scripts are organized under:

sql/

# 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure and behavior of the retail data.

Areas analyzed
Overall sales trends
Daily demand behavior
Store-level sales
Product-family demand
Promotion activity
Transaction patterns
Holiday effects
External variables
Historical Sales Insights

Some of the major product families observed in the historical sales data include:

GROCERY I
BEVERAGES
PRODUCE
CLEANING
DAIRY

EDA was used to understand historical demand behavior before building the forecasting models.

# ⚙️ Time-Series Feature Engineering

Retail sales are time-dependent, so historical observations were transformed into time-series features.

Calendar Features
Day of week
Day of month
Week of year
Month
Year
Lag Features
Lag 1 day
Lag 7 days
Lag 14 days
Lag 28 days

Lag features allow the model to use previous demand observations as predictive signals.

Rolling Features
7-day rolling mean
14-day rolling mean
28-day rolling mean

Rolling statistics help capture recent demand trends and smooth short-term fluctuations.

Business Features
Promotion count
Oil price
Holiday indicator

# 🤖 Machine Learning

Multiple machine learning models were explored during the forecasting workflow.

Models Evaluated
1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

The final forecasting workflow uses XGBoost as the primary model for demand prediction.

The model learns relationships between historical demand and engineered features such as:

Lagged sales
Rolling demand
Calendar variables
Promotions
External variables

# 📈 Demand Forecasting

The main forecasting objective is to predict demand for the next 7 days.

Forecasting Pipeline
```text
Historical Sales
       ↓
Lag Features
       ↓
Rolling Statistics
       ↓
Calendar Features
       ↓
Promotion & External Features
       ↓
XGBoost Model
       ↓
Future Demand Prediction
       ↓
7-Day Forecast
```

The generated forecast contains:

Forecast date
Product family
Predicted sales

Forecast results are stored in:

outputs/future_demand_forecasts.csv
# 📊 Model Evaluation

The forecasting models are evaluated using regression metrics.

Evaluation Metrics
MAE — Mean Absolute Error
RMSE — Root Mean Squared Error

The forecasting workflow uses chronological splitting rather than randomly shuffling time-series observations.

This helps preserve the temporal relationship between historical data and future observations.

The recorded model metrics are available in:

outputs/model_metrics.csv

# 📦 Inventory Recommendation

The demand forecasting layer is connected to an inventory planning layer.

The forecast is used to estimate how much inventory may be required for the upcoming period.

1. Predicted 7-Day Demand

The system calculates the total expected demand for the upcoming seven days.

2. Demand Variability

Historical demand variability is used to estimate uncertainty.

3. Safety Stock

Safety stock provides additional inventory coverage against demand fluctuations.

4. Recommended Stock

The project uses the following business logic:

Recommended Stock
=
Predicted 7-Day Demand
+
Safety Stock
5. Demand Risk

The system compares predicted demand with historical demand behavior.

The resulting risk categories include:

High Demand
Normal
Low Demand

Inventory recommendations are stored in:

outputs/inventory_recommendations.csv

# 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

Dashboard Features
Product-family selection
Forecasted demand KPI
Recommended stock KPI
Safety stock KPI
Demand risk indicator
Future demand line chart
Daily forecast table
Inventory recommendation summary
User Flow
```text
Select Product Family
        ↓
Send Forecast Request
        ↓
Receive Forecast
        ↓
Display Demand
        ↓
Display Inventory Recommendation
        ↓
Display Demand Risk
```

# 🌐 Live Dashboard

👉 https://nithin-demand-forecasting-2026.streamlit.app

🔌 FastAPI REST API

FastAPI is used as the backend service for serving demand forecasting results.

It separates the forecasting backend from the Streamlit user interface.

API Endpoints
Method	Endpoint	Purpose
GET	/	API health check
GET	/families	Return available product families
POST	/forecast	Return forecast and inventory results

# 📥 Forecast API Example
```text
Request
POST /forecast
{
  "family": "AUTOMOTIVE"
}
Example Response
{
  "family": "AUTOMOTIVE",
  "forecasted_7_day_demand": 1679.96,
  "daily_forecast": [
    {
      "date": "2017-08-16",
      "predicted_sales": 293.06
    },
    {
      "date": "2017-08-17",
      "predicted_sales": 232.48
    },
    {
      "date": "2017-08-18",
      "predicted_sales": 253.95
    }
  ],
  "recommended_stock": 2154.17,
  "safety_stock": 474.21,
  "demand_risk": "Low Demand"
}
```
### 🌐 Live FastAPI

👉 https://nithin-retail-demand-api.onrender.com

### 📚 Swagger Documentation

👉 https://nithin-retail-demand-api.onrender.com/docs

### 🐳 Docker

The FastAPI backend is containerized using Docker.

Docker Architecture
```text
Docker Image
     ↓
Python 3.11
     ↓
FastAPI
     ↓
Uvicorn
     ↓
Retail Forecasting API
```

The repository includes:

Dockerfile
requirements.txt
api.py

Docker provides a reproducible environment for running the backend service.

# ☁️ Cloud Deployment

The project is deployed using separate frontend and backend services.

Frontend

Platform: Streamlit Community Cloud

Live Application:

https://nithin-demand-forecasting-2026.streamlit.app

Backend

Platform: Render

Live API:

https://nithin-retail-demand-api.onrender.com

API Documentation

Swagger:

https://nithin-retail-demand-api.onrender.com/docs

# 🔄 Deployed Application Flow

The final deployed application follows this architecture:
```text
                 USER
                   │
                   ▼
        ┌────────────────────┐
        │ Streamlit Dashboard│
        └─────────┬──────────┘
                  │
                  │ HTTP POST
                  ▼
        ┌────────────────────┐
        │  FastAPI Backend   │
        │      Render        │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Forecast &         │
        │ Inventory Results  │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ JSON API Response  │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Streamlit Dashboard│
        │ Displays Results   │
        └────────────────────┘
```
# 📸 Project Screenshots

Project screenshots are available in:

screenshots/

The screenshots demonstrate:

Live Streamlit dashboard
Product-family demand forecasting
Future demand visualization
Inventory recommendations
Demand risk
FastAPI Swagger interface
API responses
Deployment results

# 📁 Project Structure
```text

Retail-demand-forecasting/
│
├── data/
│
├── models/
│
├── outputs/
│   ├── forecast_model_feature_importance.csv
│   ├── future_demand_forecasts.csv
│   ├── inventory_recommendations.csv
│   ├── model_metrics.csv
│   └── retail_forecasting_predictions.csv
│
├── screenshots/
│
├── sql/
│
├── app.py
├── api.py
├── Dockerfile
├── requirements.txt
├── Retail_Demand_Forecasting_&_Inventory_Optimization.ipynb
├── README.md
├── LICENSE
└── .gitignore
```

# 🧪 Jupyter / Colab Notebook

The complete machine learning workflow is documented in:

Retail_Demand_Forecasting_&_Inventory_Optimization.ipynb

The notebook contains the project workflow including:

Data loading
Data exploration
Data cleaning
SQL-related analysis
Feature engineering
Model training
Model evaluation
Forecast generation
Inventory recommendations
Visualization
🛠️ Technologies Used
Programming
Python 3.11
Data Engineering
SQL
MySQL
Pandas
NumPy
Machine Learning
Scikit-learn
XGBoost
Visualization
Matplotlib
Application Development
Streamlit
FastAPI
Pydantic
Uvicorn
Deployment & DevOps
Docker
Git
GitHub
Streamlit Community Cloud
Render

# ▶️ Run the Project Locally
1. Clone the Repository
git clone https://github.com/Nithin10180/Retail-demand-forecasting.git

Navigate into the project:

cd Retail-demand-forecasting
2. Install Dependencies
pip install -r requirements.txt
3. Run Streamlit
streamlit run app.py

The Streamlit dashboard will open in your browser.

4. Run FastAPI

Open another terminal and run:

uvicorn api:app --host 0.0.0.0 --port 8000
5. Open Swagger

Once FastAPI is running, open:

http://localhost:8000/docs

You can use Swagger UI to test the API endpoints.

# 🧪 API Testing

The FastAPI backend can be tested using:

Swagger UI
Python Requests
cURL
Postman
Python Example
import requests

response = requests.post(
    "https://nithin-retail-demand-api.onrender.com/forecast",
    json={
        "family": "AUTOMOTIVE"
    }
)

print(response.status_code)
print(response.json())

## 💼 Business Value

This project connects machine learning predictions with a practical retail business decision.

The system can support:

Demand planning
Inventory replenishment
Stock planning
Product-level demand analysis
Demand risk identification
Data-driven ordering decisions

Instead of only generating a machine learning prediction, the project connects the prediction to an inventory planning workflow:
```text
Forecast Demand
      ↓
Estimate Required Inventory
      ↓
Calculate Safety Stock
      ↓
Recommend Stock Level
      ↓
Identify Demand Risk
```
#### ⭐ Key Features
✅ SQL-based retail data preparation
✅ Exploratory data analysis
✅ Time-series feature engineering
✅ Lag features
✅ Rolling-window features
✅ Calendar features
✅ Multiple machine learning models
✅ XGBoost demand forecasting
✅ 7-day future demand prediction
✅ Safety stock calculation
✅ Recommended inventory calculation
✅ Demand risk classification
✅ Interactive Streamlit dashboard
✅ FastAPI REST API
✅ Swagger API documentation
✅ Docker containerization
✅ GitHub version control
✅ Streamlit Cloud deployment
✅ Render API deployment
✅ Streamlit → FastAPI integration

## 🔮 Future Improvements

Future versions of the project could include:

Store-specific forecasting
Hierarchical forecasting
SARIMA / Prophet comparison
More advanced inventory optimization
Promotion-aware forecasting
Automated hyperparameter optimization
Automated model retraining
Model monitoring
Prediction drift detection
Cloud database integration
CI/CD automation
Scheduled forecast generation
Real-time model inference
Automated forecast monitoring dashboards

### 🎓 What This Project Demonstrates

This project demonstrates a complete Data Science and ML Engineering workflow:
```text

Data Collection
      ↓
SQL
      ↓
Data Cleaning
      ↓
EDA
      ↓
Feature Engineering
      ↓
Time-Series Modeling
      ↓
Machine Learning
      ↓
Forecast Evaluation
      ↓
Business Decision Support
      ↓
Streamlit
      ↓
FastAPI
      ↓
Docker
      ↓
Cloud Deployment
```

The project demonstrates how a machine learning solution can move from raw retail data to a deployed business application.

#### 📚 Learning Outcomes

Through this project, the following practical concepts were implemented:

Data preprocessing
SQL data analysis
Exploratory Data Analysis
Time-series forecasting
Feature engineering
Machine learning model comparison
Regression evaluation
Demand forecasting
Inventory planning
REST API development
Interactive dashboard development
Docker containerization
Git and GitHub
Cloud deployment
Frontend-backend integration
### 👨‍💻 Author
Nithin

B.Tech Computer Science & Engineering

### GitHub

https://github.com/Nithin10180

#### 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.
