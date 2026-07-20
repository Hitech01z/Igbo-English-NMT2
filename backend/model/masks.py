import torch


def create_src_mask(src):

    return (
        src != 0
    ).unsqueeze(1).unsqueeze(2)


def create_tgt_mask(tgt):

    batch_size, length = tgt.shape

    padding = (
        tgt != 0
    ).unsqueeze(1).unsqueeze(2)

    causal = torch.tril(

        torch.ones(
            length,
            length,
            device=tgt.device,
        )

    ).bool()

    causal = causal.unsqueeze(0).unsqueeze(1)

    return padding & causal