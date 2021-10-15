#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program

import math


def volume_calculator(radius, height):
    # calculate volume
    volume = radius ** 2 * height * math.pi
    return volume


def main():
    print("Starting ...")
    print("")
    print("This progaram calculates volume of a cylinder")
    print("Please enter the radius and height")
    print("")
    # input
    integer1 = input("The radius is: ")
    integer2 = input("The height is: ")
    try:
        radius_from_user = float(integer1)
        height_from_user = float(integer2)
        if height_from_user < 0 or radius_from_user < 0:
            print("There is no solution")
        else:
            calculated_volume = volume_calculator(radius_from_user, height_from_user)
            print(
                "The volume is cylinder with radius {0}mm and height {1}mm is {2}mm³".format(
                    radius_from_user, height_from_user, calculated_volume
                )
            )

    except Exception:
        print("Please use numbers")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
