import os
import time
import random

animals = [
    "Elephant", "Dog", "Cat", "Lion", "Tiger", "Giraffe", "Zebra",
    "Kangaroo", "Panda", "Monkey", "Bear", "Rabbit", "Horse", "Fox"
]

# How long before clearing the screen (in seconds)
clear_delay = 5  

# Step 1: Pick animals
chosen_animals = random.sample(animals, 10)

# Step 2: Show them one by one
for animal in chosen_animals:
    print(animal)
    time.sleep(1)  # Time between showing animals

# Step 3: Wait before clearing
print(f"\nScreen will clear in {clear_delay} seconds...")
time.sleep(clear_delay)

# Clear the screen
os.system("cls" if os.name == "nt" else "clear")

# Step 4: Wait before recall
wait_time = 5
print(f"Now wait {wait_time} seconds before recalling the animals...\n")
time.sleep(wait_time)

# Step 5: Ask for recall
recall = input("Please recite the animals back (separate with spaces):\n")

# Step 6: Process recall
user_animals = recall.split()

# Normalize to lowercase for comparison
chosen_set = set(a.lower() for a in chosen_animals)
user_set = set(a.lower() for a in user_animals)

# Score = number of correct animals recalled (order doesn't matter)
score = len(chosen_set & user_set)

print("\nCorrect animals were:")
print(chosen_animals)

print("\nYou recalled:")
print(user_animals)

print(f"\nYour score: {score} / {len(chosen_animals)}")
