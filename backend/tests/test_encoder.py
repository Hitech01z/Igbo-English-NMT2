import torch

from app.models.encoder import EncoderLayer

encoder = EncoderLayer(

    d_model=512,

    num_heads=8,

    hidden_dim=2048

)

x = torch.randn(

    2,

    20,

    512

)

output = encoder(x)

print(output.shape)