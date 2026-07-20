import torch
import sentencepiece as spm

from model.transformer import Transformer
from model.config import (
    TOKENIZER,
    CHECKPOINT_DIR,
    DEVICE,
    MAX_LENGTH,
)

sp = spm.SentencePieceProcessor(
    model_file=str(TOKENIZER)
)

model = Transformer().to(DEVICE)

checkpoint = torch.load(
    CHECKPOINT_DIR / "transformer.pt",
    map_location=DEVICE,
)

# Load checkpoint
if "model_state_dict" in checkpoint:
    model.load_state_dict(checkpoint["model_state_dict"])
else:
    model.load_state_dict(checkpoint)

model.eval()


def pad(ids):
    ids = ids[:MAX_LENGTH]
    ids += [0] * (MAX_LENGTH - len(ids))
    return ids


def translate(sentence: str):

    src_ids = [2] + sp.encode(sentence, out_type=int) + [3]

    src = torch.tensor(
        [pad(src_ids)],
        dtype=torch.long,
        device=DEVICE,
    )

    tgt = torch.tensor(
        [[2]],
        dtype=torch.long,
        device=DEVICE,
    )

    with torch.no_grad():

        for _ in range(MAX_LENGTH):

            print("Current target length:", tgt.shape)

            output = model(src, tgt)

            next_token = output[:, -1].argmax(dim=-1)

            tgt = torch.cat(
                [tgt, next_token.unsqueeze(1)],
                dim=1,
            )

            if next_token.item() == 3:
                break

    ids = tgt.squeeze().tolist()

    # Remove BOS and EOS
    ids = [i for i in ids if i not in (0, 2, 3)]

    return sp.decode(ids)


if __name__ == "__main__":

    while True:

        text = input("\nEnglish: ")

        if text.lower() == "exit":
            break

        print("Igbo:", translate(text))