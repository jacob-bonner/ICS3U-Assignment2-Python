#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can calculate the volume of a sphere


import math


def main():
    # This function calculates the volume of a sphere

    # Input
    radius = int(input("Enter the radius of your sphere here (cm): "))

    # Process
    volume = 4/3*math.pi*radius**3

    # Output
    print("")
    print("The volume of your sphere is {}cm^3".format(round(volume, 2)))


if __name__ == "__main__":
    main()
