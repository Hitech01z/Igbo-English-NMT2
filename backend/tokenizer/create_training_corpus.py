import csv
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


DATASET = (
    BASE_DIR
    / "corpus_generator"
    / "output"
    / "raw_dataset.csv"
)


OUTPUT_FILE = (
    Path(__file__).resolve().parent
    / "training_corpus.txt"
)


# ============================================================
# CREATE TRAINING CORPUS
# ============================================================

def create_training_corpus():

    sentences = []

    print(
        "Loading dataset..."
    )

    with open(

        DATASET,

        encoding="utf-8",

        newline="",

    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            english = (

                row["english"]

                .strip()

            )


            igbo = (

                row["igbo"]

                .strip()

            )


            if english:

                sentences.append(

                    english

                )


            if igbo:

                sentences.append(

                    igbo

                )


    # ========================================================
    # REMOVE DUPLICATE SENTENCES
    # ========================================================

    sentences = list(

        dict.fromkeys(

            sentences

        )

    )


    # ========================================================
    # SAVE CORPUS
    # ========================================================

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8",

    ) as file:

        for sentence in sentences:

            file.write(

                sentence

                + "\n"

            )


    print()

    print(

        "Tokenizer corpus created successfully."

    )

    print(

        f"Unique sentences: {len(sentences)}"

    )

    print(

        f"Saved to: {OUTPUT_FILE}"

    )


if __name__ == "__main__":

    create_training_corpus()