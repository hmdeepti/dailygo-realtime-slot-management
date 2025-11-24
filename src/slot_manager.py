import sqlite3

def auto_close_events(db_path="../dailygo.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        UPDATE events
        SET status = 'closed'
        WHERE filled_slots >= total_slots AND status = 'open';
    """)

    conn.commit()
    conn.close()
    print("Auto close check completed.")
