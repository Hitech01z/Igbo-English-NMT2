from pathlib import Path
import sentencepiece as spm

BASE_DIR = Path(__file__).parent

CORPUS = BASE_DIR / "training_corpus.txt"
MODEL_PREFIX = BASE_DIR / "spm"

spm.SentencePieceTrainer.train(
    input=str(CORPUS),
    model_prefix=str(MODEL_PREFIX),
    vocab_size=1000,
    model_type="bpe",
    pad_id=0,
    unk_id=1,
    bos_id=2,
    eos_id=3,
    character_coverage=1.0,
)

print("Tokenizer training completed successfully.")