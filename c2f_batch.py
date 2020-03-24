import sys
#  get temperature on command line

# convert temperature string to a float number

# convert C to F

#  print out C, F

celsius_raw = sys.argv[1]

# print("raw celsius is", celsius_raw)

celsius = float(celsius_raw)

fahrenheit = ((9 * celsius) / 5) + 32

print("{}\u00B0 C is {}\u00B0 F".format(celsius, fahrenheit))

