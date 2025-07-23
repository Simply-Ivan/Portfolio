
import sqlite3 as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    createDB