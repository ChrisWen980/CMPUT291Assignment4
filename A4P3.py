'''
Winter 2021 Cmput 291
Assignment 4, Part 3
Ahmad, Chris
'''
from averager import *

Q4Query = "SELECT MAX(partPrice) FROM Parts WHERE madeIn = :code;"
Q4ColumnGenerateFrom = "madeIn"
Q4Num = 4
indexCreationStatement = "CREATE INDEX idxQ4Optimize ON Parts (partPrice)"

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDb(Q4Query,50,50,50,10,5, Q4ColumnGenerateFrom, Q4Num)
    makeIndex(indexCreationStatement)
    avgEachDb(Q4Query,50,50,50,10,5, Q4ColumnGenerateFrom, Q4Num)