import csv
from pathlib import Path

from corpus_generator.grammar import generate_all

OUTPUT = (
    Path(__file__).parent /
    "output" /
    "raw_dataset.csv"
)

OUTPUT.parent.mkdir(
    exist_ok=True
)


def save(rows):

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


def main():

    rows = generate_all(
        size_per_domain=200,
    )

    save(rows)

    print("\n" + "=" * 50)

    print("Dataset Generation Complete")

    print("=" * 50)

    print(f"Sentence pairs : {len(rows):,}")

    print(f"Saved to : {OUTPUT}")


if __name__ == "__main__":

    main()