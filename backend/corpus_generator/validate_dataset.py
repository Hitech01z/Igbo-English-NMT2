import csv
from pathlib import Path

DATASET = (
    Path(__file__).parent /
    "output" /
    "final_dataset_clean.csv"
)

rows = 0
problems = 0

with open(
    DATASET,
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        rows += 1

        if (
            not row["english"].strip()
            or
            not row["igbo"].strip()
        ):
            problems += 1

print("=" * 50)
print("Dataset Validation")
print("=" * 50)
print(f"Rows: {rows:,}")
print(f"Problems: {problems:,}")

if problems == 0:
    print("Dataset validation passed.")
else:
    print("Dataset contains invalid rows.")