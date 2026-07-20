from pathlib import Path
import torch

BASE_DIR = Path(__file__).parent.parent

DATASET = BASE_DIR / "corpus_generator" / "output" / "final_dataset_clean.csv"

TOKENIZER = BASE_DIR / "tokenizer" / "spm.model"

CHECKPOINT_DIR = BASE_DIR / "checkpoints"
CHECKPOINT_DIR.mkdir(exist_ok=True)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

VOCAB_SIZE = 1000

MAX_LENGTH = 64

BATCH_SIZE = 8

EMBED_SIZE = 256

NUM_HEADS = 8

NUM_ENCODER_LAYERS = 4

NUM_DECODER_LAYERS = 4

FF_DIM = 1024

DROPOUT = 0.1

EPOCHS = 10

LEARNING_RATE = 1e-4