from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#fyi
#red_end is attach_c_motor, - values go down
#white_end is attach_d_motor, + values go down
# -values=straight, +values=backwards 
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A)
attach_c_motor = Motor(Port.C)
attach_d_motor = Motor(Port.D)
colorsensor = ColorSensor(Port.E)
colorsensor2 = ColorSensor(Port.F)
hub = PrimeHub()
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=120)
drive_base.use_gyro(True)
drive_base.settings(500,300,500,300)
#start of code
drive_base.straight(-760)
wait(100)
drive_base.turn(-90)
drive_base.straight(-195)
drive_base.straight(50)
attach_d_motor.run_angle(300, 200)
drive_base.straight(-20)
attach_d_motor.run_angle(150,-150)
drive_base.straight(380)
drive_base.turn(90)
drive_base.straight(-55)
attach_d_motor.run_angle(310, 300)
drive_base.turn(15)
drive_base.straight(50)
attach_d_motor.run_angle(310,-300)
drive_base.straight(-25)
attach_d_motor.run_angle(310,350)
attach_d_motor.run_angle(300,-200)
drive_base.straight(150)
drive_base.turn(30)
drive_base.straight(500)