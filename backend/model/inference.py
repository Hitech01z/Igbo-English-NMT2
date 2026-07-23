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
    # SOURCE ENCODING
    # --------------------------------------------------------

    source_text = (

        direction_token

        + " "

        + sentence

    )


    src_ids = [

        BOS_IDX

    ]


    src_ids.extend(

        sp.encode(

            source_text,

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


            if next_token == EOS_IDX:

                break


            if next_token == PAD_IDX:

                break


            if next_token == BOS_IDX:

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

        )


        if text.lower() == "exit":

            break


        direction = input(

            "Direction (en-ig / ig-en): "

        ).strip().lower()


        if direction == "en-ig":

            result = translate(

                text,

                source="english",

                target="igbo",

            )


        elif direction == "ig-en":

            result = translate(

                text,

                source="igbo",

                target="english",

            )


        else:

            print(

                "Invalid direction."

            )

            continue


        print()

        print(

            "Translation:"

        )

        print(

            result

        )

        print()