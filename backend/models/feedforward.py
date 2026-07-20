import torch.nn as nn


class FeedForward(nn.Module):

    def __init__(self, d_model, hidden_dim, dropout=0.1):

        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(d_model, hidden_dim),

            nn.ReLU(),

            nn.Dropout(dropout),

            nn.Linear(hidden_dim, d_model)

        )

    def forward(self, x):

        return self.network(x)