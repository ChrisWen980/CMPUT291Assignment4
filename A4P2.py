'''
Winter 2021 Cmput 291
Assignment 4, Part 2
Ahmad, Chris
'''
from averager import *

Q3Query = "SELECT AVG(partPrice) FROM Parts GROUP BY madeIn;"
indexCreationStatement = "CREATE INDEX idxMadeIn ON Parts (madeIn)"
Q3Num = 3

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDbSimple(Q3Query,100,100,100,100,100,Q3Num)
    makeIndex(indexCreationStatement)
    avgEachDbSimple(Q3Query,100,100,100,100,100,Q3Num)
