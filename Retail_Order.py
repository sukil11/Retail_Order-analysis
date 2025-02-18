import streamlit as st
import pymysql
import pandas as pd
mydb = pymysql.connect(
            host='127.0.0.1',
            user="root",
            password='sukil',
            database="retail_orders",
            autocommit=True
        )
mycursor = mydb.cursor()
#st.success("Connected to the database successfully!")

st.title("RETAIL_ORDERS")
st.header("GIVEN QUERIES:")

mycursor.execute('use retail_orders')

if st.button("1"):
     st.markdown(" Find top 10 highest revenue generating products:")
     mycursor.execute('''SELECT table_05.product_id, SUM(table_05.sale_price * table_05.quantity) AS revenue
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_05.product_id
ORDER BY revenue DESC
LIMIT 10;
''')
     st.table(mycursor)
if st.button("2"):
     st.markdown("Find the top 5 cities with the highest profit margins:")
     mycursor.execute('''SELECT table_0.city, SUM(table_05.profit) AS total_profit
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.city
ORDER BY total_profit DESC
LIMIT 5;
''')
     st.table(mycursor)

if st.button("3"):
     st.markdown("Calculate the total discount given for each category:")
     mycursor.execute('''SELECT table_0.category, SUM(table_05.discount) AS total_discount
FROM table_0
JOIN table_05 ON table_0.order_id =table_05.order_id
GROUP BY table_0.category;
''' )
     st.table(mycursor)

if st.button("4"):
     st.markdown("Find the average sale price per product category:")
     mycursor.execute('''SELECTtable_0.category, AVG(table_05.sale_price) AS avg_sale_price
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category;
''' )
     st.table(mycursor)

if st.button("5"):
     st.markdown("Find the region with the highest average sale price:")
     mycursor.execute('''SELECT table_0.region, AVG(table_05.sale_price) AS avg_sale_price
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.region
ORDER BY avg_sale_price DESC
LIMIT 1;
''')
     st.table(mycursor)

if st.button("6"):
     st.markdown("Find the total profit per category:")
     mycursor.execute('''SELECT table_0.category, SUM(table_05.profit) AS total_profit
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category;
''' )
     st.table(mycursor)

if st.button("7"):
     st.markdown(" Identify the top 3 segments with the highest quantity of orders:")
     mycursor.execute('''SELECT table_05.segment, SUM(table_05.quantity) AS total_quantity
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_05.segment
ORDER BY total_quantity DESC
LIMIT 3;
 ''')
     st.table(mycursor)

if st.button("8"):
     st.markdown("Determine the average discount percentage given per region:")
     mycursor.execute('''SELECTtable_0.region, AVG(table_05.discount_percent) AS avg_discount_percent
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.region;
'''  )
     st.table(mycursor)

if st.button("9"):
     st.markdown("Find the product category with the highest total profit:")
     mycursor.execute('''SELECT table_0.category, SUM(table_05.profit) AS total_profit
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category
ORDER BY total_profit DESC
LIMIT 1;
 ''' )
     st.table(mycursor)

if st.button("10"):
     st.markdown("Calculate the total revenue generated per year:")
     mycursor.execute('''SELECT YEAR(table_0.order_date) AS year, 
       SUM(table_05.sale_price * table_05.quantity) AS total_revenue
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY YEAR(table_0.order_date)
''')
     st.table(mycursor)

st.header("MY OWN GIVEN QUERIES:")

if st.button("11"):
     st.markdown("Find the top 5 lowest revenue generating products:")
     mycursor.execute('''SELECT table_05.product_id, SUM(table_05.sale_price * table_05.quantity) AS revenue
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_05.product_id
ORDER BY revenue ASC
LIMIT 5;
 ''' )
     st.table(mycursor)

if st.button("12"):
     st.markdown("Find the top 5 cities with the lowest profit margins:")
     mycursor.execute('''
        SELECT table_0.city, SUM(table_05.profit) AS total_profit
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.city
ORDER BY total_profit ASC
LIMIT 5;
   '''  )
     st.table(mycursor)

if st.button("13"):
     st.markdown("Calculate the total discount given for each category:")
     mycursor.execute('''
        SELECT table_0.category, SUM(table_05.discount) AS total_discount
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category;
  '''   )
     st.table(mycursor)

if st.button("14"):
     st.markdown("Find the average sale price per product category:")
     mycursor.execute('''
        SELECT table_0.category, AVG(table_05.sale_price) AS avg_sale_price
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category;
''')
     st.table(mycursor)

if st.button("15"):
     st.markdown("Find the region with the lowest average sale price:")
     mycursor.execute('''
        SELECT table_0.region, AVG(table_05.sale_price) AS avg_sale_price
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.region
ORDER BY avg_sale_price ASC
LIMIT 1;
''')
     st.table(mycursor)

if st.button("16"):
     st.markdown(" Find the total profit for each category:")
     mycursor.execute('''
        SELECT table_0.category, SUM(table_05.profit) AS total_profit
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category;
'''  )
     st.table(mycursor)

if st.button("17"):
     st.markdown("Identify the top 5 segments with the lowest quantity of orders:")
     mycursor.execute('''
        SELECT table_05.segment, SUM(table_05.quantity) AS total_quantity
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_05.segment
ORDER BY total_quantity ASC
LIMIT 5;
''' )
     st.table(mycursor)

if st.button("18"):
     st.markdown("Determine the average discount percentage given for total revenue:")
     mycursor.execute('''
        SELECT SUM(table_05.sale_price * table_05.quantity) AS total_revenue,
       AVG(table_05.discount_percent) AS avg_discount_percent
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id;
''' )
     st.table(mycursor)

if st.button("19"):
     st.markdown("Find the product category with the lowest total profit:")
     mycursor.execute('''
        SELECT table_0.category, SUM(table_05.profit) AS total_profit
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.category
ORDER BY total_profit ASC
LIMIT 1;
''' )
     st.table(mycursor)

if st.button("20"):
     st.markdown(" Calculate the total revenue generated per day:")
     mycursor.execute('''SELECT table_0.order_date, SUM(table_05.sale_price * table_05.quantity) AS total_revenue
FROM table_0
JOIN table_05 ON table_0.order_id = table_05.order_id
GROUP BY table_0.order_date
ORDER BY table_0.order_date;
''' )
     st.table(mycursor)


