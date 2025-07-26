from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Button, Direction
from pybricks.iodevices import XboxController
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the hub
hub = PrimeHub()

#Controller Controls
"""
-- left joystick - angles robot
-- right joystick - up/down -> goes forward/backward slowly, right/left ->
goes faster forward/backward
-- triggers - turns robot
"""
# Initialize motors- *change if necessary
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

# Initialize Xbox controller
controller = XboxController()

# Drive base settings
wheel_diameter = 56 # mm (small spike prime wheels)
axle_track = 120 # mm (Verify this value for your robot's physical dimensions)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True)

# Define a straight drive speed when triggers are pressed
TRIGGER_DRIVE_SPEED = 500 # Adjust as needed

# --- Main loop ---
while True:
    # Read controller input
    left_stick = controller.joystick_left()
    right_stick = controller.joystick_right()
    right_trigger, left_trigger = controller.triggers()

    # Initialize speed and turn rate
    speed_forward = 0
    turn_rate = 0

    # Trigger control for straight movement
    if left_trigger:
        speed_forward = -TRIGGER_DRIVE_SPEED  # Move straight backward
    elif right_trigger:
        speed_forward = TRIGGER_DRIVE_SPEED   # Move straight forward

    # Joystick control for turning and fine movement
    # This will now always be active and can combine with trigger input
    joystick_turn_rate = right_stick[0] * 2  # Scale joystick X-axis for turning
    joystick_speed_forward = left_stick[1] * 10 # Scale joystick Y-axis for forward/backward

    # If triggers are not pressed, use joystick for forward/backward speed
    if not (left_trigger or right_trigger):
        speed_forward = joystick_speed_forward

    # Always apply joystick turn rate
    turn_rate = joystick_turn_rate

    # Ensure speed and turn rate are within limits
    turn_rate = max(-360, min(360, turn_rate)) # Degrees per second for turning
    speed_forward = max(-1000, min(1000, speed_forward)) # Speed for drive

    # Apply drive base commands
    if speed_forward != 0 or turn_rate != 0:
        drive_base.drive(speed_forward, turn_rate)
    else:
        drive_base.stop() # Stop if no input is detected