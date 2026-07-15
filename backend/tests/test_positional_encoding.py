import torch

from app.models.positional_encoding import PositionalEncoding

pe = PositionalEncoding(
    d_model=512
)

x = torch.randn(
    2,
    20,
    512
)

output = pe(x)

print(output.shape)