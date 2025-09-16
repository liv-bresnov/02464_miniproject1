import random
import time
from wordfreq import top_n_list
import csv


# Get a large list of common words (e.g., top 50k)
words = top_n_list("en", 50000)

# Filter to 3-letter alphabetic words only
filtered_words = [w for w in words if len(w) == 3 and w.isalpha()]

# Take the top 500 of those
three_letter_words = filtered_words[:500]


def run_trial(n=15, interval=1):
    # Pick random 3-letter words without replacement
    trial_words = random.sample(three_letter_words, n)

    print("\nMemorize these words:")
    for word in trial_words:
        print(word)
        time.sleep(interval)  # show each for 'interval' seconds
        print("\033c", end="")  # clear screen

    return trial_words

# Dictionary to store results
results = {}

# Run 20 trials
for trial_num in range(1, 21):
    print(f"\n--- Trial {trial_num} ---")
    sequence = run_trial()
    recall = input("Please recite the words back (separate with spaces):\n").lower().split()

    # Save both sequence and recall in dictionary
    results[trial_num] = {
        "sequence": sequence,
        "recall": recall
    }

# CSV file name
csv_filename = "recall_chunking.csv"

# Save results to CSV
with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Trial", "Sequence", "Recall"])  # header row
    
    for trial, data in results.items():
        writer.writerow([
            trial,
            " ".join(data["sequence"]),  # join list into a single string
            " ".join(data["recall"])
        ])

print("\nExperiment complete! Results saved to 'experiment_results.csv'")
