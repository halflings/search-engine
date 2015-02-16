from collections import defaultdict, Counter
from operator import mul

from tokenizing import tokenize_sentence

class BaseIndex(object):
    def insert(self, term, document, position):
        return NotImplemented

    def search(self, query):
        return NotImplemented

class TfidfIndex(BaseIndex):
    def __init__(self):
        self.term_frequency = defaultdict(Counter)
        self.document_frequency = Counter()
        self.terms = set()
        self.documents = set()

    def insert(self, term, document, position):
        self.terms.add(term)
        self.documents.add(document)

        if term not in self.term_frequency[document]:
            self.document_frequency[term] += 1

        self.term_frequency[document][term] += 1

    def search(self, query):
        tokens = [t for t in tokenize_sentence(query) if t in self.terms]
        return sorted(self.documents, key=lambda d : reduce(mul, map(lambda t : self.term_frequency[d][t] / self.document_frequency[t], tokens)), reverse=True)[:5]