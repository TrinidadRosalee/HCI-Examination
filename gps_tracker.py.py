# gps_tracker.py
# Simple GPS Tracker Simulation

def gps_tracker():
    x, y = 0, 0  # starting point (0,0)
    print("GPS Tracker Started! Starting at (0,0).")
    print("Enter N/S/E/W to move, or STOP to end.\n")

    while True:
        command = input("Move: ").strip().lower()

        if command in ["n", "north"]:
            y += 1
        elif command in ["s", "south"]:
            y -= 1
        elif command in ["e", "east"]:
            x += 1
        elif command in ["w", "west"]:
            x -= 1
        elif command == "stop":
            print("\nSession ended.")
            break
        else:
            print("❌ Invalid input! Use N/S/E/W or STOP.")
            continue

        print(f"📍 Current position: ({x}, {y})")

    print(f"\nFinal position: ({x}, {y})")
    if (x, y) == (0, 0):
        print("✅ You returned to the origin (0,0).")
    else:
        print("❌ You did not return to the origin.")

# Run program
if __name__ == "__main__":
    gps_tracker()
