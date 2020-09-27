import numpy as np

samples = ["The cat sat on the mat.", " The dog ate my homework."]

dictionary = {}
for sample in samples:
    for word in sample.split():
        if word not in dictionary:
            # Note we keep the value of index 0 reserved for nothing.
            dictionary[word] = len(dictionary) + 1

print(dictionary)

words = 10  # Only consider the first 10 words in each sample.
results = np.zeros(shape=(len(samples), words, max(dictionary.values()) + 1))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:words]:
        index = dictionary.get(word)
        results[i, j, index] = 1.0

print(results)
