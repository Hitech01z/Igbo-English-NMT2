import torch.nn as nn


class MultiHeadAttention(nn.Module):

    def __init__(

        self,

        embed_dim,

        num_heads,

    ):

        super().__init__()


        self.attention = nn.MultiheadAttention(

            embed_dim=embed_dim,

            num_heads=num_heads,

            batch_first=True,

        )


    def forward(

        self,

        query,

        key,

        value,

        key_padding_mask=None,

        attn_mask=None,

    ):

        output, _ = self.attention(

            query,

            key,

            value,

            key_padding_mask=key_padding_mask,

            attn_mask=attn_mask,

            need_weights=False,

        )


        return output