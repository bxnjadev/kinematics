import math
import cuadratic_math
import math_helper

GRAVITATIONAL_CONSTANT = 9.81
GRAVITATIONAL_CONSTANT_VECTOR = -GRAVITATIONAL_CONSTANT

initial_position_y = float(input("initial position y: "))
final_position_y = float(input("final position y: "))

initial_velocity_x = float(input("initial velocity x: "))
initial_velocity_y = float(input("initial velocity y "))

h_max = (- (initial_velocity_y ** 2) + (2 * GRAVITATIONAL_CONSTANT_VECTOR) * initial_position_y) \
        / 2 * GRAVITATIONAL_CONSTANT_VECTOR

velocity_angle = math.atan2(initial_velocity_x, initial_velocity_y)

final_times = cuadratic_math.equation_square(GRAVITATIONAL_CONSTANT_VECTOR / 2, - initial_velocity_y,
                                             (final_position_y - initial_position_y))

final_time = math_helper.get_positive_value(final_times)

print("H max : ", h_max)
print("Velocity Angle", math.degrees(velocity_angle))
print("Final Time ", final_time)

