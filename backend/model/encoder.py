import torch.nn as nn

from model.attention import MultiHeadAttention
from model.feedforward import FeedForward


class EncoderLayer(nn.Module):

    def __init__(
        self,
        embed_dim,
        num_heads,
        ff_dim,
        dropout,
    ):
        super().__init__()

        self.self_attention = MultiHeadAttention(
            embed_dim,
            num_heads,
        )

        self.feed_forward = FeedForward(
            embed_dim,
            ff_dim,
            dropout,
        )

        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        x,
        mask=None,
    ):

        attention = self.self_attention(
            x,
            x,
            x,
            mask,
        )

        x = self.norm1(
            x + self.dropout(attention)
        )

        ff = self.feed_forward(x)

        x = self.norm2(
            x + self.dropout(ff)
        )

        return x


class Encoder(nn.Module):

    def __init__(
        self,
        embed_dim,
        num_layers,
        num_heads,
        ff_dim,
        dropout,
    ):
        super().__init__()

        self.layers = nn.ModuleList(

            [
                EncoderLayer(
                    embed_dim,
                    num_heads,
                    ff_dim,
                    dropout,
                )

                for _ in range(num_layers)
            ]

        )

    def forward(
        self,
        x,
        mask=None,
    ):

        for layer in self.layers:

            x = layer(
                x,
                mask,
            )

        return x