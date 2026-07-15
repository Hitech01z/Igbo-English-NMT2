import torch

from app.models.attention import MultiHeadAttention


model = MultiHeadAttention(

    d_model=512,

    num_heads=8

)

x = torch.randn(

    2,

    15,

    512

)

output = model(

    x,

    x,

    x

)

print(output.shape)