import numpy as np

# Toy dataset
n_ratings = 5

dataset = type("Dataset", (), {})()  # simple mock object
dataset.user_id = np.array([10, 11, 12, 13, 14])
dataset.item_id = np.array([1, 1, 2, 3, 3])
dataset.rating  = np.array([5, 3, 4, 2, 5])

# Original data
print("Original:")
for u, i, r in zip(dataset.user_id, dataset.item_id, dataset.rating):
    print(u, i, r)

# Shuffle
np.random.seed(1)  # for reproducibility
idxs = np.arange(n_ratings)
np.random.shuffle(idxs)

rows_dupes = dataset.user_id[idxs]
cols_dupes = dataset.item_id[idxs]
vals       = dataset.rating[idxs]

# Shuffled data
print("\nShuffled:")
for u, i, r in zip(rows_dupes, cols_dupes, vals):
    print(u, i, r)
