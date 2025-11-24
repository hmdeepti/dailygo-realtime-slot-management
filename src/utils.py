def mark_on_duty(worker_id, db_path="../dailygo.db"):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("UPDATE workers SET on_duty=1 WHERE worker_id=?", (worker_id,))
    conn.commit()
    conn.close()
    print(f"Worker {worker_id} set to ON DUTY")
