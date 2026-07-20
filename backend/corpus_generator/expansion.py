import random


class ExpansionEngine:

    def __init__(self):

        self.prefixes = [
            "",
            "Please",
            "Kindly",
            "Now",
            "Today",
            "Tomorrow",
            "Quickly",
        ]

        self.suffixes = [
            "",
            "now.",
            "today.",
            "immediately.",
            "carefully.",
            "again.",
        ]

        self.fillers = [
            "",
            "really",
            "very",
            "always",
            "often",
            "sometimes",
        ]

    def expand(self, pair):

        english = pair["english"]
        igbo = pair["igbo"]

        prefix = random.choice(self.prefixes)
        suffix = random.choice(self.suffixes)
        filler = random.choice(self.fillers)

        if filler:

            words = english.split()

            if len(words) > 2:

                index = random.randint(
                    1,
                    len(words) - 2,
                )

                words.insert(
                    index,
                    filler,
                )

                english = " ".join(words)

        if prefix:

            english = f"{prefix} {english}"

        if suffix:

            english = f"{english} {suffix}"

        return {
            "domain": pair["domain"],
            "english": english.strip(),
            "igbo": igbo.strip(),
        }