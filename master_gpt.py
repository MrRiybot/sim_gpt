from random import randint, choice

# Function to generate a random name
def generate_name():
    first_names = ["Alex", "Jamie", "Jordan", "Taylor", "Morgan", "Casey", "Avery", "Riley", "Quinn", "Dakota"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    return f"{choice(first_names)} {choice(last_names)}"

# Function to generate a random age between 18 and 70
def generate_age():
    return randint(18, 70)

# Generate world description with families, their members, and details
def generate_world_description():
    world_description = "In this world, there are 10 families each with unique characteristics. Here are the families:\n\n"
    for i in range(1, 11):
        family_name = generate_name().split()[1]  # Use the generated last name as the family name
        member_count = randint(1, 4)  # Each family has 1-4 members
        world_description += f"Family {i} (The {family_name}s):\n"
        for j in range(member_count):
            member_name = generate_name()
            member_age = generate_age()
            world_description += f"- {member_name}, {member_age} years old\n"
        world_description += "\n"
    return world_description

# Generate and print the world description
world_description = generate_world_description()
world_description
