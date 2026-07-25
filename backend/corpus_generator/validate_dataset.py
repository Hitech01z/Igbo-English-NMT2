import csv
from pathlib import Path
from collections import defaultdict


BASE_DIR = Path(__file__).parent

DATASET = (
    BASE_DIR
    / "output"
    / "final_dataset.csv"
)


rows = []

with open(
    DATASET,
    encoding="utf-8",
    newline="",
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        rows.append(row)


print("=" * 50)
print("DATASET VALIDATION REPORT")
print("=" * 50)


# ============================================================
# EMPTY ROWS
# ============================================================

empty_rows = []

for row in rows:

    if not row["english"].strip() or not row["igbo"].strip():

        empty_rows.append(row)


# ============================================================
# DUPLICATE PAIRS
# ============================================================

pairs = set()

duplicate_pairs = []

for row in rows:

    pair = (

        row["english"].strip().lower(),

        row["igbo"].strip().lower(),

    )

    if pair in pairs:

        duplicate_pairs.append(row)

    else:

        pairs.add(pair)


# ============================================================
# AMBIGUOUS ENGLISH SOURCES
# ============================================================

english_to_igbo = defaultdict(set)

english_domains = defaultdict(set)

for row in rows:

    english = row["english"].strip()

    igbo = row["igbo"].strip()

    domain = row["domain"].strip()

    english_to_igbo[english].add(igbo)

    english_domains[english].add(domain)


ambiguous = {

    english: translations

    for english, translations

    in english_to_igbo.items()

    if len(translations) > 1

}


# ============================================================
# SUSPICIOUS ROWS
# ============================================================

suspicious = []

for row in rows:

    english = row["english"].lower().strip()
    igbo = row["igbo"].lower().strip()

    english_words = english.split()
    igbo_words = igbo.split()

    has_repeated_word = False

    # --------------------------------------------------------
    # CHECK ENGLISH
    # --------------------------------------------------------

    for i in range(len(english_words) - 1):

        if english_words[i] == english_words[i + 1]:

            has_repeated_word = True
            break

    # --------------------------------------------------------
    # CHECK IGBO
    # --------------------------------------------------------

    if not has_repeated_word:

        for i in range(len(igbo_words) - 1):

            if igbo_words[i] == igbo_words[i + 1]:

                has_repeated_word = True
                break

    # --------------------------------------------------------
    # SAVE ONCE
    # --------------------------------------------------------

    if has_repeated_word:

        suspicious.append(row)

# ============================================================
# REPORT
# ============================================================

print(

    f"Total rows: {len(rows)}"

)

print(

    f"Empty rows: {len(empty_rows)}"

)

print(

    f"Duplicate pairs: {len(duplicate_pairs)}"

)

print(

    f"Ambiguous English sources: "

    f"{len(ambiguous)}"

)

print(

    f"Suspicious rows: "

    f"{len(suspicious)}"

)

print("=" * 50)


# ============================================================
# SHOW AMBIGUOUS SOURCES
# ============================================================

if ambiguous:

    print()

    print(

        "AMBIGUOUS ENGLISH SOURCES"

    )

    print("-" * 50)


    for english, translations in ambiguous.items():

        print()

        print(

            f"English: {english}"

        )

        print(

            "Igbo translations:"

        )


        for translation in translations:

            print(

                f"  - {translation}"

            )


# ============================================================
# SHOW SUSPICIOUS ROWS
# ============================================================

if suspicious:

    print()

    print(

        "SUSPICIOUS ROW DETAILS"

    )

    print("-" * 50)


    for index, row in enumerate(

        suspicious,

        start=1,

    ):

        print()

        print(

            f"{index}. "

            f"Domain: {row['domain']}"

        )

        print(

            f"   English: "

            f"{row['english']}"

        )

        print(

            f"   Igbo: "

            f"{row['igbo']}"

        )