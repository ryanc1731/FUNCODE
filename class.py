import random

# List of people
people = [
    "Lylah", "Faith", "Katelyn", "Chloe","Kaiyah","Caden","Andrea","Christopher","Braylin"," Isabella",
    "Madilynn","Fredrick","Jesus","Gabriele","Hudson"," Joseph","Tessa","Shamariah","Karter","Savannah",
    "Brayden","Micheal","Jose","Austine","Allison","Ke'Airah"
    
]

# Number of groups
num_groups = 8

# Shuffle the list
random.shuffle(people)

# Create the groups
groups = [[] for _ in range(num_groups)]
for i, person in enumerate(people):
    groups[i % num_groups].append(person)

# Print the groups
for i, group in enumerate(groups, start=1):
    print(f"Group {i}: {group}")