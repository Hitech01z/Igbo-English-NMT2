import torch.nn as nn

from model.positional_encoding import (
    PositionalEncoding,
)


class TransformerEmbedding(nn.Module):

    def __init__(
        self,
        vocab_size,
        embed_dim,
        max_length,
        dropout,
    ):

        super().__init__()

        self.token = nn.Embedding(
            vocab_size,
            embed_dim,
        )

        self.position = PositionalEncoding(
            embed_dim,
            max_length,
        )

        self.dropout = nn.Dropout(
            dropout,
        )

    def forward(
        self,
        x,
    ):

        x = self.token(x)

        x = self.position(x)

        return self.dropout(x)