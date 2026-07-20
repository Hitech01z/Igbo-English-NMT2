import csv
from pathlib import Path

INPUT = (
    Path(__file__).parent /
    "output" /
    "augmented_dataset.csv"
)

OUTPUT = (
    Path(__file__).parent /
    "output" /
    "final_dataset_clean.csv"
)

seen = set()

rows = []

with open(
    INPUT,
    encoding="utf-8",
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        key = (
            row["english"].strip().lower(),
            row["igbo"].strip().lower(),
        )

        if key not in seen:

            seen.add(key)

            rows.append(row)

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

    writer.writerows(rows)

print(
    f"Final rows : {len(rows):,}"
)