from string import printable as characters

import numpy as np

samples = ["The cat sat on the mat.", "The dog ate my homework."]

char_dictionary = dict(zip(characters, range(1, len(characters) + 1)))

print(char_dictionary)

chars = 50  # Only consider the first 50 characters in each sample.
results = np.zeros((len(samples), chars, max(char_dictionary.values()) + 1))

for i, sample in enumerate(samples):
    for j, char in enumerate(sample):
        index = char_dictionary.get(char)
        results[i, j, index] = 1.0

print(results)
