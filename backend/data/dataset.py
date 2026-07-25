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

    PAD_IDX,

)


# ============================================================
# TOKENIZER
# ============================================================

sp = spm.SentencePieceProcessor(

    model_file=str(TOKENIZER)

)


# ============================================================
# TRANSLATION DATASET
# ============================================================

class TranslationDataset(Dataset):


    def __init__(self):


        self.rows = []


        # ----------------------------------------------------
        # LOAD DATASET
        # ----------------------------------------------------

        with open(

            DATASET,

            encoding="utf-8",

            newline="",

        ) as file:


            reader = csv.DictReader(

                file

            )


            for row in reader:


                english = row[

                    "english"

                ].strip()


                igbo = row[

                    "igbo"

                ].strip()


                # ====================================================
                # ENGLISH → IGBO
                # ====================================================

                self.rows.append({

                    "direction": "<en2ig>",

                    "source": english,

                    "target": igbo,

                })


                # ====================================================
                # IGBO → ENGLISH
                # ====================================================

                self.rows.append({

                    "direction": "<ig2en>",

                    "source": igbo,

                    "target": english,

                })


    # ============================================================
    # DATASET LENGTH
    # ============================================================

    def __len__(

        self

    ):


        return len(

            self.rows

        )


    # ============================================================
    # PADDING
    # ============================================================

    def pad(

        self,

        ids,

    ):


        ids = ids[

            :MAX_LENGTH

        ]


        ids += [

            PAD_IDX

        ] * (

            MAX_LENGTH - len(ids)

        )


        return ids


    # ============================================================
    # GET ITEM
    # ============================================================

    def __getitem__(

        self,

        index,

    ):


        row = self.rows[

            index

        ]


        # --------------------------------------------------------
        # DIRECTION TOKEN
        # --------------------------------------------------------

        direction_id = sp.piece_to_id(

            row["direction"]

        )


        # ========================================================
        # SOURCE
        #
        # [BOS] [DIRECTION] SENTENCE [EOS]
        # ========================================================

        source_ids = [

            BOS_IDX,

            direction_id,

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


        # ========================================================
        # TARGET
        #
        # [BOS] SENTENCE [EOS]
        # ========================================================

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


        # ========================================================
        # RETURN TENSORS
        # ========================================================

        return (

            torch.tensor(

                self.pad(

                    source_ids

                ),

                dtype=torch.long,

            ),

            torch.tensor(

                self.pad(

                    target_ids

                ),

                dtype=torch.long,

            ),

        )