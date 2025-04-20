import numpy as np
from Observing_data import df

# Splitting train-test set
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_indices, test_indices = split_train_test(df, 0.3)
print("Number of train instances:", len(train_indices))
print("Number of test indices:", len(test_indices))