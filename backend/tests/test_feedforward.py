import torch

from app.models.feedforward import FeedForward

ff = FeedForward(

    d_model=512,

    hidden_dim=2048

)

x = torch.randn(

    2,

    15,

    512

)

output = ff(x)

print(output.shape)