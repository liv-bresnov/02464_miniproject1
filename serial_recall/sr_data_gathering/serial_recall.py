import random
import time
import csv

# --- Configure here ---
participant = "YOU_FORGOT_TO_WRITE_YOUR_NAME"   # <--- change this to your name/ID once
experiment_name = "SR"    # <--- change this to your experiment name
csv_filename = f"csv_files/{participant.lower()}.csv"
# ----------------------

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
    time.sleep(5)
    sequence = run_trial()
    recall = input("Please recite the words back (separate with spaces):\n").lower().split()

    # Save both sequence and recall in dictionary
    results[trial_num] = {
        "sequence": sequence,
        "recall": recall
    }


# Save results to CSV
with open(csv_filename, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    if csvfile.tell() == 0:  # write header only if file is new
        writer.writerow(["Name", "Experiment", "Trial", "Sequence", "Recall"])
    for trial, data in results.items():
        writer.writerow([
            participant.lower(),
            experiment_name,
            trial,
            " ".join(data["sequence"]),
            " ".join(data["recall"])
        ])

print(f"\nExperiment complete! Results saved to {csv_filename}.")
