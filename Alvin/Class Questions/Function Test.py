"""
6.9 (Conversions between feet and meters) Write a module that contains the following
two functions:
# Converts from feet to meters
def footToMeter(foot):
# Converts from meters to feet
def meterToFoot(meter):
The formulas for the conversion are:
foot = meter / 0.305
meter = 0.305 * foot
Write a test program that invokes these functions to display the following tables:
Feet Meters | Meters Feet
1.0 0.305 | 20.0 66.574
2.0 0.610 | 26.0 81.967
...
9.0 2.745 | 60.0 196.721
10.0 3.050 | 66.0 213.115
"""

def footToMeter(foot):
    meter = 0.305 * foot
    print(foot,"feet =",meter,"meters")
def meterToFoot(meter):
    foot  = meter / 0.305
    print(meter,"meters =",foot,"feet")

footToMeter(1)
footToMeter(2)
footToMeter(3)
footToMeter(4)
footToMeter(5)
footToMeter(6)
footToMeter(7)
footToMeter(8)
footToMeter(9)
footToMeter(10)

meterToFoot(20)
meterToFoot(26)
meterToFoot(30)
meterToFoot(36)
meterToFoot(40)
meterToFoot(46)
meterToFoot(50)
meterToFoot(56)
meterToFoot(60)
meterToFoot(66)


