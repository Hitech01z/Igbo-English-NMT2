from evaluation.evaluate import (
    bleu,
    chrf,
)


def get_metrics():

    return {

        "bleu": round(bleu, 2),

        "chrf": round(chrf, 2),

    }