from typing import Iterator

import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    print("connection to redshift made")

    return connect



def extract_transactional_data(dbname,host,port,user,password):
    # extracts data from redshift
    # join the description 2 table
    # remove invoices where customerid is blank
    # remove invoices where stock code is in Bank charges,post etc
    # converts the invoice date to a datetime field
    # creates a variable called total order value
    # replace missing description with unknown

    connect = connect_to_redshift(dbname, host, port, user, password)

    query = """
    SELECT ot.invoice, 
        ot.stock_code,
        CASE WHEN sd.description IS NULL THEN 'Unknown'
            ELSE sd.description END AS description,
        ot.quantity,
        ot.price,
         /*add a variable that gives the total order_value*/
        ot.price*ot.quantity as total_order_value,
        CAST(invoice_date As DateTime) AS invoice_date,
        ot.customer_id,
        ot.country
    FROM bootcamp.online_transactions ot
    /* this is a subquery that removes '?' from the stock_description table */
    LEFT JOIN ( SELECT *
            FROM bootcamp.stock_description
            WHERE description <> '?') AS sd ON ot.stock_code = sd.stock_code
    WHERE ot.customer_id <> ''
    AND ot.stock_code NOT IN ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
    """
    online_trans_cleaned =pd.read_sql(query,connect)
    print(online_trans_cleaned.shape)
    print(online_trans_cleaned.head())

    return online_trans_cleaned




