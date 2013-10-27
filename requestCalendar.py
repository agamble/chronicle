import requests
from database import *

d = DatabaseManager()

r = requests.get('http://www.ucl.ac.uk/timetable/ics/spxipmlh28sgtpd')

event_array = []
inside_block = False
index = 0

print r.text

for line in r.text:
	if line is "BEGIN:VEVENT":
		inside_block = True
		event_array.append = []
		index += 1
		continue
	if line is "END:VEVENT":
		inside_block = False
	if inside_block == True:
		event.array[index].append(line)

print event_array



