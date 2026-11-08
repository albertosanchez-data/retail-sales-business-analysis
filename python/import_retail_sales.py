import csv
import getpass
import psycopg

CSV_PATH = r"D:\ANALISIS DE DATOS CURSO\VIDEOS\EXCELL\Retail_Sales_Data.csv"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "RetailSalesAnalysis",
    "user": "postgres"
}

EXPECTED_HEADERS = [
    "Order_ID", "Order_Date", "Customer_ID", "Customer_Name",
    "City", "Region", "Salesperson", "Product_ID", "Product_Name",
    "Category", "Quantity", "Unit_Price_MXN", "Unit_Cost_MXN",
    "Discount_Rate", "Payment_Method", "Sales_Channel",
    "Order_Status", "Net_Sales_MXN", "Total_Cost_MXN",
    "Gross_Profit_MXN", "Gross_Margin_Pct", "Discount_Amount_MXN",
    "Gross_Sales_MXN", "Sales_Reconciliation_Check",
    "Profitability_Status"
]

password = getpass.getpass("PostgreSQL password: ")

with open(CSV_PATH, "r", encoding="cp1252", newline="") as file:
    reader = csv.reader(file)
    headers = next(reader)

    if headers != EXPECTED_HEADERS:
        raise ValueError("CSV headers do not match the expected structure.")

    with psycopg.connect(**DB_CONFIG, password=password) as conn:
        with conn.cursor() as cur:

            cur.execute("SELECT COUNT(*) FROM public.stg_retail_sales")
            existing_rows = cur.fetchone()[0]

            if existing_rows != 0:
                raise ValueError("Target table is not empty. Import cancelled.")

            with cur.copy(
                "COPY public.stg_retail_sales FROM STDIN"
            ) as copy:

                imported_rows = 0

                for row in reader:
                    if len(row) != 25:
                        raise ValueError("Invalid row: expected 25 columns.")

                    copy.write_row([value if value != "" else None for value in row])
                    imported_rows += 1

print(f"Import completed: {imported_rows} rows.")