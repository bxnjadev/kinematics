import math

GRAVITATIONAL_CONSTANT = 9.81
GRAVITATIONAL_CONSTANT_VECTOR = -GRAVITATIONAL_CONSTANT

initial_position_x = float(input("initial position x: "))
initial_position_y = float(input("initial position y: "))

initial_velocity_x = float(input("initial velocity x: "))
initial_velocity_y = float(input("initial velocity y "))

h_max = (- (initial_velocity_y**2) + 2 * GRAVITATIONAL_CONSTANT_VECTOR * initial_position_y) \
        / 2 * GRAVITATIONAL_CONSTANT_VECTOR

velocity_angle = math.atan2(initial_velocity_x, initial_velocity_y)

print("H max : ", h_max)
print("Velocity Angle", math.degrees(velocity_angle))

