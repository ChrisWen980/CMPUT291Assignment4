'''
Winter 2021 Cmput 291
Assignment 4, Part 1
Ahmad, Chris
'''
from averager import *

Q1 = ["SELECT partPrice FROM Parts WHERE partNumber = :code;", "partNumber", 1]
Q2 = ["SELECT partPrice FROM Parts WHERE needsPart = :code;", "needsPart", 2]
indexCreationStatement = "CREATE INDEX idxNeedsPart ON Parts (needsPart)"

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDb(Q1[0],50,50,50,10,5,Q1[1], Q1[2])
    avgEachDb(Q2[0],50,50,50,10,5,Q2[1], Q2[2])
    makeIndex(indexCreationStatement)
    avgEachDb(Q1[0],50,50,50,10,5,Q1[1], Q1[2])
    avgEachDb(Q2[0],50,50,50,10,5,Q2[1], Q2[2])

