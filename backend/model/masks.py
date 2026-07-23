import torch


def create_src_padding_mask(src):

    return src == 0


def create_tgt_padding_mask(tgt):

    return tgt == 0


def create_causal_mask(

    length,

    device,

):

    return torch.triu(

        torch.ones(

            length,

            length,

            device=device,

            dtype=torch.bool,

        ),

        diagonal=1,

    )