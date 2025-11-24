import sqlite3
import math

def distance_km(lat1, lon1, lat2, lon2):
    # Haversine formula
    R = 6371
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = (math.sin(dlat/2)**2 +
         math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) *
         math.sin(dlon/2)**2)
    return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))

def find_on_duty_workers(event_id, db_path="../dailygo.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Get event location
    cur.execute("SELECT lat, lon FROM events WHERE event_id=?", (event_id,))
    ev = cur.fetchone()
    if not ev:
        print("Event not found")
        return []

    ev_lat, ev_lon = ev

    # Fetch workers on duty
    cur.execute("SELECT worker_id, name, lat, lon FROM workers WHERE on_duty=1")
    workers = cur.fetchall()

    nearby = []
    for w in workers:
        wid, name, wlat, wlon = w
        d = distance_km(ev_lat, ev_lon, wlat, wlon)
        if d <= 5:
            nearby.append((wid, name, d))

    conn.close()
    return nearby

def push_notify(worker_id, event_id):
    print(f"Push notification sent to {worker_id} for event {event_id}")

if __name__ == "__main__":
    workers = find_on_duty_workers("E001")
    for w in workers:
        print("Nearby worker:", w)
        push_notify(w[0], "E001")
