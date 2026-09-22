import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

API_URL = "https://nithin-retail-demand-api.onrender.com/forecast"

st.title("📈 Retail Demand Forecasting & Inventory Optimization")
st.write(
    "Forecast future product demand and support inventory planning."
)

# Product families
families = [
    "AUTOMOTIVE",
    "BABY CARE",
    "BEAUTY",
    "BEVERAGES",
    "BOOKS",
    "BREAD/BAKERY",
    "CELEBRATION",
    "CLEANING",
    "DAIRY",
    "DELI",
    "EGGS",
    "FROZEN FOODS",
    "GROCERY I",
    "GROCERY II",
    "HARDWARE",
    "HOME AND KITCHEN I",
    "HOME AND KITCHEN II",
    "HOME APPLIANCES",
    "HOME CARE",
    "LADIESWEAR",
    "LAWN AND GARDEN",
    "LINGERIE",
    "LIQUOR,WINE,BEER",
    "MAGAZINES",
    "MEATS",
    "PERSONAL CARE",
    "PET SUPPLIES",
    "PLAYERS AND ELECTRONICS",
    "POULTRY",
    "PREPARED FOODS",
    "PRODUCE",
    "SCHOOL AND OFFICE SUPPLIES",
    "SEAFOOD"
]

selected_family = st.selectbox(
    "Select Product Family",
    families
)

# Call FastAPI
try:
    response = requests.post(
        API_URL,
        json={"family": selected_family},
        timeout=90
    )

    if response.status_code != 200:
        st.error(
            f"API request failed with status code "
            f"{response.status_code}"
        )
        st.stop()

    result = response.json()

except requests.exceptions.RequestException as e:
    st.error(f"Unable to connect to FastAPI: {e}")
    st.stop()

# Extract API response
forecasted_demand = result["forecasted_7_day_demand"]
recommended_stock = result.get("recommended_stock", 0)
safety_stock = result.get("safety_stock", 0)
demand_risk = result.get("demand_risk", "N/A")

daily_forecast = pd.DataFrame(
    result["daily_forecast"]
)

daily_forecast["date"] = pd.to_datetime(
    daily_forecast["date"]
)

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Forecasted Demand",
    f"{forecasted_demand:,.0f}"
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
    demand_risk
)

# Forecast chart
st.subheader("Future Demand Forecast")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    daily_forecast["date"],
    daily_forecast["predicted_sales"],
    marker="o"
)

ax.set_title(
    f"{selected_family} - Future Demand"
)

ax.set_xlabel("Date")
ax.set_ylabel("Predicted Sales")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Daily forecast table
st.subheader("Daily Forecast")

display_forecast = daily_forecast.rename(
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
    f"**Demand risk:** {demand_risk}"
)