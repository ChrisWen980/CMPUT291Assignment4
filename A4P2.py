'''
Winter 2021 Cmput 291
Assignment 4, Part 2
Ahmad, Chris
'''
from averager import *

Q3 = ["SELECT AVG(partPrice) FROM Parts GROUP BY madeIn;", 3]
indexCreationStatement = "CREATE INDEX idxMadeIn ON Parts (madeIn)"

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDbSimple(Q3[0],100,100,100,100,100,Q3[1])
    makeIndex(indexCreationStatement)
    avgEachDbSimple(Q3[0],100,100,100,100,100,Q3[1])
