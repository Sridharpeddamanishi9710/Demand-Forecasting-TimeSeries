# 📊 Demand Forecasting & Time Series Modeling

## 🚀 Overview
This project focuses on forecasting future sales demand using time series models and translating predictions into actionable business insights.

Instead of relying on a single model, multiple forecasting techniques were compared to identify the most effective approach for real-world decision-making.

---

## 🎯 Objectives
- Analyze historical sales data
- Identify trends and seasonality
- Build multiple forecasting models
- Compare model performance
- Generate business recommendations

---

## 📂 Dataset
- Source: Kaggle Sales Dataset
- Data Type: Time series (monthly sales)
- Key Features:
  - Date
  - Sales

---

## ⚙️ Models Used
- ARIMA (AutoRegressive Integrated Moving Average)
- SARIMA (Seasonal ARIMA)
- Prophet (Facebook/Meta)

---

## 📊 Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

---

## 📈 Key Results
- SARIMA performed best due to strong seasonal patterns
- ARIMA captured trend but failed in seasonality
- Prophet provided smoother forecasts but slightly higher error

---

## 💼 Business Impact
This system helps businesses:

- Optimize inventory levels
- Reduce overstocking and storage costs
- Prevent stockouts during high demand
- Improve staffing decisions during peak periods
- Support better demand planning and forecasting

---

## 🖥️ Streamlit Dashboard

The project includes an interactive dashboard with:

- Sales trend visualization
- Model comparison
- Forecast insights
- Business recommendations

---

## 📁 Project Structure

Demand-Forecasting-TimeSeries/
│
├── data/
├── notebooks/
├── src/
├── models/
├── outputs/
├── app/
├── requirements.txt
└── README.md


---

## ▶️ How to Run Locally

git clone https://github.com/Sridharpeddamanishi9710/Demand-Forecasting-TimeSeries.git
cd Demand-Forecasting-TimeSeries

pip install -r requirements.txt
streamlit run app/streamlit_app.py

🌐 Live Demo

  https://demand-forecasting-timeseries-sri9710.streamlit.app/
