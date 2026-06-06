# E-commerce Data Analytics Project

## Overview
Built an ELT pipeline using BigQuery to analyze user behavior and conversion funnel.

## Data Sources
E-commerce clickstream and transaction data Customer 360 Dataset from Kaggle that included multiple related tables such as clickstream events, customers, orders and more.
The dataset offers a detailed view of user interactions and transactions, enabling analysis of user behavior.

## Architecture
Python extract(preprocessing and sampling) → BigQuery → SQL transformations → Analysis

## Data Modeling 
created models for user activity, sessions and enriched dimensions

## Key Analyses
- Funnel conversion rates
- Payer vs non-payer behavior
- Retention analysis

## Key Insights
- for further analyis go to [Insight analysis](sql/analysis/Insights.md)


## Analysis Mapping
| Analysis           | Tables Used                             |
| ------------------ | --------------------------------------- |
| DAU / MAU          | `fact_events`                           |
| Retention Analysis | `fact_events`                           |
| Conversion Funnel  | `fact_events`, `stg_orders`             |
| Refund Rate        | `stg_orders`                            |
| Customer Analysis  | `dim_users`, `stg_orders`               |
| Revenue Analysis   | `stg_orders`                            |
| Top Categories     | `stg_orders`, `stg_products`            |
| Payer Analysis     | `dim_payers`, `dim_users`, `stg_orders` |
| Session Analysis   | `dim_sessions`, `fact_events`           |


## Project Structure
```
ecommerce-data-project/
│
├── assets/
│   └── Project diagrams and dashboard screenshots
│
├── dashboard/
│   └── Tableau dashboards and exports
│
├── data/
│   └── Raw CSV files (excluded from Git)
│
├── scripts/
│   │
│   ├── load_to_bigquery.py
│   │   └── Uploads source CSV files into BigQuery
│   │
│   ├── split_data.py
│   │   └── Samples and reduces large clickstream datasets
│   │
│   └── calculation_refund_rate.py
│       └── Python-based refund rate calculations
│
├── sql/
│   │
│   ├── staging/
│   │   ├── stg_events.sql
│   │   ├── stg_orders.sql
│   │   └── stg_products.sql
│   │
│   ├── marts/
│   │   ├── fact_events.sql
│   │   ├── dim_users.sql
│   │   ├── dim_sessions.sql
│   │   └── dim_payers.sql
│   │
│   └── analysis/
│       ├── active_users.sql
│       ├── conversion.sql
│       ├── customers_anl.sql
│       ├── most_purchased_category.sql
│       ├── orders_ans.sql
│       ├── refund_rate.sql
│       ├── retention.sql
│       └── insights.md
│
├── config.py
│   └── Project configuration variables
│
├── main.py
│   └── Pipeline entry point for data loading
│
├── architecture_lineage.mmd
│   └── Data lineage and architecture diagram
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│
└── .gitignore
```


## Data Pipeline Architecture
```
Raw Data
│
├── customers
├── orders
├── product_catalog
└── clickstream_events
        │
        ▼
Python Layer
│
├── split_data.py

└── load_to_bigquery.py
        │
        ▼
BigQuery Staging
│
├── stg_events
├── stg_orders
└── stg_products
        │
        ▼
Data Mart Layer
│
├── fact_events
├── dim_users
├── dim_sessions
└── dim_payers
        │
        ▼
Analytics Layer
│
├── Active Users (DAU / MAU)
├── Conversion Funnel
├── Retention Analysis
├── Refund Analysis
├── Customer Analysis
├── Order Analysis
└── Product Analysis
```

## Technologies
- Python
- Pandas
- SQL
- Google BigQuery
- Tableau