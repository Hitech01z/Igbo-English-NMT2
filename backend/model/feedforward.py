import torch.nn as nn


class FeedForward(nn.Module):

    def __init__(
        self,
        embed_dim,
        ff_dim,
        dropout,
    ):

        super().__init__()

        self.layers = nn.Sequential(

            nn.Linear(
                embed_dim,
                ff_dim,
            ),

            nn.ReLU(),

            nn.Dropout(dropout),

            nn.Linear(
                ff_dim,
                embed_dim,
            ),
        )

    def forward(
        self,
        x,
    ):

        return self.layers(x)