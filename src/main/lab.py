import sqlite3

def problem1():
    with open("problem1.sql","r",encoding="utf-8") as f:
        sql=f.read().strip()

    conn=sqlite3.connect(":memory:")
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE song(
        title TEXT,
        artist TEXT
    );
    """)

    cur.execute(sql)
    conn.commit()
    return cur.rowcount>0
