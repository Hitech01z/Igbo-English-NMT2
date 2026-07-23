import torch

import torch.nn as nn

from torch.utils.data import DataLoader


from data.dataset import TranslationDataset

from model.transformer import Transformer

from model.config import (

    DEVICE,

    VOCAB_SIZE,

    PAD_IDX,

    CHECKPOINT_DIR,

)


# ============================================================
# TRAINING SETTINGS
# ============================================================

BATCH_SIZE = 8

EPOCHS = 30

LEARNING_RATE = 0.0003


# ============================================================
# DATASET
# ============================================================

dataset = TranslationDataset()


loader = DataLoader(

    dataset,

    batch_size=BATCH_SIZE,

    shuffle=True,

)


print(

    "Using device:",

    DEVICE,

)


print(

    "Training samples:",

    len(dataset),

)


# ============================================================
# MODEL
# ============================================================

model = Transformer().to(DEVICE)


# ============================================================
# LOSS
# ============================================================

criterion = nn.CrossEntropyLoss(

    ignore_index=PAD_IDX,

)


# ============================================================
# OPTIMIZER
# ============================================================

optimizer = torch.optim.AdamW(

    model.parameters(),

    lr=LEARNING_RATE,

    betas=(0.9, 0.98),

    weight_decay=0.01,

)


# ============================================================
# CHECKPOINT DIRECTORY
# ============================================================

CHECKPOINT_DIR.mkdir(

    parents=True,

    exist_ok=True,

)


best_loss = float("inf")


# ============================================================
# TRAINING
# ============================================================

for epoch in range(EPOCHS):

    model.train()


    total_loss = 0


    for batch_index, (

        source,

        target,

    ) in enumerate(loader):


        source = source.to(DEVICE)

        target = target.to(DEVICE)


        # ----------------------------------------------------
        # DECODER INPUT
        # ----------------------------------------------------

        target_input = target[:, :-1]


        # ----------------------------------------------------
        # EXPECTED OUTPUT
        # ----------------------------------------------------

        target_output = target[:, 1:]


        # ----------------------------------------------------
        # FORWARD PASS
        # ----------------------------------------------------

        output = model(

            source,

            target_input,

        )


        # ----------------------------------------------------
        # RESHAPE
        # ----------------------------------------------------

        output = output.reshape(

            -1,

            VOCAB_SIZE,

        )


        target_output = target_output.reshape(

            -1,

        )


        # ----------------------------------------------------
        # LOSS
        # ----------------------------------------------------

        loss = criterion(

            output,

            target_output,

        )


        # ----------------------------------------------------
        # BACKPROPAGATION
        # ----------------------------------------------------

        optimizer.zero_grad()


        loss.backward()


        torch.nn.utils.clip_grad_norm_(

            model.parameters(),

            max_norm=1.0,

        )


        optimizer.step()


        total_loss += loss.item()


        if batch_index % 10 == 0:

            print(

                f"Epoch {epoch + 1}/{EPOCHS} "

                f"| Batch {batch_index}/{len(loader)} "

                f"| Loss: {loss.item():.4f}"

            )


    average_loss = (

        total_loss

        / len(loader)

    )


    print()

    print(

        f"Epoch {epoch + 1}/{EPOCHS} "

        f"Loss: {average_loss:.4f}"

    )


    # --------------------------------------------------------
    # SAVE BEST MODEL
    # --------------------------------------------------------

    if average_loss < best_loss:

        best_loss = average_loss


        torch.save(

            {

                "model_state_dict":

                model.state_dict(),

                "optimizer_state_dict":

                optimizer.state_dict(),

                "epoch":

                epoch + 1,

                "loss":

                average_loss,

            },

            CHECKPOINT_DIR

            / "transformer.pt",

        )


        print(

            "Best checkpoint saved."

        )


print()

print(

    "Training completed successfully."

)

print(

    "Best loss:",

    best_loss,

)