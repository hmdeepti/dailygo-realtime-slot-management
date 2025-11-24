-- Workers table
CREATE TABLE workers (
    worker_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(15),
    rating FLOAT,
    lat FLOAT,
    lon FLOAT,
    on_duty BOOLEAN DEFAULT FALSE
);

-- Events table
CREATE TABLE events (
    event_id VARCHAR(10) PRIMARY KEY,
    event_name VARCHAR(100),
    lat FLOAT,
    lon FLOAT,
    total_slots INT,
    filled_slots INT,
    event_time TIMESTAMP,
    status VARCHAR(20)
);

-- Assignments table
CREATE TABLE assignments (
    assign_id SERIAL PRIMARY KEY,
    event_id VARCHAR(10),
    worker_id VARCHAR(10),
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample workers
INSERT INTO workers VALUES
('W101','Ravi','9998887776',4.5,12.9716,77.5946, FALSE),
('W102','Suresh','9998887771',4.2,12.9600,77.6200, FALSE),
('W103','Arun','9998887773',4.8,12.9550,77.6100, TRUE),
('W104','Vishal','9998887700',3.9,12.9900,77.5800, TRUE);

-- Sample events
INSERT INTO events VALUES
('E001','Corporate Event',12.9750,77.5990,50,48,'2025-07-12 09:00','open'),
('E002','Mall Promotion',12.9450,77.6100,30,30,'2025-07-12 11:00','closed');

