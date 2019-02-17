#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
 
import sys
from itertools import groupby
from operator import itemgetter
 
class Mapper:
   
    def run(self):
        data = self.readInput()
        for cur_id, follow in data:
            print('%s\t1' % follow)
 
    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 1)

class Reducer:
    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        s = 0
        c = 0
        for cur_follow, one in data:
            s += float(cur_follow)
            c += float(one)
        print(s/c)

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 1)

class Combiner:

    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        s = 0
        c = 0
        for cur_follow, one in data:
            s += float(cur_follow)
            c += float(one)
        print('%s\t%s' % (str(s), str(c)))

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 1)

if __name__ == "__main__":
    my_func = sys.argv[1]
    if my_func == "map":
        mapper = Mapper()
        mapper.run()
    elif my_func == "reduce":
        reducer = Reducer()
        reducer.run()
    elif my_func == "combine":
        combiner = Combiner()
        combiner.run()