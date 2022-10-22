def solve():
  x = (x1+x2)**2
  y = (y1+y2)**2 
  Z = (x+y)**0.5 
  return Z
print("Find distance between any two point:")
x1 = float(input('Enter a value of x1:\n'))
x2 = float(input('Enter a value of x2:\n'))
y1 = float(input('Enter a value of y1:\n'))
y2 = float(input('Enter a value of y2:\n'))
print("The distance between two point is", solve())