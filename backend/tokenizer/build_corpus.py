import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATASET = (
    BASE_DIR
    / "corpus_generator"
    / "output"
    / "final_dataset.csv"
)

OUTPUT = BASE_DIR / "tokenizer" / "training_corpus.txt"


with open(
    DATASET,
    encoding="utf-8",
    newline="",
) as file:

    reader = csv.DictReader(file)

    sentences = []

    for row in reader:

        english = row["english"].strip()
        igbo = row["igbo"].strip()

        sentences.append(
            f"<en2ig> {english}"
        )

        sentences.append(
            f"<ig2en> {igbo}"
        )


with open(
    OUTPUT,
    "w",
    encoding="utf-8",
) as file:

    for sentence in sentences:

        file.write(
            sentence
            + "\n"
        )


print(
    "Tokenizer corpus created successfully."
)

print(
    f"Total sentences: {len(sentences)}"
)

print(
    f"Saved to: {OUTPUT}"
)