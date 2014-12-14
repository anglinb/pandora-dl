#producer.py
import time

with open('exampleoutput.txt', "r") as code:
	for line in code:
		print(line)
		time.sleep(.01)