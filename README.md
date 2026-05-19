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
- 5% drop from view to cart
- 4% of users purchase without add_to_cart
- for further analyis go to [Insight analysis](analysis/Insights.md)