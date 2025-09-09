import random
import time
import nltk

# Download word list (first time only)
nltk.download("words")
from nltk.corpus import words

# Get all 3-letter dictionary words
three_letter_words = [w.lower() for w in words.words() if len(w) == 3]

def run_trial(n=15, interval=1):
    # Pick random 3-letter words without replacement
    trial_words = random.sample(three_letter_words, n)

    print("\nMemorize these words:")
    for word in trial_words:
        print(word)
        time.sleep(interval)  # show each for 'interval' seconds
        print("\033c", end="")  # clear screen (works in most terminals)

    return trial_words

# Run experiment
sequence = run_trial()
print("Now recall the words!")

