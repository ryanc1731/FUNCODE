import random

# List of people
people = [
    "Joshua", "Courtney", "Reignan", "Zaidan","Luke","Rian","Isaiah","Harmony","Zayla"," Allyssa",
    "William","Christopher","Jonathon","Kaylie","Blake","Brooke","Addison","Zana","Brian","Kendrum",
    "Jayson","Jeffrey","Maiya"
    
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
