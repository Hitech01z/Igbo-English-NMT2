import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from model.dataset import TranslationDataset
from model.transformer import Transformer
from model.config import (
    DEVICE,
    BATCH_SIZE,
    LEARNING_RATE,
    EPOCHS,
    CHECKPOINT_DIR,
    VOCAB_SIZE,
)

dataset = TranslationDataset()

loader = DataLoader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
)

model = Transformer().to(DEVICE)

criterion = nn.CrossEntropyLoss(ignore_index=0)

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE,
)

print(f"Using device: {DEVICE}")
print(f"Training samples: {len(dataset)}")


for epoch in range(EPOCHS):

    model.train()

    total_loss = 0

    for batch_idx, (src, tgt) in enumerate(loader):

        src = src.to(DEVICE)
        tgt = tgt.to(DEVICE)

        decoder_input = tgt[:, :-1]
        target = tgt[:, 1:]

        output = model(
            src,
            decoder_input,
        )

        loss = criterion(
            output.reshape(-1, VOCAB_SIZE),
            target.reshape(-1),
        )

        optimizer.zero_grad()

        loss.backward()

        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            1.0,
        )

        optimizer.step()

        total_loss += loss.item()

        if batch_idx % 50 == 0:
            print(
                f"Epoch {epoch+1}/{EPOCHS} | "
                f"Batch {batch_idx}/{len(loader)} | "
                f"Loss: {loss.item():.4f}"
            )

    avg_loss = total_loss / len(loader)

    print(
        f"Epoch {epoch+1}/{EPOCHS} Loss: {avg_loss:.4f}"
    )

    torch.save(
        {
            "epoch": epoch + 1,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "loss": avg_loss,
        },
        CHECKPOINT_DIR / "transformer.pt",
    )

print("\nTraining Finished Successfully.")