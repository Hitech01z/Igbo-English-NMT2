import csv
from pathlib import Path

DATASET = (
    Path(__file__).parent /
    "output" /
    "final_dataset_clean.csv"
)

english_vocab = set()
igbo_vocab = set()

pairs = 0

with open(
    DATASET,
    encoding="utf-8",
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        pairs += 1

        english_vocab.update(
            row["english"].split()
        )

        igbo_vocab.update(
            row["igbo"].split()
        )

print("=" * 50)
print("Vocabulary Report")
print("=" * 50)
print(f"Sentence pairs : {pairs:,}")
print(f"English vocab  : {len(english_vocab):,}")
print(f"Igbo vocab     : {len(igbo_vocab):,}")