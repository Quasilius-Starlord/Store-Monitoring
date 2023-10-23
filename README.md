Python Django framework and sqlite3 database.

# Steps 1
Run following commands in terminal to install necessary packages:
- pip install psycopg2
- pip install djangorestframework
- pip install markdown       # Markdown support for the browsable API.
- pip install django-filter  # Filtering support

The csv containing poll data of every store has to be placed in `/api/csv_data/storeStatus.csv` with recommended file name.
with schema of `store_id,status,timestamp_utc`.(Above is done so github doesnt let file of large size be uploaded)

# Step 2
Make migrations
- python manage.py makemigrations
- python manage.py migrate

# Step 3
Run server
- python manage.py runserver

# Send necessary HTTP requests to trigger resport
- GET Request
- url http://localhost:8000/store/{STORE_ID}/trigger_report/
- header 'Content-Type: application/json'

# Send necessary HTTP requests to download CSV of report
- POST request
- url http://localhost:8000/store/get_report/
- header 'Content-Type: application/json'
- data - '{
	"report_id": {REPORT_ID GENERATED IN PREVIOUS STEP AS INTEGER}
}'



# Step by step logic for last one day (uptime and downtime):
- Initialize a dictionary last_one_day_data with keys "uptime...", "downtime...". The values for "uptime..." and "downtime..." are set to 0.

- Calculate one_day_ago as the day of the week one day before the current_day. If current_day is 0 (Monday), set one_day_ago to 6 (Sunday).
- Check if the store is open during the last one day (one_day_ago to current_day) at the current time (current_time). 
- This is done by querying the store.timings to see if there is any entry that matches the conditions for day and time.
- If the store is not open during the last one day, return the initialized last_one_day_data.
- If the store is open during the last one day, query the store.status_logs to get all the logs within the last one day (utc_time - 1 day to utc_time) and order them by timestamp.
- Loop through each log in last_one_day_logs:
- Check if the log's timestamp falls within the store's business hours on that day (log_in_store_business_hours). This is done by querying the store.timings to see if there is any entry that matches the conditions for day and time.
- If the log is not within the store's business hours, skip it and move to the next log.
- If the log's status is "active", increment the "uptime..." value in last_one_day_data by 1.
- If the log's status is not "active", increment the "downtime..." value in last_one_day_data by 1.
- Same logic has been followed for last one hour and last one week uptime and downtime.