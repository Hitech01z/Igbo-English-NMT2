import torch

from app.models.embeddings import TokenEmbedding

embedding = TokenEmbedding(

    vocab_size=10000,

    d_model=512

)

tokens = torch.randint(

    0,

    10000,

    (2, 12)

)

output = embedding(tokens)

print(output.shape)