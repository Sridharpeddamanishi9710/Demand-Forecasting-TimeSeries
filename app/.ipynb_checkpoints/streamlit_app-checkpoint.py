import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Demand Forecasting Dashboard",
    layout="wide"
)

st.title("📊 Demand Forecasting & Time Series Dashboard")
st.write("ARIMA vs SARIMA vs Prophet model comparison with business insights")

DATA_PATH = "data/processed/monthly_sales.csv"
RESULTS_PATH = "outputs/metrics/model_results.csv"
BUSINESS_PATH = "outputs/metrics/business_insight.csv"
PLOT_PATH = "outputs/plots/comparison.png"

required_files = [DATA_PATH, RESULTS_PATH, BUSINESS_PATH]

for file in required_files:
    if not os.path.exists(file):
        st.error(f"File not found: {file}")
        st.stop()

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

results_df = pd.read_csv(RESULTS_PATH)
business_df = pd.read_csv(BUSINESS_PATH)

st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Select Page",
    [
        "Overview",
        "Sales Trend",
        "Model Comparison",
        "Future Forecast",
        "Business Insights"
    ]
)

# =========================
# OVERVIEW
# =========================
if page == "Overview":
    st.subheader("Project Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Months", len(df))
    col2.metric("Total Sales", f"{df['sales'].sum():,.0f}")
    col3.metric("Average Monthly Sales", f"{df['sales'].mean():,.0f}")

    st.write("""
    This project forecasts future sales demand using time series models.
    It compares ARIMA, SARIMA, and Prophet models and converts forecasting
    results into business recommendations for inventory and demand planning.
    """)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

# =========================
# SALES TREND
# =========================
elif page == "Sales Trend":
    st.subheader("Monthly Sales Trend")

    start_date = st.date_input("Start Date", df["date"].min())
    end_date = st.date_input("End Date", df["date"].max())

    filtered_df = df[
        (df["date"] >= pd.to_datetime(start_date)) &
        (df["date"] <= pd.to_datetime(end_date))
    ]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(filtered_df["date"], filtered_df["sales"], marker="o")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.grid(True)

    st.pyplot(fig)

    st.write("""
    This trend chart helps identify sales growth, decline, and possible seasonal
    demand patterns across months.
    """)

# =========================
# MODEL COMPARISON
# =========================
elif page == "Model Comparison":
    st.subheader("Model Performance Comparison")

    st.dataframe(results_df)

    best_model = results_df.sort_values("MAPE").iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Best Model", best_model["Model"])
    col2.metric("Best RMSE", round(best_model["RMSE"], 2))
    col3.metric("Best MAPE", f"{round(best_model['MAPE'], 2)}%")

    model_choice = st.selectbox(
        "Select model to inspect",
        results_df["Model"].tolist()
    )

    selected_model = results_df[results_df["Model"] == model_choice].iloc[0]

    st.write(f"### Selected Model: {model_choice}")

    c1, c2, c3 = st.columns(3)
    c1.metric("MAE", round(selected_model["MAE"], 2))
    c2.metric("RMSE", round(selected_model["RMSE"], 2))
    c3.metric("MAPE", f"{round(selected_model['MAPE'], 2)}%")

    st.subheader("Actual vs Predicted Sales")

    if os.path.exists(PLOT_PATH):
        st.image(PLOT_PATH)
    else:
        st.warning("Comparison plot not found. Run 06_Model_Comparison.ipynb first.")

    st.write("""
    Lower MAE, RMSE, and MAPE values indicate better forecasting performance.
    The best model is selected based on the lowest MAPE value.
    """)

# =========================
# FUTURE FORECAST
# =========================
elif page == "Future Forecast":
    st.subheader("Future Demand Forecast")

    best_model = business_df["Best_Model"].iloc[0]

    st.success(f"Best model selected for forecasting: {best_model}")

    st.write("""
    This section represents the future demand decision layer.
    The selected best model can be used to forecast upcoming sales and support
    inventory planning.
    """)

    st.line_chart(df.set_index("date")["sales"])

    avg_sales = df["sales"].mean()
    recent_avg = df["sales"].tail(3).mean()

    col1, col2 = st.columns(2)
    col1.metric("Average Monthly Sales", f"{avg_sales:,.0f}")
    col2.metric("Recent 3-Month Avg Sales", f"{recent_avg:,.0f}")

    if recent_avg > avg_sales * 1.10:
        st.success("Recent demand is higher than average. Prepare additional inventory.")
    elif recent_avg < avg_sales * 0.90:
        st.warning("Recent demand is lower than average. Avoid overstocking.")
    else:
        st.info("Demand is stable. Maintain normal inventory levels.")

# =========================
# BUSINESS INSIGHTS
# =========================
elif page == "Business Insights":
    st.subheader("Business Recommendation")

    st.dataframe(business_df)

    best_model = business_df["Best_Model"].iloc[0]
    recommendation = business_df["Recommendation"].iloc[0]

    st.success(f"Best Model Used: {best_model}")

    if "increase" in recommendation.lower():
        st.success(recommendation)
    elif "decrease" in recommendation.lower() or "reduce" in recommendation.lower():
        st.warning(recommendation)
    else:
        st.info(recommendation)

    st.write("""
    ### Business Impact

    Better demand forecasting helps businesses:

    - Reduce overstocking and inventory cost
    - Prevent stockouts during high-demand periods
    - Plan staffing for peak demand
    - Improve product and supply-chain decisions
    - Support better promotion and sales planning
    """)