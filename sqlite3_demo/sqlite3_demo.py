import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

#Normal usage
query_maj = "select major from recent_grads"
cursor.execute(query_maj)
majors = cursor.fetchall()
print(majors[0:3])

#excute & fetchmany()
query = "select Major, Major_category from recent_grads"
five_results = cursor.execute(query).fetchmany(5)

#close connection with sqlite db
conn.close()