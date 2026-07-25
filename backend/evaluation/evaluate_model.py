import csv
import random

import torch
import sentencepiece as spm
import sacrebleu

from model.transformer import Transformer

from model.config import (
    DATASET,
    TOKENIZER,
    CHECKPOINT_DIR,
    DEVICE,
    MAX_LENGTH,
    BOS_IDX,
    EOS_IDX,
    PAD_IDX,
)


# ============================================================
# CONFIGURATION
# ============================================================

SEED = 42

random.seed(SEED)

torch.manual_seed(SEED)


# ============================================================
# TOKENIZER
# ============================================================

sp = spm.SentencePieceProcessor(
    model_file=str(TOKENIZER)
)


# ============================================================
# LOAD MODEL
# ============================================================

print("Loading trained model...")

model = Transformer().to(DEVICE)


checkpoint = torch.load(
    CHECKPOINT_DIR / "transformer.pt",
    map_location=DEVICE,
)


model.load_state_dict(
    checkpoint["model_state_dict"]
)


model.eval()


print("Model loaded successfully.")


# ============================================================
# LOAD DATASET
# ============================================================

def load_dataset():

    rows = []

    with open(
        DATASET,
        encoding="utf-8",
        newline="",
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            english = row["english"].strip()

            igbo = row["igbo"].strip()

            if english and igbo:

                rows.append({

                    "english": english,

                    "igbo": igbo,

                })

    return rows


# ============================================================
# CREATE TEST SET
# ============================================================

def create_test_set(rows):

    rows = rows.copy()

    random.shuffle(rows)

    test_size = int(

        0.15 * len(rows)

    )

    return rows[:test_size]


# ============================================================
# PADDING
# ============================================================

def pad(ids):

    ids = ids[:MAX_LENGTH]

    ids += [

        PAD_IDX

    ] * (

        MAX_LENGTH - len(ids)

    )

    return ids


# ============================================================
# TRANSLATION
# ============================================================

def translate(

    sentence,

    source,

    target,

):

    # --------------------------------------------------------
    # DIRECTION TOKEN
    # --------------------------------------------------------

    if (

        source == "english"

        and target == "igbo"

    ):

        direction_token = "<en2ig>"


    elif (

        source == "igbo"

        and target == "english"

    ):

        direction_token = "<ig2en>"


    else:

        raise ValueError(

            "Unsupported translation direction."

        )


    # --------------------------------------------------------
    # DIRECTION ID
    # --------------------------------------------------------

    direction_id = sp.piece_to_id(

        direction_token

    )


    # --------------------------------------------------------
    # SOURCE ENCODING
    # --------------------------------------------------------

    src_ids = [

        BOS_IDX,

        direction_id,

    ]


    src_ids.extend(

        sp.encode(

            sentence,

            out_type=int,

        )

    )


    src_ids.append(

        EOS_IDX

    )


    src = torch.tensor(

        [

            pad(src_ids)

        ],

        dtype=torch.long,

        device=DEVICE,

    )


    # --------------------------------------------------------
    # DECODER STARTS WITH BOS
    # --------------------------------------------------------

    tgt = torch.tensor(

        [

            [

                BOS_IDX

            ]

        ],

        dtype=torch.long,

        device=DEVICE,

    )


    generated = []


    # --------------------------------------------------------
    # AUTOREGRESSIVE DECODING
    # --------------------------------------------------------

    with torch.no_grad():

        for _ in range(

            MAX_LENGTH - 1

        ):


            output = model(

                src,

                tgt,

            )


            logits = output[

                0,

                -1,

            ]


            next_token = torch.argmax(

                logits

            ).item()


            if next_token in [

                EOS_IDX,

                PAD_IDX,

                BOS_IDX,

            ]:

                break


            generated.append(

                next_token

            )


            next_token_tensor = torch.tensor(

                [

                    [

                        next_token

                    ]

                ],

                dtype=torch.long,

                device=DEVICE,

            )


            tgt = torch.cat(

                [

                    tgt,

                    next_token_tensor,

                ],

                dim=1,

            )


    # --------------------------------------------------------
    # DECODE
    # --------------------------------------------------------

    result = sp.decode(

        generated

    )


    return result.strip()


# ============================================================
# EVALUATE ENGLISH → IGBO
# ============================================================

def evaluate_en_to_ig(test_rows):

    references = []

    predictions = []


    print()

    print("=" * 60)

    print("EVALUATING ENGLISH → IGBO")

    print("=" * 60)


    for row in test_rows:

        source = row["english"]

        reference = row["igbo"]


        prediction = translate(

            source,

            source="english",

            target="igbo",

        )


        references.append(reference)

        predictions.append(prediction)


    bleu = sacrebleu.corpus_bleu(

        predictions,

        [references],

    )


    chrf = sacrebleu.corpus_chrf(

        predictions,

        [references],

    )


    print()

    print(

        f"BLEU: {bleu.score:.2f}"

    )


    print(

        f"chrF++: {chrf.score:.2f}"

    )


    return {

        "bleu": bleu.score,

        "chrf": chrf.score,

        "predictions": predictions,

    }


# ============================================================
# EVALUATE IGBO → ENGLISH
# ============================================================

def evaluate_ig_to_en(test_rows):

    references = []

    predictions = []


    print()

    print("=" * 60)

    print("EVALUATING IGBO → ENGLISH")

    print("=" * 60)


    for row in test_rows:

        source = row["igbo"]

        reference = row["english"]


        prediction = translate(

            source,

            source="igbo",

            target="english",

        )


        references.append(reference)

        predictions.append(prediction)


    bleu = sacrebleu.corpus_bleu(

        predictions,

        [references],

    )


    chrf = sacrebleu.corpus_chrf(

        predictions,

        [references],

    )


    print()

    print(

        f"BLEU: {bleu.score:.2f}"

    )


    print(

        f"chrF++: {chrf.score:.2f}"

    )


    return {

        "bleu": bleu.score,

        "chrf": chrf.score,

        "predictions": predictions,

    }


# ============================================================
# PRINT SAMPLE TRANSLATIONS
# ============================================================

def print_samples(

    test_rows,

    en_ig_results,

    ig_en_results,

):

    print()

    print("=" * 60)

    print("SAMPLE TRANSLATIONS")

    print("=" * 60)


    sample_count = min(

        10,

        len(test_rows)

    )


    for index in range(

        sample_count

    ):

        row = test_rows[index]


        print()

        print(

            f"Example {index + 1}"

        )

        print(

            "-" * 40

        )


        print(

            "English:"

        )

        print(

            row["english"]

        )


        print(

            "Reference Igbo:"

        )

        print(

            row["igbo"]

        )


        print(

            "Predicted Igbo:"

        )

        print(

            en_ig_results["predictions"][index]

        )


        print()

        print(

            "Igbo:"

        )

        print(

            row["igbo"]

        )


        print(

            "Reference English:"

        )

        print(

            row["english"]

        )


        print(

            "Predicted English:"

        )

        print(

            ig_en_results["predictions"][index]

        )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("IGBO–ENGLISH NMT MODEL EVALUATION")

    print("=" * 60)


    rows = load_dataset()


    print()

    print(

        f"Total dataset pairs: {len(rows)}"

    )


    test_rows = create_test_set(

        rows

    )


    print(

        f"Evaluation pairs: {len(test_rows)}"

    )


    en_ig_results = evaluate_en_to_ig(

        test_rows

    )


    ig_en_results = evaluate_ig_to_en(

        test_rows

    )


    print_samples(

        test_rows,

        en_ig_results,

        ig_en_results,

    )


    print()

    print("=" * 60)

    print("FINAL EVALUATION RESULTS")

    print("=" * 60)


    print()

    print(

        f"English → Igbo BLEU: "

        f"{en_ig_results['bleu']:.2f}"

    )


    print(

        f"English → Igbo chrF++: "

        f"{en_ig_results['chrf']:.2f}"

    )


    print()

    print(

        f"Igbo → English BLEU: "

        f"{ig_en_results['bleu']:.2f}"

    )


    print(

        f"Igbo → English chrF++: "

        f"{ig_en_results['chrf']:.2f}"

    )


    print()

    print("=" * 60)

    print("EVALUATION COMPLETED")

    print("=" * 60)