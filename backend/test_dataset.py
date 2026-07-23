from data.dataset import TranslationDataset


dataset = TranslationDataset()


print(
    "Dataset size:",
    len(dataset),
)


source, target = dataset[0]


print(
    "Source shape:",
    source.shape,
)


print(
    "Target shape:",
    target.shape,
)


print(
    "First source IDs:",
    source.tolist(),
)


print(
    "First target IDs:",
    target.tolist(),
)