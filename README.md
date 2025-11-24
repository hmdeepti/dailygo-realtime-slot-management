# dailygo-realtime-slot-management

Real-Time Slot Management System (DailyGo)

Overview
--------
This project contains a simple version of the slot management system we used at DailyGo.
The actual operation required us to handle three things in real time:
1. Track slot fill status for each event.
2. Auto-close events as soon as slots were full.
3. Handle last-minute no-shows by identifying nearby “on-duty” workers.

The on-duty option allowed workers to stay available for any nearby event.
When a no-show happened, event managers could immediately pull workers within a 5 km radius.
This significantly reduced last-minute disruptions.

Components
----------
1. SQL tables for workers, events and assignments.
2. Auto-close script that updates event status based on slot count.
3. On-duty engine that:
   - checks worker’s live status,
   - calculates distance using a simple Haversine function,
   - finds available workers within 5 km,
   - triggers push notifications.

How to run
----------
1. Initialize the database:
   python src/db_setup.py

2. Check auto-close:
   python src/slot_manager.py

3. Find nearby on-duty workers for an event:
   python src/on_duty_engine.py

Notes
-----
- The data in /data is sample data.
- The scripts here are simplified to show the core logic.
- In production we used triggers, cron jobs and Firebase for actual push notifications.
