# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word_list = sorted([letter for letter in word])

    def match(self, word_list):
        matched_word = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_list:
                matched_word.append(word)

        return matched_word