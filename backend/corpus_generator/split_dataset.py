import csv
import random
from pathlib import Path

INPUT = (
    Path(__file__).parent /
    "output" /
    "final_dataset_clean.csv"
)

OUTPUT = (
    Path(__file__).parent /
    "output"
)

rows = []

with open(
    INPUT,
    encoding="utf-8",
) as f:

    reader = csv.DictReader(f)

    for row in reader:
        rows.append(row)

random.shuffle(rows)

n = len(rows)

train = rows[: int(0.8 * n)]
valid = rows[int(0.8 * n): int(0.9 * n)]
test = rows[int(0.9 * n):]

for name, data in [
    ("train.csv", train),
    ("valid.csv", valid),
    ("test.csv", test),
]:

    with open(
        OUTPUT / name,
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
        writer.writerows(data)

print("=" * 50)
print("Dataset Split Complete")
print("=" * 50)
print(f"Train : {len(train):,}")
print(f"Valid : {len(valid):,}")
print(f"Test  : {len(test):,}")