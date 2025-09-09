import random
import time
from wordfreq import top_n_list

# Get a frequency-ranked English word list
word_list = top_n_list("en", 1000)

# Keep only 3-letter words (already filtered to common words)
three_letter_words = [w for w in word_list if len(w) == 3]

def run_trial(n=15, interval=1):
    # Pick random 3-letter words without replacement
    trial_words = random.sample(three_letter_words, n)

    print("\nMemorize these words:")
    for word in trial_words:
        print(word)
        time.sleep(interval)  # show each for 'interval' seconds
        print("\033c", end="")  # clear screen

    return trial_words

# Run experiment
sequence = run_trial()
print("Now recall the words!")


# Mangler at gemme original sequence og vores gæt.
