import sqlite3

def init_db(db_path="../dailygo.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    with open("../data/sample_data.sql", "r") as f:
        sql_script = f.read()
        cur.executescript(sql_script)

    conn.commit()
    conn.close()
    print("Database initialized at", db_path)

if __name__ == "__main__":
    init_db()
