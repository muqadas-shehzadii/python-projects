import random

def treasure_hunt():
    places = ['cave', 'forest', 'lake', 'temple']
    treasures = {
        'cave': ['sword'],
        'forest': ['gold', 'trap'],
        'lake': ['magic ring'],
        'temple': ['ancient coin', 'trap']
    }

    visited = []
    inventory = []

    print("Welcome, explorer! Let's begin your treasure hunt!\n")

    while len(visited) < len(places):
        print("\nPlace you want to explore:", [p for p in places if p not in visited])
        place = input("Enter a place to visit: ").lower()

        if place not in places:
            print("Invalid place. Try again.")
            continue
        if place in visited:
            print("You already visited this place.")
            continue

        visited.append(place)
        print(f"\nYou entered the {place}...")

        found_items = treasures[place]

        for item in found_items:
            if item == "trap":
                if inventory:
                    lost = inventory.pop()
                    print(f"Oh no! A trap! You lost your {lost}.")
                else:
                    print("You found a trap... but had nothing to lose!")
            else:
                inventory.append(item)
                print(f"You found a {item}! Added to inventory.")

        print("Current inventory:", inventory)

    # Final inventory using list comprehension
    final_inventory = [item.upper() for item in inventory]

    print("\n🎉 Adventure complete!")
    print("Visited places:", visited)
    print("Your treasures:", final_inventory)

treasure_hunt()
