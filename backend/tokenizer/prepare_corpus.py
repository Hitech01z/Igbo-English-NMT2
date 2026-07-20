import csv
from pathlib import Path

DATASET = (
    Path(__file__).parent.parent
    / "corpus_generator"
    / "output"
    / "final_dataset_clean.csv"
)

OUTPUT = Path(__file__).parent / "training_corpus.txt"

with open(DATASET, encoding="utf-8") as f, \
     open(OUTPUT, "w", encoding="utf-8") as out:

    reader = csv.DictReader(f)

    for row in reader:
        out.write(row["english"] + "\n")
        out.write(row["igbo"] + "\n")

print(f"Saved corpus to {OUTPUT}")