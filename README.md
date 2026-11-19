Shopify Store Sales Analysis

This project analyzes Shopify store orders and creates sales reports.

Project Structure:
shopify-sales-analysis/
- data/shopify_orders.csv
- src/analysis.py
- charts/ (output charts)
- requirements.txt
- README.md

How to Run:
pip install -r requirements.txt
python src/analysis.py

What it does:
- Calculates total sales, total delivered orders, average order value
- Finds monthly sales trend
- Finds top selling products
- Generates 2 charts in charts folder.

Wireless Earbuds is the top performing product with 21 units sold, followed by Men-s T-Shirt.

September 2024 recorded highest sales of ∼50,000 Rs, while July was lowest. 
This shows strong growth after July.

Tech used: Python, Pandas, Matplotlib
