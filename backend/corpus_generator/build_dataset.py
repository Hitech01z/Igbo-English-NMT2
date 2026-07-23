import csv
from pathlib import Path


BASE_DIR = Path(__file__).parent


SOURCE_DATA_DIR = (
    BASE_DIR
    / "source_data"
)


RESOURCES_DIR = (
    BASE_DIR
    / "resources"
)


OUTPUT_DIR = (
    BASE_DIR
    / "output"
)


OUTPUT_FILE = (
    OUTPUT_DIR
    / "raw_dataset.csv"
)


def load_csv_file(source_file):

    rows = []


    print(

        f"Loading: {source_file}"

    )


    with open(

        source_file,

        encoding="utf-8",

        newline="",

    ) as file:


        reader = csv.DictReader(file)


        required_columns = {

            "domain",

            "english",

            "igbo",

        }


        if not required_columns.issubset(

            reader.fieldnames or []

        ):

            raise ValueError(

                f"{source_file.name} "

                "must contain columns: "

                "domain, english, igbo"

            )


        for row in reader:


            domain = (

                row["domain"]

                .strip()

            )


            english = (

                row["english"]

                .strip()

            )


            igbo = (

                row["igbo"]

                .strip()

            )


            if not english or not igbo:

                continue


            rows.append({

                "domain": domain,

                "english": english,

                "igbo": igbo,

            })


    return rows


def load_all_datasets():

    rows = []


    # ==================================================
    # 1. LOAD ORIGINAL BASE DATASET
    # ==================================================

    base_dataset = (

        SOURCE_DATA_DIR

        / "base_dataset.csv"

    )


    if base_dataset.exists():

        rows.extend(

            load_csv_file(

                base_dataset

            )

        )


    else:

        print(

            "WARNING: "

            "base_dataset.csv not found."

        )


    # ==================================================
    # 2. LOAD ALL DOMAIN DATASETS
    # ==================================================

    resource_files = sorted(

        RESOURCES_DIR.glob(

            "*.csv"

        )

    )


    for resource_file in resource_files:


        rows.extend(

            load_csv_file(

                resource_file

            )

        )


    return rows


def remove_duplicates(rows):


    seen = set()


    clean_rows = []


    for row in rows:


        key = (

            row["english"]

            .lower()

            .strip(),

            row["igbo"]

            .lower()

            .strip(),

        )


        if key in seen:

            continue


        seen.add(key)


        clean_rows.append(row)


    return clean_rows


def save_dataset(rows):


    OUTPUT_DIR.mkdir(

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


def main():


    print(

        "Loading all dataset sources..."

    )


    rows = (

        load_all_datasets()

    )


    print(

        f"Total loaded rows: "

        f"{len(rows)}"

    )


    rows = (

        remove_duplicates(

            rows

        )

    )


    print(

        f"After deduplication: "

        f"{len(rows)}"

    )


    save_dataset(rows)


    print()


    print(

        "Dataset generation completed."

    )


    print(

        f"Saved to: "

        f"{OUTPUT_FILE}"

    )


if __name__ == "__main__":


    main()