from collections import defaultdict, Counter

class BaseIndex(object):
    def insert(self, term, document, position):
        return NotImplemented

    def search(self, query):
        return NotImplemented

class TfidfIndex(BaseIndex):
    def __init__(self):
        self.term_frequency = defaultdict(Counter)
        self.document_frequency = Counter()

    def insert(self, term, document, position):
        if term not in self.term_frequency[document]:
            self.document_frequency[term] += 1

        self.term_frequency[document][term] += 1

    def search(self, query):
        return NotImplemented