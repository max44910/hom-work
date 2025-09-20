import math

def calculate_circumference(radius):
  """
  Calculates the circumference of a circle given its radius.
  """
  return 2 * math.pi * radius

circle_radius = 5
circumference_result = calculate_circumference(circle_radius)
print(circumference_result)
