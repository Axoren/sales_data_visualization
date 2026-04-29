# Sales Performance Analysis and Visualization

This project analyzes sales performance across product lines, countries, and time periods using order-level sales data.

The goal is to identify revenue drivers, seasonality, pricing patterns, and product performance insights for business decision-making.

## Business Problem

A sales or commercial team needs to understand what drives revenue and where performance differs across products and markets.

The key questions:

1. Which product lines generate the highest revenue?
2. Which countries contribute the most to sales?
3. Are there monthly patterns or seasonality?
4. Which product lines have the highest average unit price?
5. Is revenue mainly driven by order volume or price?

## Dataset

Source: Kaggle Sample Sales Data.

Main fields used:

| Field | Description |
|---|---|
| ORDERDATE | Order date |
| PRODUCTLINE | Product category |
| SALES | Order revenue |
| QUANTITYORDERED | Number of units ordered |
| PRICEEACH | Unit price |
| COUNTRY | Customer country |
| CUSTOMERNAME | Customer name |

## Methodology

The analysis follows this workflow:

1. Load order-level sales data.
2. Clean and format date fields.
3. Aggregate revenue by product line, country, and month.
4. Compare product categories by total revenue and average unit price.
5. Analyze monthly sales trend and seasonality.
6. Check the relationship between quantity ordered and revenue.
7. Convert findings into commercial recommendations.

## Metrics

Total sales:

```text
total_sales = sum(sales)
```

Average unit price:

```text
average_unit_price = average(price_each)
```

Monthly sales:

```text
monthly_sales = sum(sales) grouped by order_month
```

Product line revenue share:

```text
revenue_share = product_line_sales / total_sales
```

## Visualizations and Insights

### Total Sales by Product Line

Classic Cars and Motorcycles are the top-performing categories by revenue.

![Sales by Product Line](screenshots/productline_sales.png)

### Sales by Product Line and Country

Sales vary by geography. Classic Cars dominate in several top-performing countries.

![Sales by Country](screenshots/sales_by_country.png)

### Monthly Sales Trend

December peaks indicate possible seasonal demand and holiday-driven sales cycles.

![Monthly Sales](screenshots/monthly_sales.png)

### Average Unit Price by Product Line

Planes and Ships have the highest average unit prices, which may affect revenue mix and margin strategy.

![Average Unit Price](screenshots/avg_unit_price.png)

### Quantity Ordered vs Sales

Revenue generally increases with order quantity, but outliers suggest that product mix and unit price also matter.

![Quantity vs Sales](screenshots/quantity_vs_sales.png)

## Key Findings

1. Revenue is concentrated in a few product lines.
2. Country-level performance differs by product category.
3. Sales show monthly peaks that should be checked against seasonality and campaign calendars.
4. Average unit price varies strongly by product line.
5. Revenue is not explained by quantity alone. Product mix also matters.

## Business Recommendations

1. Prioritize top-performing product lines in planning and inventory decisions.
2. Review December demand separately from normal monthly performance.
3. Analyze product line performance by country before scaling campaigns.
4. Separate volume-driven growth from price-driven growth.
5. Add margin data to move from sales analysis to profit analysis.

## Limitations

- The dataset does not include marketing spend, margin, discounts, or inventory constraints.
- Revenue is analyzed, but profit is not available.
- Seasonality is observed visually and should be validated with more years of data.
- Country-level results may be affected by sample size differences.
- Customer-level retention is not part of the current version.

## Next Steps

Planned improvements:

- add SQL version of revenue aggregation,
- calculate revenue share by country and product line,
- add customer repeat purchase analysis,
- add margin simulation if cost data is unavailable,
- create a Tableau dashboard version.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
