import sentencepiece as spm
from pathlib import Path

MODEL = Path(__file__).parent / "spm.model"

sp = spm.SentencePieceProcessor(model_file=str(MODEL))

ids = [2, 116, 491, 166, 11, 380, 959, 3]

print(sp.decode(ids))