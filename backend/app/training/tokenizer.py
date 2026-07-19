from collections import Counter
import pandas as pd


class Tokenizer:

    PAD = "<pad>"
    UNK = "<unk>"
    SOS = "<sos>"
    EOS = "<eos>"

    def __init__(self):

        self.word2idx = {
            self.PAD: 0,
            self.UNK: 1,
            self.SOS: 2,
            self.EOS: 3,
        }

        self.idx2word = {
            0: self.PAD,
            1: self.UNK,
            2: self.SOS,
            3: self.EOS,
        }

    def build_vocab(self, dataframe, min_freq=1):

        counter = Counter()

        for _, row in dataframe.iterrows():

            igbo = str(row["igbo"]).lower().split()

            english = str(row["english"]).lower().split()

            counter.update(igbo)

            counter.update(english)

        index = len(self.word2idx)

        for word, freq in counter.items():

            if freq >= min_freq and word not in self.word2idx:

                self.word2idx[word] = index

                self.idx2word[index] = word

                index += 1

    def encode(self, sentence):

        words = str(sentence).lower().split()

        ids = [self.word2idx[self.SOS]]

        for word in words:

            ids.append(
                self.word2idx.get(
                    word,
                    self.word2idx[self.UNK],
                )
            )

        ids.append(self.word2idx[self.EOS])

        return ids

    def decode(self, ids):

        words = []

        for idx in ids:

            if idx in (
                self.word2idx[self.PAD],
                self.word2idx[self.SOS],
                self.word2idx[self.EOS],
            ):
                continue

            words.append(
                self.idx2word.get(idx, self.UNK)
            )

        return " ".join(words)


# --------------------------------------------------
# Build tokenizer automatically
# --------------------------------------------------

df = pd.read_csv("dataset/final_dataset_clean.csv")

tokenizer = Tokenizer()

tokenizer.build_vocab(df)

print(f"Vocabulary Size: {len(tokenizer.word2idx)}")