import numpy as np

samples = [
    "The cat sat on the mat.",
    " The dog ate my homework.",
    "The fox jumped over the lazy dog.",
]

word_dictionary = {}
for sample in samples:
    for word in sample.split():
        if word not in word_dictionary:
            # Note we keep the value of index 0 reserved for nothing.
            word_dictionary[word] = len(word_dictionary) + 1

print(word_dictionary)

words = 10  # Only consider the first 10 words in each sample.
results = np.zeros(shape=(len(samples), words, max(word_dictionary.values()) + 1))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:words]:
        index = word_dictionary.get(word)
        results[i, j, index] = 1.0

print(results)
