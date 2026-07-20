import torch.nn as nn

from model.attention import MultiHeadAttention
from model.feedforward import FeedForward


class DecoderLayer(nn.Module):

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

        self.cross_attention = MultiHeadAttention(
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
        self.norm3 = nn.LayerNorm(embed_dim)

        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        x,
        encoder_output,
        src_mask=None,
        tgt_mask=None,
    ):

        attention = self.self_attention(
            x,
            x,
            x,
            tgt_mask,
        )

        x = self.norm1(
            x + self.dropout(attention)
        )

        cross = self.cross_attention(
            x,
            encoder_output,
            encoder_output,
            src_mask,
        )

        x = self.norm2(
            x + self.dropout(cross)
        )

        ff = self.feed_forward(x)

        x = self.norm3(
            x + self.dropout(ff)
        )

        return x


class Decoder(nn.Module):

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
                DecoderLayer(
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
        encoder_output,
        src_mask=None,
        tgt_mask=None,
    ):

        for layer in self.layers:

            x = layer(
                x,
                encoder_output,
                src_mask,
                tgt_mask,
            )

        return x