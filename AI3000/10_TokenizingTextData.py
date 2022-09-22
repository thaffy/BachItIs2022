import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer

# nltk.download()

input_text = "Do you know how tokenization works? It's actually quite interesting. Let's analyze a couple of sentences and figure it out"

# Sentence Tokenizer
print("\nSentence Tokenizer:")
print(sent_tokenize(input_text))

# Word tokenizer
print("\nWord Tokenizer:")
print(word_tokenize(input_text))

# WordPunct Tokenizer
print("\nWord Punct Tokenizer:")
print(WordPunctTokenizer().tokenize(input_text))
