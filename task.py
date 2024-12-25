#function to count the frequency of word in a sentence
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


