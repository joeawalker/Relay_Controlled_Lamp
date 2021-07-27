# Relay Controlled Lamp
<br>

## **Code**

On the Raspberry Pi save this python script to a preferred location and enable SSH in the settings

```
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
```

<br>

## **Wiring**

Using a 5 volt relay switch
1. Connect the Ground pin to GPIO 6 (Ground)
2. Connect the 5V VCC pin to GPIO 2 (5V power)
3. Connect the Signal pin to GPIO 21 (PCM_DOUT)

<p align="center">
  <img width="460" height="270" src="https://github.com/joeawalker/Relay_Controlled_Lamp/blob/main/Images/Relay%20Diagram.png">
</p>

Carefully expose the wire on the lamp and cut through it to split it. Once that is done connect the side closes to the plug into NC and the other side into C.

<p align="center">
  <img width="460" height="470" src="https://github.com/joeawalker/Relay_Controlled_Lamp/blob/main/Images/Relay.jpg">
</p>

The final wiring can be seen here:

![test](https://github.com/joeawalker/Relay_Controlled_Lamp/blob/main/Images/Raspberry%20Pi.jpg)

<br>

## **Remote Controlling**
You will first need your Raspberry Pi IP address:

On your local machine (Windows) open command prompt and type in `ipconfig` to get your ip address. Enter this into a browser and select 'Network Devices'. You will find your Raspberry Pi ip address there.

Switch back to the command prompt and enter `ssh pi@xxx.xxx.x.xxx` with the x's being your ip address. You will then be prompted to enter the password which by default is 'raspberry'.

Next navigate to the directory of the python script that was saved earlier and run `python script.py`. This will now run the program and present you with the menu allowing you to run the commands:
1. on
2. off
3. flash
4. timer
5. exit

<p align="center">
  <img src="https://github.com/joeawalker/Relay_Controlled_Lamp/blob/main/Images/cmd.JPG">
</p>


<br>

## **Demonstration**

https://user-images.githubusercontent.com/55537303/127207399-943bbbd1-88f5-4202-9825-a29d10b1cafc.mp4



