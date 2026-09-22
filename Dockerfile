FROM python:3.11-slim

WORKDIR /app

COPY api.py .
COPY requirements.txt .

COPY outputs/future_demand_forecasts.csv outputs/
COPY outputs/inventory_recommendations.csv outputs/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]