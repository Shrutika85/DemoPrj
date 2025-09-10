# Python Demo Code (~50 lines)

import math
import json

# A simple class for geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


# A function to save data in JSON file
def save_to_file(data, filename="shapes.json"):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print("Error while saving:", e)


# Main program
if __name__ == "__main__":
    circles = [Circle(r) for r in range(1, 6)]  # List of Circle objects

    # Use list comprehension to prepare summary
    summary = [
        {"radius": c.radius, "area": c.area(), "perimeter": c.perimeter()}
        for c in circles
    ]

    # Print data nicely
    print("Circle Details:")
    for item in summary:
        print(f"Radius: {item['radius']}, Area: {item['area']}, Perimeter: {item['perimeter']}")

   

    # Read back from file and print
    with open("shapes.json", "r") as f:
        data = json.load(f)
        print("\nData loaded from file:")
        for d in data:
            print(d)
