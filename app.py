
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

# Load data
forecasts = pd.read_csv("future_demand_forecasts.csv")
inventory = pd.read_csv("inventory_recommendations.csv")

forecasts["date"] = pd.to_datetime(forecasts["date"])

# Make numeric columns numeric
forecasts["predicted_sales"] = pd.to_numeric(
    forecasts["predicted_sales"],
    errors="coerce"
).fillna(0)

numeric_inventory_cols = [
    "recommended_stock",
    "safety_stock",
    "predicted_7_day_demand",
    "avg_daily_demand"
]

for col in numeric_inventory_cols:
    if col in inventory.columns:
        inventory[col] = pd.to_numeric(
            inventory[col],
            errors="coerce"
        ).fillna(0)

st.title("📈 Retail Demand Forecasting & Inventory Optimization")
st.write(
    "Forecast future product demand and support inventory planning."
)

families = sorted(forecasts["family"].dropna().unique())

selected_family = st.selectbox(
    "Select Product Family",
    families
)

family_forecast = (
    forecasts[
        forecasts["family"] == selected_family
    ]
    .sort_values("date")
    .copy()
)

family_inventory = inventory[
    inventory["family"] == selected_family
].copy()

# KPI calculations
total_demand = float(
    family_forecast["predicted_sales"].sum()
)

if not family_inventory.empty:

    recommended_stock = float(
        family_inventory["recommended_stock"].iloc[0]
    )

    safety_stock = float(
        family_inventory["safety_stock"].iloc[0]
    )

    risk = str(
        family_inventory["risk_category"].iloc[0]
    )

else:
    recommended_stock = 0.0
    safety_stock = 0.0
    risk = "N/A"

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Forecasted Demand",
    f"{total_demand:,.0f}"
)

col2.metric(
    "Recommended Stock",
    f"{recommended_stock:,.0f}"
)

col3.metric(
    "Safety Stock",
    f"{safety_stock:,.0f}"
)

col4.metric(
    "Demand Risk",
    risk
)

# Forecast chart
st.subheader("Future Demand Forecast")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    family_forecast["date"],
    family_forecast["predicted_sales"],
    marker="o"
)

ax.set_xlabel("Date")
ax.set_ylabel("Predicted Sales")
ax.set_title(
    f"{selected_family} - Future Demand"
)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Daily forecast
st.subheader("Daily Forecast")

display_forecast = family_forecast[
    ["date", "predicted_sales"]
].rename(
    columns={
        "date": "Date",
        "predicted_sales": "Predicted Sales"
    }
)

st.dataframe(
    display_forecast,
    width="stretch"
)

# Inventory recommendation
st.subheader("Inventory Recommendation")

st.write(
    f"**Recommended stock:** "
    f"{recommended_stock:,.0f} units"
)

st.write(
    f"**Safety stock:** "
    f"{safety_stock:,.0f} units"
)

st.write(
    f"**Demand risk:** {risk}"
)
