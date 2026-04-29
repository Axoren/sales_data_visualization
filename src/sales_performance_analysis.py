"""Sales performance analysis pipeline.

This script loads order-level sales data, calculates commercial metrics,
creates aggregated summaries, and saves outputs for reporting.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


DATA_PATH = Path("sales_data_sample.csv")
OUTPUT_DIR = Path("outputs")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load order-level sales data."""
    return pd.read_csv(path, encoding="ISO-8859-1")


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich sales data."""
    clean_df = df.copy()
    clean_df.columns = clean_df.columns.str.strip()

    clean_df["ORDERDATE"] = pd.to_datetime(clean_df["ORDERDATE"])
    clean_df["order_month"] = clean_df["ORDERDATE"].dt.to_period("M").dt.to_timestamp()
    clean_df["order_year"] = clean_df["ORDERDATE"].dt.year

    return clean_df


def summarize_by_product_line(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate sales metrics by product line."""
    summary = (
        df.groupby("PRODUCTLINE")
        .agg(
            orders=("ORDERNUMBER", "nunique"),
            total_sales=("SALES", "sum"),
            total_quantity=("QUANTITYORDERED", "sum"),
            avg_unit_price=("PRICEEACH", "mean"),
            avg_order_sales=("SALES", "mean"),
        )
        .reset_index()
    )

    total_sales = summary["total_sales"].sum()
    summary["sales_share"] = summary["total_sales"] / total_sales

    return summary.sort_values("total_sales", ascending=False)


def summarize_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate sales metrics by country."""
    summary = (
        df.groupby("COUNTRY")
        .agg(
            customers=("CUSTOMERNAME", "nunique"),
            orders=("ORDERNUMBER", "nunique"),
            total_sales=("SALES", "sum"),
            avg_order_sales=("SALES", "mean"),
        )
        .reset_index()
    )

    total_sales = summary["total_sales"].sum()
    summary["sales_share"] = summary["total_sales"] / total_sales

    return summary.sort_values("total_sales", ascending=False)


def summarize_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate monthly sales trend."""
    return (
        df.groupby("order_month")
        .agg(
            orders=("ORDERNUMBER", "nunique"),
            total_sales=("SALES", "sum"),
            total_quantity=("QUANTITYORDERED", "sum"),
            customers=("CUSTOMERNAME", "nunique"),
        )
        .reset_index()
        .sort_values("order_month")
    )


def save_outputs(
    product_summary: pd.DataFrame,
    country_summary: pd.DataFrame,
    monthly_summary: pd.DataFrame,
) -> None:
    """Save aggregated outputs for reporting."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    product_summary.to_csv(OUTPUT_DIR / "product_line_summary.csv", index=False)
    country_summary.to_csv(OUTPUT_DIR / "country_summary.csv", index=False)
    monthly_summary.to_csv(OUTPUT_DIR / "monthly_sales_summary.csv", index=False)


def print_summary(product_summary: pd.DataFrame, country_summary: pd.DataFrame) -> None:
    """Print concise business summary."""
    print("Sales Performance Summary")
    print("=" * 80)
    print("Top product lines by sales")
    print(product_summary.head(5).to_string(index=False, float_format=lambda x: f"{x:.2f}"))
    print("\nTop countries by sales")
    print(country_summary.head(5).to_string(index=False, float_format=lambda x: f"{x:.2f}"))


def main() -> None:
    """Run the sales performance analysis pipeline."""
    raw_df = load_data()
    clean_df = clean_sales_data(raw_df)

    product_summary = summarize_by_product_line(clean_df)
    country_summary = summarize_by_country(clean_df)
    monthly_summary = summarize_by_month(clean_df)

    save_outputs(product_summary, country_summary, monthly_summary)
    print_summary(product_summary, country_summary)


if __name__ == "__main__":
    main()
