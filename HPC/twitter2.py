#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
 
import sys
from math import log10
class Mapper:
    def run(self):
        data = self.readInput()
        for cur_id, follow1 in data:
            follow = int(follow1)
            if follow == 1:
                group = 0
            else:
                group = int(log10(follow-1))
            print('%d\t1' % group)
 
    def readInput(self):
        for line in sys.stdin:
            yield line.encode("utf8").strip().split('\t', 1)

class Reducer:
    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        last_group = -1
        last_count = 0
        for group1, one in data:
            group = int(group1)
            if last_group == group:
                last_count += int(one)
            else:
                if last_group != -1:
                    print(self.makestring(last_group)+'\t'+str(last_count))
                last_group = group
                last_count = int(one)
        print(self.makestring(last_group)+'\t'+str(last_count))

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 1)

    def makestring(self, k):
        if k == 0:
            s = "["
        else:
            s = "("
        s = s + str(10**k)+", " + str(10**(k+1))+"]"
        return s

class Combiner:
    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        last_group = -1
        last_count = 0
        for group1, one in data:
            group = int(group1)
            if last_group == group:
                last_count += int(one)
            else:
                if last_group != -1:
                    print(str(last_group)+'\t'+str(last_count))
                last_group = group
                last_count = int(one)
        print(str(last_group)+'\t'+str(last_count))

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
