import random
import time

# Get a frequency-ranked English word list
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

def run_trial(n=15, interval=1):
    # Pick random 3-letter words without replacement
    trial_letters = random.sample(alphabet, n)

    print("\nMemorize these letters:")
    for word in trial_letters:
        print(word)
        time.sleep(interval)  # show each for 'interval' seconds
        print("\033c", end="")  # clear screen

    return trial_letters

# Run experiment
sequence = run_trial()
print("Now recall the letters!")

# Step 5: Ask for recall
recall = input("Please recite the letters back (separate with spaces):\n")