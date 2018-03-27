import pandas as pd
import sqlite3


conn = sqlite3.connect("chinook.db")

query = "select * from track limit 5"
result = pd.read_sql_query(query, conn)

print(result[:])
