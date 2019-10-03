#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program does if, else if, else, and endif statements


def main():

    integer = int(input("Enter integer: "))

    if integer > 0:
        print("+")
    elif integer < 0:
        print("-")
    elif integer == 0:
        print("0")
    else:
        print("No idea")


if __name__ == "__main__":
    main()
