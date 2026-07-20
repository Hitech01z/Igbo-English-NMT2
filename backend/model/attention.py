import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):

    def __init__(
        self,
        embed_dim,
        num_heads,
    ):

        super().__init__()

        self.attention = nn.MultiheadAttention(
            embed_dim,
            num_heads,
            batch_first=True,
        )

    def forward(
        self,
        query,
        key,
        value,
        mask=None,
    ):

        output, _ = self.attention(
            query,
            key,
            value,
            need_weights=False,
        )

        return output