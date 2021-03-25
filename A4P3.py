'''
Winter 2021 Cmput 291
Assignment 4, Part 3
Ahmad, Chris

Query4 = "SELECT MAX(partPrice) FROM Parts WHERE madeIn = :code;"
"code" is randomly sampled from column madeIn from the database the query is executed on.
indexCreationStatement = "CREATE INDEX idxQ4Optimize ON Parts (partPrice)"
'''
from averager import *

Q4Query = "SELECT MAX(partPrice) FROM Parts WHERE madeIn = :code;"
indexCreationStatement = "CREATE INDEX idxQ4Optimize ON Parts (partPrice)"
Q4ColumnGenerateFrom = "madeIn"
Q4Num = 4

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDb(Q4Query,50,50,50,10,5,Q4ColumnGenerateFrom, Q4Num)
    makeIndex(indexCreationStatement)
    avgEachDb(Q4Query,50,50,50,10,5,Q4ColumnGenerateFrom, Q4Num)