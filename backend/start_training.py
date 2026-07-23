import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split

from data.dataset import TranslationDataset

from model.transformer import Transformer

from model.config import (
    DEVICE,
    BATCH_SIZE,
    EPOCHS,
    LEARNING_RATE,
    PAD_IDX,
    CHECKPOINT_DIR,
)


# ============================================================
# CONFIGURATION
# ============================================================

print("Using device:", DEVICE)


# ============================================================
# DATASET
# ============================================================

dataset = TranslationDataset()


train_size = int(

    0.8 * len(dataset)

)

val_size = len(dataset) - train_size


train_dataset, val_dataset = random_split(

    dataset,

    [

        train_size,

        val_size,

    ],

)


train_loader = DataLoader(

    train_dataset,

    batch_size=BATCH_SIZE,

    shuffle=True,

)


val_loader = DataLoader(

    val_dataset,

    batch_size=BATCH_SIZE,

    shuffle=False,

)


print(

    "Total dataset samples:",

    len(dataset),

)


print(

    "Training samples:",

    len(train_dataset),

)


print(

    "Validation samples:",

    len(val_dataset),

)


# ============================================================
# MODEL
# ============================================================

model = Transformer().to(DEVICE)


# ============================================================
# LOSS FUNCTION
# ============================================================

criterion = nn.CrossEntropyLoss(

    ignore_index=PAD_IDX

)


# ============================================================
# OPTIMIZER
# ============================================================

optimizer = torch.optim.Adam(

    model.parameters(),

    lr=LEARNING_RATE,

)


# ============================================================
# BEST MODEL TRACKING
# ============================================================

best_val_loss = float("inf")


CHECKPOINT_DIR.mkdir(

    parents=True,

    exist_ok=True,

)


# ============================================================
# TRAINING
# ============================================================

for epoch in range(

    EPOCHS

):


    # --------------------------------------------------------
    # TRAINING MODE
    # --------------------------------------------------------

    model.train()


    total_train_loss = 0


    for batch_index, (

        src,

        tgt,

    ) in enumerate(

        train_loader

    ):


        src = src.to(

            DEVICE

        )


        tgt = tgt.to(

            DEVICE

        )


        # ----------------------------------------------------
        # TEACHER FORCING
        # ----------------------------------------------------

        tgt_input = tgt[:, :-1]

        tgt_output = tgt[:, 1:]


        # ----------------------------------------------------
        # CLEAR GRADIENTS
        # ----------------------------------------------------

        optimizer.zero_grad()


        # ----------------------------------------------------
        # FORWARD PASS
        # ----------------------------------------------------

        output = model(

            src,

            tgt_input,

        )


        # ----------------------------------------------------
        # CALCULATE LOSS
        # ----------------------------------------------------

        loss = criterion(

            output.reshape(

                -1,

                output.size(-1),

            ),

            tgt_output.reshape(

                -1

            ),

        )


        # ----------------------------------------------------
        # BACKPROPAGATION
        # ----------------------------------------------------

        loss.backward()


        # ----------------------------------------------------
        # GRADIENT CLIPPING
        # ----------------------------------------------------

        torch.nn.utils.clip_grad_norm_(

            model.parameters(),

            max_norm=1.0,

        )


        # ----------------------------------------------------
        # UPDATE PARAMETERS
        # ----------------------------------------------------

        optimizer.step()


        total_train_loss += loss.item()


        if batch_index % 10 == 0:

            print(

                f"Epoch {epoch + 1}/{EPOCHS} "

                f"| Batch {batch_index}/{len(train_loader)} "

                f"| Loss: {loss.item():.4f}"

            )


    average_train_loss = (

        total_train_loss

        /

        len(train_loader)

    )


    # ========================================================
    # VALIDATION
    # ========================================================

    model.eval()


    total_val_loss = 0


    with torch.no_grad():


        for src, tgt in val_loader:


            src = src.to(

                DEVICE

            )


            tgt = tgt.to(

                DEVICE

            )


            tgt_input = tgt[:, :-1]

            tgt_output = tgt[:, 1:]


            output = model(

                src,

                tgt_input,

            )


            loss = criterion(

                output.reshape(

                    -1,

                    output.size(-1),

                ),

                tgt_output.reshape(

                    -1

                ),

            )


            total_val_loss += loss.item()


    average_val_loss = (

        total_val_loss

        /

        len(val_loader)

    )


    print()

    print(

        f"Epoch {epoch + 1}/{EPOCHS}"

    )


    print(

        f"Training Loss:   {average_train_loss:.4f}"

    )


    print(

        f"Validation Loss: {average_val_loss:.4f}"

    )


    # ========================================================
    # SAVE BEST MODEL
    # ========================================================

    if average_val_loss < best_val_loss:


        best_val_loss = average_val_loss


        torch.save(

            {

                "model_state_dict":

                model.state_dict(),


                "optimizer_state_dict":

                optimizer.state_dict(),


                "epoch":

                epoch + 1,


                "train_loss":

                average_train_loss,


                "val_loss":

                average_val_loss,

            },

            CHECKPOINT_DIR / "transformer.pt",

        )


        print()

        print(

            "✓ Best model saved."

        )


    print()

    print(

        "=" * 60

    )


print()

print(

    "Training completed."

)


print(

    "Best validation loss:",

    best_val_loss,

)


print(

    "Best model saved to:",

    CHECKPOINT_DIR / "transformer.pt",

)