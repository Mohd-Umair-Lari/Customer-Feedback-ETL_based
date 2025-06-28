# Customer-Feedback-ETL_based

A Python FastAPI microservice for ingesting, analyzing, and exposing analytics on e-commerce product data.

## Features

- Upload product data (CSV)
- Automated ETL: Clean, store, and analyze data
- REST endpoints for real-time analytics (average price, top category, average rating)
- SQLite for storage, Pandas for analytics
- Pytest-based test suite

## Usage

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn app.main:app --reload`
4. Test endpoints:
    - `POST /upload` with a CSV file (see `app/sample_products.csv`)
    - `GET /insights` for analytics

## Testing

1. Upload Data
 - User POSTs sample_products.csv to /upload
 - Backend reads the CSV, stores products in DB, computes analytics

2. Analytics Computed
 - Average price: 443.6
 - Top category: Electronics
 - Average rating: 4.44

3. Get Insights
 - User GETs /insights
 - Service returns latest analytics as JSON
