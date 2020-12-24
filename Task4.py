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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

candidate_marketers = set()
not_marketers = set()

for record in calls:
    # candidate marketer: makes outgoing calls
    candidate_marketers.add(record[0])
    # definitely not marketer: receives calls
    not_marketers.add(record[1])

# exclude texters also
for record in texts:
    not_marketers.add(record[0])
    not_marketers.add(record[1])

marketers = candidate_marketers - not_marketers

print("These numbers could be telemarketers: ")
for marketer in sorted(marketers):
    print(marketer)
