
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(
    title="Retail Demand Forecasting API",
    description="API for retail demand forecasting and inventory recommendations",
    version="1.0.0"
)

# Load forecast and inventory data
forecasts = pd.read_csv("future_demand_forecasts.csv")
inventory = pd.read_csv("inventory_recommendations.csv")


class ForecastRequest(BaseModel):
    family: str


@app.get("/")
def home():
    return {
        "message": "Retail Demand Forecasting API is running",
        "status": "success"
    }


@app.get("/families")
def get_families():
    families = sorted(
        forecasts["family"].dropna().unique().tolist()
    )

    return {
        "families": families
    }


@app.post("/forecast")
def forecast(request: ForecastRequest):

    family = request.family

    forecast_data = forecasts[
        forecasts["family"] == family
    ].copy()

    inventory_data = inventory[
        inventory["family"] == family
    ].copy()

    if forecast_data.empty:
        return {
            "error": f"Product family '{family}' not found"
        }

    forecast_data["date"] = pd.to_datetime(
        forecast_data["date"]
    )

    result = {
        "family": family,
        "forecasted_7_day_demand": round(
            float(
                forecast_data["predicted_sales"].sum()
            ),
            2
        ),
        "daily_forecast": [
            {
                "date": row["date"].strftime("%Y-%m-%d"),
                "predicted_sales": round(
                    float(row["predicted_sales"]),
                    2
                )
            }
            for _, row in forecast_data.iterrows()
        ]
    }

    if not inventory_data.empty:

        result["recommended_stock"] = round(
            float(
                inventory_data[
                    "recommended_stock"
                ].iloc[0]
            ),
            2
        )

        result["safety_stock"] = round(
            float(
                inventory_data[
                    "safety_stock"
                ].iloc[0]
            ),
            2
        )

        result["demand_risk"] = str(
            inventory_data[
                "risk_category"
            ].iloc[0]
        )

    return result
