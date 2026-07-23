from sacrebleu.metrics import CHRF


metric = CHRF(word_order=2)


def compute_chrf(references, predictions):

    score = metric.corpus_score(
        predictions,
        [references],
    )

    return score.score