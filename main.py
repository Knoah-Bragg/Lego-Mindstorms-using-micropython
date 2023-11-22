#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize Objects
ev3 = EV3Brick()
# Write your program here.
ev3.speaker.beep()

medium_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S4) 
color_sensor = ColorSensor(Port.S1)  
timer = StopWatch() 
timeToWait = 5000
speed = 2000
detect = 0

# Start the timer
timer.reset()
timer.resume()  

ev3.screen.draw_text(0, 0, "Counting")

# Wait timeToWait milliseconds
while timer.time() < timeToWait:
    # Check if the touch sensor was pressed
    if touch_sensor.pressed() == True:  
        # Increment the counter and play sound
        ev3.speaker.play_file(SoundFile.CONFIRM)
        detect += 1
    # Check if the color sensor is detecting black
    elif color_sensor.color() == Color.BLACK or color_sensor.color() == Color.BROWN:  
        # Increment the counter and play sound
        ev3.speaker.play_file(SoundFile.CONFIRM)
        detect += 1

# Reset the timer
timer.pause()
timer.reset()

# Processing text
ev3.screen.draw_text(0, 0, "Processing")
ev3.screen.draw_text(0, 0, "Done")
ev3.screen.clear()

# Make the motor run at a specified speed and degrees *HAS TO BE "run_angle()" not "run_target()"
for degrees in range(detect):
    medium_motor.run_angle(speed, 360, then=Stop.HOLD, wait=True)