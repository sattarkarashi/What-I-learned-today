# Making an iterable class using __getitem__
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = text.split()
    def __getitem__(self, index):
        return self.words[index]
    def __len__(self):
        return len(self.words)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

first_iterable = Sentence('This is a sentence')
for word in first_iterable:
    print(word)


# Making iterables and iterators using __iter__ and __next__
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = text.split()
    def __iter__(self):
        return SentenceIterator(self.words)
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    def __iter__(self):
        return self

second_iterable = Sentence('This is a sentence')
for word in second_iterable:
    print(word)

# Using generator functions to create iterables and iterators
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = text.split()
    def __iter__(self):
        for word in self.words:
            yield word
        return
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

third_iterable = Sentence('This is a sentence')
for word in third_iterable:
    print(word)

# Lazy implementaton of Sentence using re.iterall and generator expression
import re
class Sentence:
    def __init__(self, text):
        self.text = text
    def __iter__(self):
        return (match.group() for match in re.finditer(r'\w+', self.text))
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

fourth_iterable = Sentence('This is a sentence')
for word in fourth_iterable:
    print(word)