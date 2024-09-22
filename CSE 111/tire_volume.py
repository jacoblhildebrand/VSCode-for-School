import math
from datetime import datetime

def main():
    # Get user input for tire dimensions
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the volume of the tire using the provided formula
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    # Output the result
    print(f"The approximate volume is {volume:.2f} liters")

     # Get the current date (without the time)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Append the tire data to the volumes.txt file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

if __name__ == "__main__":
    main()