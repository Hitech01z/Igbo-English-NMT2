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

print(
    "Using device:",
    DEVICE,
)


# ============================================================
# DATASET
# ============================================================

dataset = TranslationDataset()


train_size = int(
    0.8 * len(dataset)
)


val_size = (
    len(dataset)
    - train_size
)


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


print()
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

model = Transformer().to(
    DEVICE
)


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
# CHECKPOINT DIRECTORY
# ============================================================

CHECKPOINT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


checkpoint_path = (
    CHECKPOINT_DIR
    /
    "transformer.pt"
)


# ============================================================
# DEFAULT TRAINING VALUES
# ============================================================

start_epoch = 1

best_val_loss = float(
    "inf"
)


# ============================================================
# LOAD CHECKPOINT
# ============================================================

if checkpoint_path.exists():

    print()
    print(
        "Loading checkpoint..."
    )


    checkpoint = torch.load(
        checkpoint_path,
        map_location=DEVICE,
    )


    # --------------------------------------------------------
    # LOAD MODEL PARAMETERS
    # --------------------------------------------------------

    model.load_state_dict(
        checkpoint[
            "model_state_dict"
        ]
    )


    # --------------------------------------------------------
    # LOAD OPTIMIZER PARAMETERS
    # --------------------------------------------------------

    optimizer.load_state_dict(
        checkpoint[
            "optimizer_state_dict"
        ]
    )


    # --------------------------------------------------------
    # RESUME FROM NEXT EPOCH
    # --------------------------------------------------------

    last_completed_epoch = checkpoint.get(
        "epoch",
        0
    )


    start_epoch = (
        last_completed_epoch
        + 1
    )


    # --------------------------------------------------------
    # RESTORE BEST VALIDATION LOSS
    # --------------------------------------------------------

    if "best_val_loss" in checkpoint:

        best_val_loss = checkpoint[
            "best_val_loss"
        ]

    elif "val_loss" in checkpoint:

        best_val_loss = checkpoint[
            "val_loss"
        ]

    elif "loss" in checkpoint:

        best_val_loss = checkpoint[
            "loss"
        ]


    print()
    print(
        f"Last completed epoch: "
        f"{last_completed_epoch}"
    )


    print(
        f"Resuming from epoch: "
        f"{start_epoch}"
    )


    print(
        f"Best validation loss: "
        f"{best_val_loss:.4f}"
    )


# ============================================================
# CHECK WHETHER TRAINING IS COMPLETE
# ============================================================

if start_epoch > EPOCHS:

    print()
    print(
        "Training is already complete."
    )


    print(
        f"Last completed epoch: "
        f"{start_epoch - 1}"
    )


    print()

    raise SystemExit


# ============================================================
# TRAINING
# ============================================================

for epoch in range(
    start_epoch,
    EPOCHS + 1
):


    # ========================================================
    # TRAINING MODE
    # ========================================================

    model.train()


    total_train_loss = 0


    for batch_index, (
        src,
        tgt,
    ) in enumerate(
        train_loader
    ):


        # ----------------------------------------------------
        # MOVE DATA TO DEVICE
        # ----------------------------------------------------

        src = src.to(
            DEVICE
        )


        tgt = tgt.to(
            DEVICE
        )


        # ----------------------------------------------------
        # TEACHER FORCING
        # ----------------------------------------------------

        tgt_input = tgt[
            :,
            :-1
        ]


        tgt_output = tgt[
            :,
            1:
        ]


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
        # LOSS
        # ----------------------------------------------------

        loss = criterion(

            output.reshape(
                -1,
                output.size(
                    -1
                ),
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
        # OPTIMIZER UPDATE
        # ----------------------------------------------------

        optimizer.step()


        total_train_loss += (
            loss.item()
        )


        # ----------------------------------------------------
        # PROGRESS
        # ----------------------------------------------------

        if batch_index % 10 == 0:

            print(

                f"Epoch {epoch}/{EPOCHS} "

                f"| Batch "

                f"{batch_index}/"

                f"{len(train_loader)} "

                f"| Loss: "

                f"{loss.item():.4f}"

            )


    # ========================================================
    # AVERAGE TRAINING LOSS
    # ========================================================

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


            tgt_input = tgt[
                :,
                :-1
            ]


            tgt_output = tgt[
                :,
                1:
            ]


            output = model(
                src,
                tgt_input,
            )


            loss = criterion(

                output.reshape(
                    -1,
                    output.size(
                        -1
                    ),
                ),

                tgt_output.reshape(
                    -1
                ),

            )


            total_val_loss += (
                loss.item()
            )


    # ========================================================
    # AVERAGE VALIDATION LOSS
    # ========================================================

    average_val_loss = (

        total_val_loss
        /
        len(val_loader)

    )


    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

    print()


    print(
        f"Epoch {epoch}/{EPOCHS}"
    )


    print(
        f"Training Loss:   "
        f"{average_train_loss:.4f}"
    )


    print(
        f"Validation Loss: "
        f"{average_val_loss:.4f}"
    )


    # ========================================================
    # UPDATE BEST MODEL
    # ========================================================

    is_best = (
        average_val_loss
        <
        best_val_loss
    )


    if is_best:

        best_val_loss = (
            average_val_loss
        )


        print()
        print(
            "✓ New best validation loss."
        )


    # ========================================================
    # SAVE CHECKPOINT
    # ========================================================

    torch.save(

        {

            "model_state_dict":
            model.state_dict(),


            "optimizer_state_dict":
            optimizer.state_dict(),


            # Last completed epoch
            "epoch":
            epoch,


            "train_loss":
            average_train_loss,


            "val_loss":
            average_val_loss,


            "best_val_loss":
            best_val_loss,

        },

        checkpoint_path,

    )


    print()
    print(
        "✓ Checkpoint saved."
    )


    print()
    print(
        "=" * 60
    )


# ============================================================
# TRAINING COMPLETED
# ============================================================

print()


print(
    "Training completed."
)


print()


print(
    f"Final epoch completed: "
    f"{EPOCHS}"
)


print()


print(
    f"Best validation loss: "
    f"{best_val_loss:.4f}"
)


print()


print(
    "Final checkpoint saved to:"
)


print(
    checkpoint_path
)