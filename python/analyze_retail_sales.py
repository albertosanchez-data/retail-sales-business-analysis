
import getpass
from pathlib import Path

import pandas as pd
import psycopg2


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "RetailSalesAnalysis",
    "user": "postgres"
}


def main():

    try:
        print("Connecting to PostgreSQL...")

        password = getpass.getpass("PostgreSQL password: ")

        conn = psycopg2.connect(
            **DB_CONFIG,
            password=password
        )

        print("Database connection successful.\n")

        # --------------------------------------------------
        # LOAD DELIVERED SALES DATA
        # --------------------------------------------------

        query = """
            SELECT *
            FROM public.vw_retail_sales_delivered;
        """

        with conn.cursor() as cur:
            cur.execute(query)

            records = cur.fetchall()
            columns = [description[0] for description in cur.description]

        conn.close()

        df = pd.DataFrame(records, columns=columns)

        df["order_date"] = pd.to_datetime(df["order_date"])

        numeric_columns = [
            "quantity",
            "unit_price_mxn",
            "unit_cost_mxn",
            "discount_rate",
            "net_sales_mxn",
            "total_cost_mxn",
            "gross_profit_mxn",
            "gross_margin_pct",
            "discount_amount_mxn",
            "gross_sales_mxn"
        ]

        for column in numeric_columns:
            df[column] = pd.to_numeric(df[column])

        # --------------------------------------------------
        # DATASET OVERVIEW
        # --------------------------------------------------

        print("DATASET OVERVIEW")
        print("-------------------------")
        print(f"Total records: {len(df)}")
        print(f"Total columns: {len(df.columns)}")

        print("\nFIRST 5 RECORDS")
        print("-------------------------")
        print(df.head().to_string(index=False))

        print("\nDATA TYPES")
        print("-------------------------")
        print(df.dtypes.to_string())

        # --------------------------------------------------
        # GENERAL KPIs
        # --------------------------------------------------

        total_orders = df["order_id"].nunique()
        total_units = df["quantity"].sum()
        gross_sales = df["gross_sales_mxn"].sum()
        total_discounts = df["discount_amount_mxn"].sum()
        net_sales = df["net_sales_mxn"].sum()
        total_cost = df["total_cost_mxn"].sum()
        gross_profit = df["gross_profit_mxn"].sum()
        gross_margin = (gross_profit / net_sales) * 100

        print("\nGENERAL BUSINESS KPIs")
        print("-------------------------")
        print(f"Delivered orders: {total_orders}")
        print(f"Units sold: {total_units}")
        print(f"Gross sales: {gross_sales:,.2f}")
        print(f"Discounts: {total_discounts:,.2f}")
        print(f"Net sales: {net_sales:,.2f}")
        print(f"Total cost: {total_cost:,.2f}")
        print(f"Gross profit: {gross_profit:,.2f}")
        print(f"Gross margin: {gross_margin:.2f}%")

        # --------------------------------------------------
        # SALES PERFORMANCE BY CATEGORY
        # --------------------------------------------------

        category_analysis = (
            df.groupby("category")
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
        )

        category_analysis["gross_margin_pct"] = (
            category_analysis["gross_profit"]
            / category_analysis["net_sales"] * 100
        )

        category_analysis = category_analysis.sort_values(
            "net_sales", ascending=False
        )

        print("\nSALES PERFORMANCE BY CATEGORY")
        print("-------------------------")
        print(category_analysis.to_string(index=False))

        # --------------------------------------------------
        # SALES PERFORMANCE BY REGION
        # --------------------------------------------------

        region_analysis = (
            df.groupby("region")
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
        )

        region_analysis["gross_margin_pct"] = (
            region_analysis["gross_profit"]
            / region_analysis["net_sales"] * 100
        )

        region_analysis = region_analysis.sort_values(
            "net_sales", ascending=False
        )

        print("\nSALES PERFORMANCE BY REGION")
        print("-------------------------")
        print(region_analysis.to_string(index=False))

        # --------------------------------------------------
        # MONTHLY SALES PERFORMANCE
        # --------------------------------------------------

        df["month"] = df["order_date"].dt.to_period("M").astype(str)

        monthly_analysis = (
            df.groupby("month")
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
        )

        monthly_analysis["gross_margin_pct"] = (
            monthly_analysis["gross_profit"]
            / monthly_analysis["net_sales"] * 100
        )

        monthly_analysis = monthly_analysis.sort_values("month")

        print("\nMONTHLY SALES PERFORMANCE")
        print("-------------------------")
        print(monthly_analysis.to_string(index=False))

        # --------------------------------------------------
        # SALES PERFORMANCE BY CHANNEL
        # --------------------------------------------------

        channel_analysis = (
            df.groupby("sales_channel")
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
        )

        channel_analysis["gross_margin_pct"] = (
            channel_analysis["gross_profit"]
            / channel_analysis["net_sales"] * 100
        )

        channel_analysis = channel_analysis.sort_values(
            "net_sales", ascending=False
        )

        print("\nSALES PERFORMANCE BY CHANNEL")
        print("-------------------------")
        print(channel_analysis.to_string(index=False))

        # --------------------------------------------------
        # SALES PERFORMANCE BY SALESPERSON
        # --------------------------------------------------

        salesperson_analysis = (
            df.groupby("salesperson")
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
        )

        salesperson_analysis["gross_margin_pct"] = (
            salesperson_analysis["gross_profit"]
            / salesperson_analysis["net_sales"] * 100
        )

        salesperson_analysis["average_order_value"] = (
            salesperson_analysis["net_sales"]
            / salesperson_analysis["orders"]
        )

        salesperson_analysis = salesperson_analysis.sort_values(
            "net_sales", ascending=False
        )

        print("\nSALES PERFORMANCE BY SALESPERSON")
        print("-------------------------")
        print(salesperson_analysis.to_string(index=False))

        # --------------------------------------------------
        # SALES PERFORMANCE BY PRODUCT
        # --------------------------------------------------

        product_analysis = (
            df.groupby(["product_id", "product_name", "category"])
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
        )

        product_analysis["gross_margin_pct"] = (
            product_analysis["gross_profit"]
            / product_analysis["net_sales"] * 100
        )

        product_analysis = product_analysis.sort_values(
            "net_sales", ascending=False
        )

        print("\nSALES PERFORMANCE BY PRODUCT")
        print("-------------------------")
        print(product_analysis.to_string(index=False))

        # --------------------------------------------------
        # TOP 10 CUSTOMERS
        # --------------------------------------------------

        top_10_customers = (
            df.groupby(["customer_id", "customer_name", "city", "region"])
            .agg(
                orders=("order_id", "nunique"),
                units_sold=("quantity", "sum"),
                net_sales=("net_sales_mxn", "sum"),
                gross_profit=("gross_profit_mxn", "sum")
            )
            .reset_index()
            .sort_values("net_sales", ascending=False)
            .head(10)
        )

        top_10_customers["gross_margin_pct"] = (
            top_10_customers["gross_profit"]
            / top_10_customers["net_sales"] * 100
        )

        print("\nTOP 10 CUSTOMERS")
        print("-------------------------")
        print(top_10_customers.to_string(index=False))

        # --------------------------------------------------
        # CUSTOMER RETENTION ANALYSIS
        # --------------------------------------------------

        customer_orders = (
            df.groupby("customer_id")["order_id"]
            .nunique()
        )

        total_customers = len(customer_orders)

        one_time_customers = int(
            (customer_orders == 1).sum()
        )

        repeat_customers = int(
            (customer_orders > 1).sum()
        )

        repeat_customer_rate = (
            repeat_customers / total_customers * 100
        )

        max_orders_per_customer = int(
            customer_orders.max()
        )

        print("\nCUSTOMER RETENTION")
        print("-------------------------")
        print(f"Total customers: {total_customers}")
        print(f"One-time customers: {one_time_customers}")
        print(f"Repeat customers: {repeat_customers}")
        print(f"Repeat customer rate: {repeat_customer_rate:.2f}%")
        print(f"Maximum orders per customer: {max_orders_per_customer}")

        # --------------------------------------------------
        # EXPORT REPORTS
        # --------------------------------------------------

        output_dir = Path(__file__).resolve().parent.parent / "outputs"
        output_dir.mkdir(parents=True, exist_ok=True)

        kpi_summary = pd.DataFrame([{
            "total_orders": total_orders,
            "total_units": total_units,
            "gross_sales_mxn": gross_sales,
            "total_discounts_mxn": total_discounts,
            "net_sales_mxn": net_sales,
            "total_cost_mxn": total_cost,
            "gross_profit_mxn": gross_profit,
            "gross_margin_pct": gross_margin
        }])

        retention_summary = pd.DataFrame([{
            "total_customers": total_customers,
            "one_time_customers": one_time_customers,
            "repeat_customers": repeat_customers,
            "repeat_customer_rate_pct": repeat_customer_rate,
            "max_orders_per_customer": max_orders_per_customer
        }])

        reports = {
            "delivered_sales_data.csv": df,
            "kpi_summary.csv": kpi_summary,
            "sales_by_category.csv": category_analysis,
            "sales_by_region.csv": region_analysis,
            "monthly_sales.csv": monthly_analysis,
            "sales_by_channel.csv": channel_analysis,
            "sales_by_salesperson.csv": salesperson_analysis,
            "sales_by_product.csv": product_analysis,
            "top_10_customers.csv": top_10_customers,
            "customer_retention.csv": retention_summary
        }

        for filename, report_df in reports.items():
            report_df.to_csv(
                output_dir / filename,
                index=False,
                encoding="utf-8-sig"
            )

        print("\nREPORT FILES EXPORTED")
        print("-------------------------")
        print(f"Files generated: {len(reports)}")
        print(f"Output directory: {output_dir}")

        print("\nANALYSIS COMPLETED SUCCESSFULLY")


    except Exception as error:
        print("\nERROR DURING ANALYSIS")
        print("-------------------------")
        print(error)


if __name__ == "__main__":
    main()
