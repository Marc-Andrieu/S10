#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from statistics import mean
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
        _, _, _, _, amount, payment_method = line.split("\t")
        yield (payment_method, float(amount))

    def reducer(self, word, counts):  # ty:ignore[invalid-method-override]
        yield None, (word, mean(counts))
    
    def reducer_truc(self, _, counts):
        yield max(counts, key=lambda x: x[1])

if __name__ == '__main__':
    MRWordCount.run()