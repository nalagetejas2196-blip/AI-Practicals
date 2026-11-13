def vacuum_cleaner():
    rooms = {
        'A': input("Enter status of Room A (Clean/Dirty): ").strip().capitalize(),
        'B': input("Enter status of Room B (Clean/Dirty): ").strip().capitalize()
    }

    location = input("Enter starting location (A/B): ").strip().upper()

    if location not in rooms or any(v not in ("Clean", "Dirty") for v in rooms.values()):
        print("Invalid input")
        return

    while True:
        if rooms[location] == "Dirty":
            print("Room", location, "is Dirty. Cleaning...")
            rooms[location] = "Clean"
        else:
            print("Room", location, "is Clean.")

        if all(status == "Clean" for status in rooms.values()):
            break

        location = "B" if location == "A" else "A"

    print("Final Room Status:", rooms)


vacuum_cleaner()
