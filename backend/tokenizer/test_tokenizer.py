from pathlib import Path
import sentencepiece as spm


BASE_DIR = Path(__file__).resolve().parent

MODEL = BASE_DIR / "spm.model"

sp = spm.SentencePieceProcessor(
    model_file=str(MODEL)
)


TEST_SENTENCES = [

    "Ụtụtụ ọma",

    "Abụ m nwa akwụkwọ",

    "Onye ọrụ ugbo wetara ọka",

    "Ọba akwụkwọ meghere",

    "ụgbọala",

    "ịntanetị",

    "<en2ig> Good morning.",

    "<ig2en> Ụtụtụ ọma.",

]


for text in TEST_SENTENCES:

    ids = sp.encode(
        text,
        out_type=int,
    )

    pieces = sp.encode(
        text,
        out_type=str,
    )

    decoded = sp.decode(ids)

    unknown_count = ids.count(
        sp.unk_id()
    )

    print("=" * 60)

    print("TEXT:")

    print(text)

    print()

    print("IDS:")

    print(ids)

    print()

    print("PIECES:")

    print(pieces)

    print()

    print("DECODED:")

    print(decoded)

    print()

    print(

        "UNKNOWN TOKEN COUNT:",

        unknown_count,

    )


print("=" * 60)

print("Tokenizer test completed.")