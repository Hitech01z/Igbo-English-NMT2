from sacrebleu.metrics import BLEU


bleu = BLEU()


def compute_bleu(references, predictions):

    score = bleu.corpus_score(
        predictions,
        [references],
    )

    return score.score