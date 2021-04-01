
#program - 1
def area(radius):
  area = 3.14 * radius * radius
  return area
circleRadius = 5
circleArea = area(circleRadius)

#program - 2
import os

file = os.path.splitext('my_file.txt')
file_extension = file[1]
print("File Extension: ", file_extension)
