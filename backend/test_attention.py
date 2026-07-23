import torch

from model.attention import MultiHeadAttention


BATCH_SIZE = 2
SEQ_LEN = 6
EMBED_SIZE = 256
NUM_HEADS = 8


attention = MultiHeadAttention(
    embed_dim=EMBED_SIZE,
    num_heads=NUM_HEADS,
)


x = torch.randn(
    BATCH_SIZE,
    SEQ_LEN,
    EMBED_SIZE,
)


# No mask
output = attention(
    query=x,
    key=x,
    value=x,
)


print(
    "Input shape:",
    x.shape,
)


print(
    "Output shape:",
    output.shape,
)