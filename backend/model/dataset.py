import csv

import torch
from torch.utils.data import Dataset

import sentencepiece as spm

from model.config import (
    DATASET,
    TOKENIZER,
    MAX_LENGTH,
)

sp = spm.SentencePieceProcessor(
    model_file=str(TOKENIZER)
)


class TranslationDataset(Dataset):

    def __init__(self):

        self.rows = []

        with open(DATASET, encoding="utf-8") as f:

            reader = csv.DictReader(f)

            for row in reader:
                self.rows.append(row)

    def __len__(self):

        return len(self.rows)

    def pad(self, ids):

        ids = ids[:MAX_LENGTH]

        ids += [0] * (MAX_LENGTH - len(ids))

        return ids

    def __getitem__(self, index):

        row = self.rows[index]

        src = [2] + sp.encode(
            row["english"],
            out_type=int,
        ) + [3]

        tgt = [2] + sp.encode(
            row["igbo"],
            out_type=int,
        ) + [3]

        return (
            torch.tensor(
                self.pad(src),
                dtype=torch.long,
            ),
            torch.tensor(
                self.pad(tgt),
                dtype=torch.long,
            ),
        )