color = input("Enter traffic light color (Red, Yellow, Green): ").strip().lower()

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Get Ready!")
elif color == "green":
    print("Go!")
else:
    print("Invalid traffic light color.")

