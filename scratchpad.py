#https://www.kdnuggets.com/2018/04/implementing-deep-learning-methods-feature-engineering-text-data-skip-gram.html#:~:text=is%20included%20here.-,The%20Skip%2Dgram%20Model,jumps%20over%20the%20lazy%20dog%E2%80%9D.
from keras.preprocessing import text

tokenizer = text.Tokenizer()
tokenizer.fit_on_texts(norm_bible)

word2frequency = tokenizer.word_counts
id2word = {v:k for k, v in word2frequency.items()}

vocab_size = len(word2frequency) + 1 
embed_size = 100

wids = [[word2frequency[w] for w in text.text_to_word_sequence(doc)] for doc in norm_bible]
print('Vocabulary Size:', vocab_size)
print('Vocabulary Sample:', list(word2frequency.items())[:10])