import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#%matplotlib inline

db = 'chinook.db'

def run_query(query_str):
    with sqlite3.connect(db) as conn:
        return pd.read_sql(query_str, conn)

def run_command(c):
    with sqlite3.connect(db) as conn:
        conn.isolation_level = None
        conn.execute(c)

def show_tables():
    #方式一
    q = '''
    SELECT
        name,
        type
    FROM sqlite_master
    WHERE type IN ("table","view");
    '''

    #方式二
    q1 = '''
        select *
        from sqlite_master
        '''

    return run_query(q)

# df = show_tables()
# print(df)

#全球销售数据 & 各个分配占比
def get_genre_sold_infor():
    q = '''
    WITH whole_sold_infor AS
    (
    SELECT 
        g.genre_id AS genre_id,
        g.name AS genre_name,
        COUNT(t.track_id) AS trace_count,
        (SELECT COUNT(*) FROM invoice_line) AS total_count,
        ROUND(CAST(COUNT(t.track_id) AS float) / (SELECT COUNT(*) FROM invoice_line), 4) AS percentage
    FROM invoice_line AS ii
    LEFT JOIN invoice AS iv ON iv.invoice_id == ii.invoice_id
    LEFT JOIN track AS t ON t.track_id == ii.track_id
    LEFT JOIN genre AS g ON g.genre_id == t.genre_id
    GROUP BY g.genre_id
    )

    SELECT * FROM whole_sold_infor
    '''
    return run_query(q)

#获取美国消费者销售统计数据
def get_usa_sold_infor():
    q = '''
    WITH usa_sold_infor AS
    (
     SELECT
      il.*
     FROM invoice_line as il
     LEFT JOIN invoice AS i ON i.invoice_id == il.invoice_id
     LEFT JOIN customer AS c ON i.customer_id == c.customer_id
     WHERE c.country == 'USA' 
     ),
     usa_persentage AS
     (
      SELECT 
          g.genre_id AS genre_id,
          g.name AS genre_name,
          COUNT(t.track_id) AS track_sold,
          ROUND(CAST(COUNT(t.track_id) AS float) / (SELECT COUNT(*) FROM usa_sold_infor), 4) AS persentage
      FROM usa_sold_infor AS u
      LEFT JOIN track AS t ON t.track_id == u.track_id
      LEFT JOIN genre AS g ON g.genre_id == t.genre_id
      GROUP BY g.genre_id
      ORDER BY track_sold DESC
     )
    
    SELECT * FROM usa_persentage
    '''

    return run_query(q)

#柱状图显示各个genre的比例
def show_usa_sold_infor():
    df = get_usa_sold_infor()

    df.set_index("genre_name", inplace=True, drop=True)
    #使用bar -- 表示垂直的柱状图
    #使用barh -- 表示水平方向的柱状图
    df["track_sold"].plot.bar(title="Top Selling Genres in the USA", xlim=(0, 650))
    # plt.ylabel('y label')

    for i, label in enumerate(list(df.index)):
        print(label)
        score = df.loc[label, "track_sold"]
        label = (df.loc[label, "persentage"] * 100
                 ).astype(int).astype(str) + "%"
        #第一个参数 -- 表示标签的string，例如“xx”，则“xx”显示在图标上
        #第二个参数 -- 表示标签显示的xy坐标位置
        plt.annotate(str(label), (i - 0.15, score + 10))

    plt.show()

def show_usa_sold_infor_v():
    df = get_usa_sold_infor()
    #inplace = True -- 表示原地修改，可以直接使用df。如果为False则需要使用返回的新df。默认False
    #drop=True -- 表示用新index后，删除之前的column。默认为True
    df.set_index('genre_name', inplace=True, drop=True)
    df['track_sold'].plot.bar(title="Top Selling Genres in the USA", ylim=(0, 650))

    #不设置Y轴标签
    plt.ylabel('')

    for i, label in enumerate((list(df.index))):
        score = df.loc[label, 'track_sold']
        tip = (df.loc[label, 'persentage'] * 100).astype(int).astype(str) + '%'

        plt.annotate(str(tip), (i - 0.2, score + 10))

    plt.show()

show_usa_sold_infor_v()