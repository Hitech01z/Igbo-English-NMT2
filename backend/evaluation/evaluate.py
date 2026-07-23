import csv

from model.inference import translate

from model.config import DATASET

from evaluation.bleu import compute_bleu

from evaluation.chrf import compute_chrf


references = []

predictions = []


with open(DATASET, encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:

        english = row["english"]

        igbo = row["igbo"]

        prediction = translate(
            english,
            source="english",
            target="igbo",
        )

        references.append(igbo)

        predictions.append(prediction)


bleu = compute_bleu(
    references,
    predictions,
)

chrf = compute_chrf(
    references,
    predictions,
)

print()

print("=" * 40)

print("MODEL EVALUATION")

print("=" * 40)

print(f"BLEU Score : {bleu:.2f}")

print(f"chrF++ Score : {chrf:.2f}")

print("=" * 40)