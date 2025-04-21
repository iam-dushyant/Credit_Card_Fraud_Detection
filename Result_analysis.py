# This code explores how the model performs with different train-test splits

from Observing_data import df
from Splitting_dataset import split_train_test
from Model_development import model_development

import numpy as np
import time

test_ratios = list(np.arange(0.1, 1.0, 0.1))
accuracies = []

start_time = time.perf_counter()

for i in test_ratios:
    train_indices, test_indices = split_train_test(df, i)
    accuracy = model_development(train_indices, test_indices)
    accuracies.append(accuracy)
    print(f"Accuracy is {accuracy:.5f}% for test ratio {i:.2f}")

end_time = time.perf_counter()

print(f"Execution time: {end_time - start_time:.6f} seconds")