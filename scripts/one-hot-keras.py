from keras.preprocessing.text import Tokenizer

samples = ["The cat sat on the mat.", "The bad cat ate my homework."]

tokenizer = Tokenizer(num_words=10)

tokenizer.fit_on_texts(samples)
results = tokenizer.texts_to_matrix(samples, mode="binary")
word_dictionary = tokenizer.word_index

print(word_dictionary)
print(results)
