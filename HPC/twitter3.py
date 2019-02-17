#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
 
import sys

class Mapper:
    def run(self):
        data = self.readInput()
        for cur_id, follow in data:
            print('%d\t%d' % (int(cur_id), int(follow)))
 
    def readInput(self):
        for line in sys.stdin:
            yield line.encode("utf8").strip().split('\t', 1)

class Reducer:
    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        i = 1
        for cur_id, follow in data:
            if i <= 50:
                print("%s\t%s" % (cur_id, follow))
            i += 1

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t')

class Combiner:
    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        i = 1
        for cur_id, follow in data:
            if i <= 50:
                print("%s\t%s" % (cur_id, follow))
            i += 1

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t')

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
