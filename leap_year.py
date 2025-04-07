#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program check if a year is a leap year
def main():
    try:
        year_leap = int(input("Enter a year: "))

        if year_leap % 4 == 0:
            if year_leap % 100 == 0:
                if year_leap % 400 == 0:
                    print("It’s a leap year!")
                else:
                    print("It’s not a leap year!")
            else:
                print("It’s a leap year!")
        else:
            print("It’s not a leap year!")

    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    main()
