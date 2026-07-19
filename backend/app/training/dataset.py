from torch.utils.data import Dataset


class TranslationDataset(Dataset):

    def __init__(self, dataframe, tokenizer):

        self.df = dataframe.reset_index(drop=True)

        self.tokenizer = tokenizer

    def __len__(self):

        return len(self.df)

    def __getitem__(self, idx):

        row = self.df.iloc[idx]

        return {

            "src": self.tokenizer.encode(row["igbo"]),

            "tgt": self.tokenizer.encode(row["english"]),

        }