#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
 
import sys
from itertools import groupby
from operator import itemgetter
 
class Mapper:
   
    def run(self):
        data = self.readInput()
        for cur_id, sub in data:
            print('%s\t1' % cur_id)
 
    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 1)

class Reducer:
    def run(self):
        sys.stderr.write('reporter:status:Reducer started\n')
        data = self.readInput()
        last_id = -99
        last_zn = 0
        for cur_id, one in data:
            if last_id == int(cur_id):
                last_zn += int(one)
            else:
                if last_id != -99:
                    print('%s\t%s' % (last_id, last_zn))
                last_id = int(cur_id)
                last_zn = int(one)
        print('%s\t%s' % (last_id, last_zn))

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t',1)

class Combiner:

    def run(self):
        sys.stderr.write('reporter:status:combiner started\n')
        data = self.readInput()
        last_id = -99
        last_count = 0
        for cur_id, one in data:
            if last_id == int(cur_id):
                last_count += int(one)
            else:
                if last_id != -99:
                    print('%s\t%s' % (last_id, last_count))
                last_id = int(cur_id)
                last_count = int(one)
        print('%s\t%s' % (last_id, last_count))
        sys.stderr.write('reporter:status:combiner Finished\n')

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