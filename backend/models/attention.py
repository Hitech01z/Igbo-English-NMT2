import math
import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, num_heads):

        super().__init__()

        assert d_model % num_heads == 0

        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

        self.fc_out = nn.Linear(d_model, d_model)

    def split_heads(self, x):

        batch_size = x.shape[0]

        return x.view(
            batch_size,
            -1,
            self.num_heads,
            self.head_dim
        ).transpose(1, 2)

    def forward(self, query, key, value, mask=None):

        batch_size = query.shape[0]

        Q = self.split_heads(self.W_q(query))
        K = self.split_heads(self.W_k(key))
        V = self.split_heads(self.W_v(value))

        energy = torch.matmul(
            Q,
            K.transpose(-2, -1)
        )

        energy = energy / math.sqrt(self.head_dim)

        if mask is not None:

            energy = energy.masked_fill(mask == 0, -1e9)

        attention = torch.softmax(
            energy,
            dim=-1
        )

        out = torch.matmul(attention, V)

        out = out.transpose(1, 2).contiguous()

        out = out.view(
            batch_size,
            -1,
            self.d_model
        )

        out = self.fc_out(out)

        return out