import torch
import torch.nn as nn


from model.config import (

    VOCAB_SIZE,
    EMBED_DIM,
    NUM_HEADS,
    NUM_LAYERS,
    FF_DIM,
    DROPOUT,
    MAX_LENGTH,

)


from model.encoder import Encoder

from model.decoder import Decoder

from model.masks import (

    create_src_padding_mask,
    create_tgt_padding_mask,
    create_causal_mask,

)


class Transformer(nn.Module):

    def __init__(self):

        super().__init__()


        # ====================================================
        # TOKEN EMBEDDING
        # ====================================================

        self.src_embedding = nn.Embedding(

            VOCAB_SIZE,

            EMBED_DIM,

            padding_idx=0,

        )


        self.tgt_embedding = nn.Embedding(

            VOCAB_SIZE,

            EMBED_DIM,

            padding_idx=0,

        )


        # ====================================================
        # POSITIONAL EMBEDDING
        # ====================================================

        self.src_position_embedding = nn.Embedding(

            64,

            EMBED_DIM,

        )


        self.tgt_position_embedding = nn.Embedding(

            64,

            EMBED_DIM,

        )


        # ====================================================
        # ENCODER
        # ====================================================

        self.encoder = Encoder(

            embed_dim=EMBED_DIM,

            num_layers=NUM_LAYERS,

            num_heads=NUM_HEADS,

            ff_dim=FF_DIM,

            dropout=DROPOUT,

        )


        # ====================================================
        # DECODER
        # ====================================================

        self.decoder = Decoder(

            embed_dim=EMBED_DIM,

            num_layers=NUM_LAYERS,

            num_heads=NUM_HEADS,

            ff_dim=FF_DIM,

            dropout=DROPOUT,

        )


        # ====================================================
        # OUTPUT PROJECTION
        # ====================================================

        self.output_layer = nn.Linear(

            EMBED_DIM,

            VOCAB_SIZE,

        )


        self.dropout = nn.Dropout(

            DROPOUT

        )


    def forward(

        self,

        src,

        tgt,

    ):

        batch_size = src.size(0)

        src_length = src.size(1)

        tgt_length = tgt.size(1)


        # ====================================================
        # POSITION INDICES
        # ====================================================

        src_positions = torch.arange(

            src_length,

            device=src.device,

        ).unsqueeze(0).expand(

            batch_size,

            src_length,

        )


        tgt_positions = torch.arange(

            tgt_length,

            device=tgt.device,

        ).unsqueeze(0).expand(

            batch_size,

            tgt_length,

        )


        # ====================================================
        # EMBEDDINGS
        # ====================================================

        src_embedded = (

            self.src_embedding(src)

            +

            self.src_position_embedding(

                src_positions

            )

        )


        tgt_embedded = (

            self.tgt_embedding(tgt)

            +

            self.tgt_position_embedding(

                tgt_positions

            )

        )


        src_embedded = self.dropout(

            src_embedded

        )


        tgt_embedded = self.dropout(

            tgt_embedded

        )


        # ====================================================
        # MASKS
        # ====================================================

        src_padding_mask = (

            create_src_padding_mask(src)

        )


        tgt_padding_mask = (

            create_tgt_padding_mask(tgt)

        )


        tgt_causal_mask = (

            create_causal_mask(

                tgt_length,

                tgt.device,

            )

        )


        # ====================================================
        # ENCODER
        # ====================================================

        encoder_output = self.encoder(

            src_embedded,

            padding_mask=src_padding_mask,

        )


        # ====================================================
        # DECODER
        # ====================================================

        decoder_output = self.decoder(

            tgt_embedded,

            encoder_output,

            src_padding_mask=src_padding_mask,

            tgt_padding_mask=tgt_padding_mask,

            tgt_causal_mask=tgt_causal_mask,

        )


        # ====================================================
        # VOCABULARY PREDICTION
        # ====================================================

        output = self.output_layer(

            decoder_output

        )


        return output