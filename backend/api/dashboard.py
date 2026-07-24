import csv

from fastapi import APIRouter

from model.config import DATASET


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


def dashboard_stats():

    rows = []

    with open(
        DATASET,
        encoding="utf-8",
    ) as f:

        reader = csv.DictReader(f)

        rows = list(reader)


    english_words = set()

    igbo_words = set()


    for row in rows:

        english_words.update(

            row["english"].split()

        )

        igbo_words.update(

            row["igbo"].split()

        )


    return {

        "dataset_size": len(rows),

        "vocabulary_size":

            len(english_words)

            + len(igbo_words),

        "domains": 10,

        "total_translations": len(rows),

        "language_distribution": {

            "English": len(rows),

            "Igbo": len(rows),

        }

    }


@router.get("/stats")
def get_dashboard_stats():

    return dashboard_stats()