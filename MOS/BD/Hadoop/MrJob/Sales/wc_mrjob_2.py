#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob

class MRWordCount(MRJob):
    def mapper(self, _, line: str):  # ty:ignore[invalid-method-override]
        _, _, _, category, amount, _ = line.split("\t")
        yield(category, float(amount))

    def reducer(self, word, counts):  # ty:ignore[invalid-method-override]
        yield(word, sum(counts))

if __name__ == '__main__':
    MRWordCount.run()