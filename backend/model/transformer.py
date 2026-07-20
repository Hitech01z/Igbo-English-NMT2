import torch
import torch.nn as nn

from model.embeddings import TransformerEmbedding
from model.encoder import Encoder
from model.decoder import Decoder

from model.config import (
    VOCAB_SIZE,
    EMBED_SIZE,
    MAX_LENGTH,
    NUM_HEADS,
    NUM_ENCODER_LAYERS,
    NUM_DECODER_LAYERS,
    FF_DIM,
    DROPOUT,
)


class Transformer(nn.Module):

    def __init__(self):
        super().__init__()

        self.embedding = TransformerEmbedding(
            vocab_size=VOCAB_SIZE,
            embed_dim=EMBED_SIZE,
            max_length=MAX_LENGTH,
            dropout=DROPOUT,
        )

        self.encoder = Encoder(
            embed_dim=EMBED_SIZE,
            num_layers=NUM_ENCODER_LAYERS,
            num_heads=NUM_HEADS,
            ff_dim=FF_DIM,
            dropout=DROPOUT,
        )

        self.decoder = Decoder(
            embed_dim=EMBED_SIZE,
            num_layers=NUM_DECODER_LAYERS,
            num_heads=NUM_HEADS,
            ff_dim=FF_DIM,
            dropout=DROPOUT,
        )

        self.output_layer = nn.Linear(
            EMBED_SIZE,
            VOCAB_SIZE,
        )

    def make_src_mask(self, src):

        return (src != 0).unsqueeze(1).unsqueeze(2)

    def make_tgt_mask(self, tgt):

        batch_size, tgt_len = tgt.shape

        padding_mask = (
            tgt != 0
        ).unsqueeze(1).unsqueeze(2)

        causal_mask = torch.tril(
            torch.ones(
                tgt_len,
                tgt_len,
                device=tgt.device,
            )
        ).bool()

        causal_mask = causal_mask.unsqueeze(0).unsqueeze(1)

        return padding_mask & causal_mask

    def forward(
        self,
        src,
        tgt,
    ):

        src_mask = self.make_src_mask(src)

        tgt_mask = self.make_tgt_mask(tgt)

        src = self.embedding(src)

        tgt = self.embedding(tgt)

        encoder_output = self.encoder(
            src,
            src_mask,
        )

        decoder_output = self.decoder(
            tgt,
            encoder_output,
            src_mask,
            tgt_mask,
        )

        output = self.output_layer(
            decoder_output
        )

        return output