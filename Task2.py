"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_on_phone_per_number = dict()
for record in calls:
    # for both outgoing calls (index 0) and incoming calls (index 1)
    for i in range(2):
        if record[i] not in time_on_phone_per_number:
            # insert current record's number (key) and duration (value) to new dict entry
            time_on_phone_per_number[record[i]] = record[3]
        else:
            # if number already in time_on_phone_per_number dict add current record's time to existing value
            time_on_phone_per_number[record[i]] = int(time_on_phone_per_number[record[i]]) + int(record[3])

busiest_number = None
longest_duration_seconds = None    

for number in time_on_phone_per_number.keys():
    # found new record holder?
    if longest_duration_seconds is None or int(time_on_phone_per_number[number]) > int(longest_duration_seconds):
        busiest_number = number
        longest_duration_seconds = time_on_phone_per_number[number]

print("{} spent the longest time, {} seconds, on the phone during September 2016."
    .format(busiest_number, longest_duration_seconds))