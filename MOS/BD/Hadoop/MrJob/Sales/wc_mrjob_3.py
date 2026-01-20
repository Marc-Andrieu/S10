#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob

class MRWordCount(MRJob):
    def mapper(self, _, line: str):  # ty:ignore[invalid-method-override]
        _, _, city, _, amount, payment_method = line.split("\t")
        if city == "San Francisco":
            yield(payment_method, float(amount))

    def reducer(self, word, counts):  # ty:ignore[invalid-method-override]
        yield(word, sum(counts))

if __name__ == '__main__':
    MRWordCount.run()