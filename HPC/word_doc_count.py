#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# cat data.txt | python bigram-count.py map ru | sort -k1,1 | python bigram-count.py reduce > output.txt
#
import sys
import re
from itertools import groupby
from operator import itemgetter

class Mapper:

    re_en = re.compile(ur"[a-z]+")
    re_ru = re.compile(ur"[а-яё]+")

    def __init__(self, lang):
        if lang == "en":
            self.re = Mapper.re_en
        else:
            self.re = Mapper.re_ru
        self.results = {}

    def run(self):
        doc_count = 0
        data = self.readInput()
        for docid, contents in data:
            text = contents.lower()
            word_count = 0
            for match in self.re.finditer(text):
                word = match.group(0)
                print(word, docid, 1)
            sys.stderr.write("reporter:counter:MyCounters,InputWords,%d\n" % word_count)
            doc_count += 1
            if doc_count % 1000 == 0:
                self.emitResults()
                sys.stderr.write("reporter:status:Processed %d documents\n" % doc_count)
        
        self.emitResults()

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 1)

    def addResult(self, w1, w2, one):
        if len(w1) > 2 and len(w2) > 2:
            if w1 not in self.results:
                self.results[w1] = {}
            w1_counts = self.results[w1]
            if w2 in w1_counts:
                w1_counts[w2] += one
            else:
                w1_counts[w2] = one

    def emitResults(self):
        for w1, counts in self.results.iteritems():
            for w2, count in counts.iteritems():
                print ('%s\t%s\t%d' % (w1, w2, count)).encode('utf-8')


class Reducer:
    def run(self):
        data = self.readInput()
        cur_word = None
        cur_docid = None
        cur_count = 0
        s = ""
        i = 0
        for w1, w2, count in data:
            count = int(count)
            if cur_word == w1 and cur_docid == w2:
                cur_count += count
            else:
                if cur_word == w1:
                    if i <= 20:
                        s += "\t" + cur_docid + ":" + str(cur_count)
                else:
                    if cur_word:
                        s += "\t" + cur_docid + ":" + str(cur_count)
                        print ('%s' % s.encode('utf-8'))
                        i = 0
                    cur_word = w1
                    s = w1
                cur_docid = w2
                cur_count = count
                i += 1
        print ('%s' % s.encode('utf-8'))

    def readInput(self):
        for line in sys.stdin:
            yield unicode(line, 'utf8').strip().split('\t', 2)


if __name__ == "__main__":
    mr_func = sys.argv[1]
    if mr_func == "map":
        lang = sys.argv[2]
        mapper = Mapper(lang)
        mapper.run()
    elif mr_func == "reduce":
        reducer = Reducer()
        reducer.run()


        '''
-D mapred.partitioner.class=org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -D mapreduce.map.output.key.field.separator=\t -D mapreduce.partition.keypartitioner.options=-k1,2 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator -D mapreduce.partition.keycomparator.options='-k1,1 -k3,3nr -k2,2'

                '''