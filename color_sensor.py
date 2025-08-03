from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
hub = PrimeHub()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)
left_color_sensor = ColorSensor(Port.E)
right_color_sensor = ColorSensor(Port.F)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=120)
drive_base.use_gyro(True)
drive_speed = 100 #good for line following200

#start of code
print("starting program")
while True:
    current_left_color = left_color_sensor.color()
    current_right_color = right_color_sensor.color()
    print(current_left_color, current_right_color)
    if current_left_color == Color.RED or current_right_color == Color.RED:
        drive_base.stop()
        break
    drive_base.drive(drive_speed, 0) #not straight method since goes for specific distance not forever
    wait(20)
print("program finished")
