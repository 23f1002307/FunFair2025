import pandas as pd
import sqlite3

# Connect the database
conn = sqlite3.connect ( "fun_fair.db" )

# Store the query as a variable:
query = "select first_name, last_name, marks, payment_mode, phone from player order by marks desc"

# Convert the extracted data into a pandas dataframe:
df = pd.read_sql_query ( query, conn )

# Converting the dataframe into an excel file and exporting it:
df.to_excel ( "fun_fair_data.xlsx", index = False )

# Close the connection:
conn.close ( )