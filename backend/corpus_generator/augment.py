import csv
from pathlib import Path

from corpus_generator.expansion import ExpansionEngine

INPUT = (
    Path(__file__).parent /
    "output" /
    "raw_dataset.csv"
)

OUTPUT = (
    Path(__file__).parent /
    "output" /
    "augmented_dataset.csv"
)

engine = ExpansionEngine()


rows = []

with open(
    INPUT,
    encoding="utf-8",
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        rows.append(row)

augmented = []

for row in rows:

    augmented.append(row)

    augmented.append(
        engine.expand(row)
    )

with open(
    OUTPUT,
    "w",
    newline="",
    encoding="utf-8",
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "domain",
            "english",
            "igbo",
        ],
    )

    writer.writeheader()

    writer.writerows(augmented)

print(
    f"Saved {len(augmented):,} rows"
)