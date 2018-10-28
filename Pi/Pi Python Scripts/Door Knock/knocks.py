#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
sound = 18


GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)

def callback(sound):
        if GPIO.input(sound):
                print "Knock Detected!"
		knocks++;
	
	if knocks >= 4:
		print "door unlocked"
	
GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)