import sys
import re
from porterStemmer import PorterStemmer
from collections import defaultdict
import copy

porter=PorterStemmer()

class QueryIndex:

    def __init__(self):
        self.index={}
        self.titleIndex={}
        #term frequencies
        self.tf={}
        #inverse document frequencies
        self.idf={}


    def intersectLists(self,lists):
        if len(lists)==0:
            return []
        #start intersecting from the smaller list
        lists.sort(key=len)
        return list(reduce(lambda x,y: set(x)&set(y),lists))
        
    
    def getStopwords(self):
        f=open(self.stopwordsFile, 'r')
        stopwords=[line.rstrip() for line in f]
        self.sw=dict.fromkeys(stopwords)
        f.close()
        

    def getTerms(self, line):
        line=line.lower()
        #put spaces instead of non-alphanumeric characters
        line=re.sub(r'[^a-z0-9 ]',' ',line) 
        line=line.split()
        line=[x for x in line if x not in self.sw]
        line=[ porter.stem(word, 0, len(word)-1) for word in line]
        return line
        
    
    def getPostings(self, terms):
        #all terms in the list are guaranteed to be in the index
        return [ self.index[term] for term in terms ]
