import torch.nn as nn

from app.models.attention import MultiHeadAttention
from app.models.feedforward import FeedForward


class EncoderLayer(nn.Module):

    def __init__(

        self,

        d_model,

        num_heads,

        hidden_dim,

        dropout=0.1

    ):

        super().__init__()

        self.attention = MultiHeadAttention(

            d_model,

            num_heads

        )

        self.norm1 = nn.LayerNorm(d_model)

        self.norm2 = nn.LayerNorm(d_model)

        self.feedforward = FeedForward(

            d_model,

            hidden_dim,

            dropout

        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):

        attention = self.attention(

            x,

            x,

            x,

            mask

        )

        x = self.norm1(

            x + self.dropout(attention)

        )

        ff = self.feedforward(x)

        x = self.norm2(

            x + self.dropout(ff)

        )

        return x