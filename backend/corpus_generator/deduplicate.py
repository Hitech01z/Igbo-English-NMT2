import csv
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = (
    BASE_DIR
    / "output"
    / "raw_dataset.csv"
)

OUTPUT_FILE = (
    BASE_DIR
    / "output"
    / "final_dataset.csv"
)


# ============================================================
# LOAD DATASET
# ============================================================

def load_dataset():

    rows = []

    with open(

        INPUT_FILE,

        encoding="utf-8",

        newline="",

    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            domain = row["domain"].strip()

            english = row["english"].strip()

            igbo = row["igbo"].strip()


            if not english or not igbo:

                continue


            rows.append({

                "domain": domain,

                "english": english,

                "igbo": igbo,

            })


    return rows


# ============================================================
# REMOVE EXACT DUPLICATE PAIRS
# ============================================================

def remove_duplicates(rows):

    seen = set()

    clean_rows = []


    for row in rows:

        key = (

            row["english"].strip().lower(),

            row["igbo"].strip().lower(),

        )


        if key in seen:

            continue


        seen.add(key)

        clean_rows.append(row)


    return clean_rows


# ============================================================
# SAVE FINAL DATASET
# ============================================================

def save_dataset(rows):

    OUTPUT_FILE.parent.mkdir(

        parents=True,

        exist_ok=True,

    )


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


# ============================================================
# MAIN
# ============================================================

def main():

    print(

        "Loading raw dataset..."

    )


    rows = load_dataset()


    print(

        f"Loaded rows: {len(rows)}"

    )


    rows = remove_duplicates(rows)


    print(

        f"Final clean rows: {len(rows)}"

    )


    save_dataset(rows)


    print()

    print(

        "Final dataset created successfully."

    )


    print(

        f"Saved to: {OUTPUT_FILE}"

    )


if __name__ == "__main__":

    main()