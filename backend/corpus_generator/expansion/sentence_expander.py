import csv

from pathlib import Path

from .expansion_rules import EXPANSION_RULES


BASE_DIR = Path(__file__).parent.parent

INPUT_FILE = (
    BASE_DIR
    / "output"
    / "raw_dataset.csv"
)

OUTPUT_FILE = (
    BASE_DIR
    / "output"
    / "expanded_dataset.csv"
)


def normalize(text):

    return " ".join(
        text.strip().split()
    )


def expand_dataset():

    rows = []


    # =====================================================
    # LOAD ORIGINAL VERIFIED DATASET
    # =====================================================

    with open(

        INPUT_FILE,

        encoding="utf-8",

        newline="",

    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            rows.append({

                "domain":
                normalize(
                    row["domain"]
                ),

                "english":
                normalize(
                    row["english"]
                ),

                "igbo":
                normalize(
                    row["igbo"]
                ),

            })


    original_count = len(rows)


    # =====================================================
    # ADD CONTROLLED VARIANTS
    # =====================================================

    for rule in EXPANSION_RULES:

        rows.append({

            "domain":
            rule["domain"],

            "english":
            rule["base_english"],

            "igbo":
            rule["base_igbo"],

        })


        for (

            english,

            igbo,

        ) in rule["variants"]:

            rows.append({

                "domain":
                rule["domain"],

                "english":
                english,

                "igbo":
                igbo,

            })


    # =====================================================
    # DEDUPLICATE
    # =====================================================

    unique = {}

    for row in rows:

        key = (

            row["english"].lower(),

            row["igbo"].lower(),

        )


        if key not in unique:

            unique[key] = row


    rows = list(
        unique.values()
    )


    # =====================================================
    # SAVE
    # =====================================================

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8",

        newline="",

    ) as file:

        writer = csv.DictWriter(

            file,

            fieldnames=[

                "domain",

                "english",

                "igbo",

            ],

        )


        writer.writeheader()

        writer.writerows(rows)


    print()

    print(
        "Controlled expansion completed."
    )

    print(

        f"Original rows: "
        f"{original_count}"

    )

    print(

        f"Final rows: "
        f"{len(rows)}"

    )

    print(

        f"Added rows: "
        f"{len(rows) - original_count}"

    )

    print()

    print(

        f"Saved to: "
        f"{OUTPUT_FILE}"

    )


if __name__ == "__main__":

    expand_dataset()