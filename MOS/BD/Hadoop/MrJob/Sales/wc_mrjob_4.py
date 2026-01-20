#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.step import MRStep
from mrjob.job import MRJob

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_truc)
        ]

    def mapper(self, _, line: str):  # ty:ignore[invalid-method-override]
        _, _, city, category, amount, payment_method = line.split("\t")
        if payment_method == "Cash" and category == "Women's Clothing":
            yield (city, float(amount))

    def reducer(self, word, counts):  # ty:ignore[invalid-method-override]
        yield None, (word, sum(counts))

    def reducer_truc(self, _, counts):
        yield max(counts, key=lambda x: x[1])

if __name__ == '__main__':
    MRWordCount.run()