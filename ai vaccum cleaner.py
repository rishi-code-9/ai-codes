
# Simple Reflex Agent for Vacuum Cleaner World

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"


# Initial environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

print("Initial Environment:", environment)
print("Starting Location:", location)

# Agent execution
for step in range(10):

    status = environment[location]

    action = vacuum_agent(location, status)

    print("\nStep:", step + 1)
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    if action == "Suck":
        environment[location] = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"

    print("Environment:", environment)

    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("\nBoth rooms are Clean!")
        print("Goal Achieved.")
        break
