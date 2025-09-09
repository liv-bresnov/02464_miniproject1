import time
import random

animals = [
    "Elephant", "Dog", "Cat", "Lion", "Tiger", "Giraffe", "Zebra",
    "Kangaroo", "Panda", "Monkey", "Bear", "Rabbit", "Horse", "Fox"
]

# Pick 10 random animals (no repeats)
chosen_animals = random.sample(animals, 10)

for animal in chosen_animals:
    print(animal)
    time.sleep(1)  # wait 1 second before showing the next one