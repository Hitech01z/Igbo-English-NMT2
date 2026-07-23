import csv

import torch

from torch.utils.data import Dataset

import sentencepiece as spm

from model.config import (
    DATASET,
    TOKENIZER,
    MAX_LENGTH,
    BOS_IDX,
    EOS_IDX,
)


sp = spm.SentencePieceProcessor(
    model_file=str(TOKENIZER)
)


class TranslationDataset(Dataset):

    def __init__(self):

        self.rows = []

        with open(
            DATASET,
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                english = row["english"].strip()

                igbo = row["igbo"].strip()


                # English → Igbo

                self.rows.append({

                    "source":
                    f"<en2ig> {english}",

                    "target":
                    igbo,

                })


                # Igbo → English

                self.rows.append({

                    "source":
                    f"<ig2en> {igbo}",

                    "target":
                    english,

                })


    def __len__(self):

        return len(self.rows)


    def pad(self, ids):

        ids = ids[:MAX_LENGTH]

        ids += [

            0

        ] * (

            MAX_LENGTH - len(ids)

        )

        return ids


    def __getitem__(self, index):

        row = self.rows[index]


        source_ids = [

            BOS_IDX

        ]

        source_ids.extend(

            sp.encode(

                row["source"],

                out_type=int,

            )

        )

        source_ids.append(

            EOS_IDX

        )


        target_ids = [

            BOS_IDX

        ]

        target_ids.extend(

            sp.encode(

                row["target"],

                out_type=int,

            )

        )

        target_ids.append(

            EOS_IDX

        )


        return (

            torch.tensor(

                self.pad(source_ids),

                dtype=torch.long,

            ),

            torch.tensor(

                self.pad(target_ids),

                dtype=torch.long,

            ),

        )