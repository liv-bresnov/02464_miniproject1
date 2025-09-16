import random
import time
import csv

# Get a frequency-ranked English word list
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']


def run_trial(n=15, interval=1):
    # Pick random letters without replacement
    trial_letters = random.sample(alphabet, n)

    print("\nMemorize these letters:")
    for word in trial_letters:
        print(word)
        time.sleep(interval)  # show each for 'interval' seconds
        print("\033c", end="")  # clear screen

    return trial_letters

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

# CSV file name. COMMENT OUT WHEN DONE OR RENAME
csv_filename = "serial_recall.csv"

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

print("\nExperiment complete! Results saved to", csv_filename)