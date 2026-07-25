import torch
import sentencepiece as spm

from model.transformer import Transformer

from model.config import (
    TOKENIZER,
    CHECKPOINT_DIR,
    DEVICE,
    MAX_LENGTH,
    BOS_IDX,
    EOS_IDX,
    PAD_IDX,
)


# ============================================================
# TOKENIZER
# ============================================================

sp = spm.SentencePieceProcessor(

    model_file=str(TOKENIZER)

)


# ============================================================
# MODEL
# ============================================================

model = Transformer().to(DEVICE)


checkpoint = torch.load(

    CHECKPOINT_DIR / "transformer.pt",

    map_location=DEVICE,

)


model.load_state_dict(

    checkpoint["model_state_dict"]

)


model.eval()


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

    source="english",

    target="igbo",

):


    # --------------------------------------------------------
    # DETERMINE TRANSLATION DIRECTION
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
    # GET DIRECTION TOKEN ID
    # --------------------------------------------------------

    direction_id = sp.piece_to_id(

        direction_token

    )


    # --------------------------------------------------------
    # ENCODE SOURCE SENTENCE
    #
    # MUST MATCH TRAINING FORMAT:
    #
    # [BOS] [DIRECTION] sentence [EOS]
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


    # --------------------------------------------------------
    # PAD SOURCE
    # --------------------------------------------------------

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


            # --------------------------------------------
            # MODEL FORWARD PASS
            # --------------------------------------------

            output = model(

                src,

                tgt,

            )


            # --------------------------------------------
            # GET LAST TOKEN PREDICTION
            # --------------------------------------------

            logits = output[

                0,

                -1,

            ]


            next_token = torch.argmax(

                logits

            ).item()


            # --------------------------------------------
            # STOP CONDITIONS
            # --------------------------------------------

            if next_token == EOS_IDX:

                break


            if next_token == PAD_IDX:

                break


            if next_token == BOS_IDX:

                break


            # --------------------------------------------
            # ADD GENERATED TOKEN
            # --------------------------------------------

            generated.append(

                next_token

            )


            # --------------------------------------------
            # APPEND TOKEN TO DECODER INPUT
            # --------------------------------------------

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


    # ========================================================
    # DECODE GENERATED TOKENS
    # ========================================================

    result = sp.decode(

        generated

    )


    return result.strip()


# ============================================================
# TERMINAL TESTING
# ============================================================

if __name__ == "__main__":


    print()

    print(

        "Igbo-English Neural Machine Translation"

    )

    print(

        "Type 'exit' to stop."

    )

    print()


    while True:


        text = input(

            "Input: "

        ).strip()


        if text.lower() == "exit":

            break


        direction = input(

            "Direction (en-ig / ig-en): "

        ).strip().lower()


        # ----------------------------------------------------
        # ENGLISH → IGBO
        # ----------------------------------------------------

        if direction == "en-ig":


            result = translate(

                text,

                source="english",

                target="igbo",

            )


        # ----------------------------------------------------
        # IGBO → ENGLISH
        # ----------------------------------------------------

        elif direction == "ig-en":


            result = translate(

                text,

                source="igbo",

                target="english",

            )


        else:


            print()

            print(

                "Invalid direction."

            )

            print()

            continue


        print()

        print(

            "Translation:"

        )

        print(

            result

        )

        print()