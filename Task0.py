"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

earliest_text_datetime = None
earliest_record = ()

for record in texts:
    texts_datetime = (record[2]).split()
    date_dmy = texts_datetime[0].split("-")
    # rearrange Day Month Year to make datetime string comparable (YYYY-MM-DD hh:mm:ss) using < operator
    texts_datetime = "{}-{}-{} {}".format(date_dmy[2], date_dmy[1], date_dmy[0], texts_datetime[1])

    if earliest_text_datetime == None or texts_datetime < earliest_text_datetime:
        earliest_text_datetime = texts_datetime
        earliest_record = record

print("First record of texts, {} texts {} at time {}".format(earliest_record[0], earliest_record[1], earliest_record[2]))

latest_call_datetime = None
latest_record = ()

for record in calls:
    calls_datetime = (record[2]).split()
    date_dmy = calls_datetime[0].split("-")
    # rearrange Day Month Year to make datetime string comparable (YYYY-MM-DD hh:mm:ss) using > operator
    calls_datetime = "{}-{}-{} {}".format(date_dmy[2], date_dmy[1], date_dmy[0], calls_datetime[1])  

    if latest_call_datetime == None or calls_datetime > latest_call_datetime:
        latest_call_datetime = calls_datetime
        latest_record = record

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(latest_record[0], latest_record[1], latest_record[2], latest_record[3]))