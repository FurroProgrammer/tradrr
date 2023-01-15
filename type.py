import sys
import time

def type(text,ttt):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(ttt)