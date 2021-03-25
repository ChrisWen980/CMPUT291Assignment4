'''
Winter 2021 Cmput 291
Assignment 4, Part 4
Ahmad, Chris
'''
from averager import *

Q5Query = "SELECT COUNT(p.partNumber) FROM Parts p WHERE NOT EXISTS (SELECT p.needsPart WHERE p.partNumber = p.needsPart);"
Q6Query = "SELECT COUNT(p.partNumber) FROM Parts p WHERE p.partNumber NOT IN (SELECT p.needsPart);"
Q5Num = 5
Q6Num = 6

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDbSimple(Q5Query,100,100,100,0,0, Q5Num)
    avgEachDbSimple(Q6Query,100,100,100,10,5, Q6Num)
    makeIndex("CREATE INDEX idxQ6Optimize ON Parts (partNumber = needsPart);")
    avgEachDbSimple(Q6Query,100,100,100,10,5, Q6Num)
    