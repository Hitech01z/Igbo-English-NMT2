import sentencepiece as spm
from pathlib import Path

MODEL = Path(__file__).parent / "spm.model"

sp = spm.SentencePieceProcessor(model_file=str(MODEL))

text = "Good morning"

ids = sp.encode(text, out_type=int)

print("Encoded:", ids)