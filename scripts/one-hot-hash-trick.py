import numpy as np

samples = ["The cat sat on the mat.", "The bad cat ate my homework."]

dictionary_length = 30
words = 10
results = np.zeros(shape=(len(samples), words, dictionary_length))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:words]:
        index = abs(hash(word)) % dictionary_length
        results[i, j, index] = 1.0

print(results)
