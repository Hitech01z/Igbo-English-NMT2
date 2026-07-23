import torch

from model.transformer import Transformer

from model.config import (

    DEVICE,

    MAX_LENGTH,

)


model = Transformer().to(DEVICE)


src = torch.randint(

    0,

    500,

    (

        2,

        MAX_LENGTH,

    ),

).to(DEVICE)


tgt = torch.randint(

    0,

    500,

    (

        2,

        MAX_LENGTH,

    ),

).to(DEVICE)


output = model(

    src,

    tgt,

)


print(

    "Source shape:",

    src.shape,

)


print(

    "Target shape:",

    tgt.shape,

)


print(

    "Output shape:",

    output.shape,

)