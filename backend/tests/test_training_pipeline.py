import torch

from data.dataset import TranslationDataset

from model.transformer import Transformer

from model.config import (
    DEVICE,
    VOCAB_SIZE,
    MAX_LENGTH,
)


print("=" * 60)

print("TESTING TRAINING PIPELINE")

print("=" * 60)


# ============================================================
# DATASET
# ============================================================

dataset = TranslationDataset()


print(
    "Dataset size:",
    len(dataset),
)


# ============================================================
# LOAD ONE SAMPLE
# ============================================================

source, target = dataset[0]


source = source.unsqueeze(0).to(DEVICE)

target = target.unsqueeze(0).to(DEVICE)


print(

    "Source shape:",

    source.shape,

)


print(

    "Target shape:",

    target.shape,

)


# ============================================================
# MODEL
# ============================================================

model = Transformer().to(DEVICE)


model.eval()


# ============================================================
# FORWARD PASS
# ============================================================

with torch.no_grad():

    output = model(

        source,

        target[:, :-1],

    )


print(

    "Model output shape:",

    output.shape,

)


# ============================================================
# EXPECTED SHAPE
# ============================================================

expected_shape = (

    1,

    MAX_LENGTH - 1,

    VOCAB_SIZE,

)


print(

    "Expected shape:",

    expected_shape,

)


if output.shape == expected_shape:

    print()

    print(

        "SUCCESS: Training pipeline is working."

    )

else:

    print()

    print(

        "ERROR: Output shape mismatch."

    )


print("=" * 60)