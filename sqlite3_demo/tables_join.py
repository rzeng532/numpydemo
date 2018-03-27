import pandas as pd
import sqlite3

conn = sqlite3.connect("factbook.db")

query_3 = "SELECT f.name as country,\
            c.urban_pop,\
            f.population as total_pop,\
            (CAST(c.urban_pop AS FLOAT) / CAST(f.population AS FLOAT)) as urban_pct\
          FROM facts as f\
          INNER JOIN (\
            SELECT\
            facts_id, SUM(population) as urban_pop\
            FROM cities\
            GROUP BY facts_id\
          ) as c on c.facts_id == f.id\
          WHERE (urban_pct > 0.5)\
          ORDER BY urban_pct"

result = pd.read_sql_query(query_3, conn)
print(result[:])