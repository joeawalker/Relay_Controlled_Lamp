import RPi.GPIO as GPIO
import time
import sys

#Assigns channel to use on Raspberry Pi
channel = 21

#Turns warnings off
GPIO.setwarnings(False) 

#Flashes lamp on and off
def flash():
    flashes = 5
    delay = 0.5
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    for x in range (0,flashes):
        GPIO.output(channel, GPIO.HIGH)
        print("FLASH")
        time.sleep(delay)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(delay)

#Turns lamp on
def on():
    print("ON")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.HIGH)

#Turns lamp off
def off():
    print("OFF")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)

#Timer that flashes lamp once complete
def timer():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)

    choice = input("1: Seconds\n2: Minutes\n")

    if str(choice) == "1":
        secs = input("Seconds: ")
        secs = int(secs)

    elif str(choice) == "2":
        secs = input("Minutes: ")
        secs = int(secs)
        secs = secs * 60

    for x in range(secs,0,-1):
        print(x)
        time.sleep(1)
    for x in range (0,6):
        GPIO.output(channel, GPIO.HIGH)
        print("BEEP")
        time.sleep(0.3)
        GPIO.output(channel, GPIO.LOW)
        time.sleep(0.3)

#Menu to enter commands
def menu():
    print("~~Menu~~")
    while True:
        sel = raw_input("")
        if sel == "on":
            on()
        elif sel == "off":
            off()
        elif sel == "flash":
            flash()
        elif sel == "timer":
            timer()
        elif sel == "exit":
            sys.exit()

menu()

GPIO.cleanup() 
