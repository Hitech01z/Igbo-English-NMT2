import sentencepiece as spm

from model.config import TOKENIZER


sp = spm.SentencePieceProcessor(
    model_file=str(TOKENIZER)
)


tests = [

    "Ụtụtụ",

    "ọma",

    "Ụtụtụ ọma",

    "Abụ m nwa akwụkwọ",

    "Onye ọrụ ugbo wetara ọka",

    "<en2ig>",

    "<ig2en>",

]


for text in tests:

    ids = sp.encode(
        text,
        out_type=int,
    )


    pieces = sp.encode(
        text,
        out_type=str,
    )


    print("=" * 60)

    print("TEXT:")

    print(text)


    print("\nIDS:")

    print(ids)


    print("\nPIECES:")

    print(pieces)


    print("\nDECODED:")

    print(sp.decode(ids))


    print("\nUNKNOWN TOKEN COUNT:")

    print(

        sum(

            1

            for token in ids

            if token == sp.unk_id()

        )

    )