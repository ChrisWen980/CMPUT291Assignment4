'''
Winter 2021 Cmput 291
Assignment 4, Part 1
Ahmad, Chris

Query1: "SELECT partPrice FROM Parts WHERE partNumber = :code;"
Query2: "SELECT partPrice FROM Parts WHERE needsPart = :code;"
"code" variable is randomly selected from partNumber or needsPart of database executed on
'''
from averager import *

Q1Query = "SELECT partPrice FROM Parts WHERE partNumber = :code;"
Q2Query = "SELECT partPrice FROM Parts WHERE needsPart = :code;"
indexCreationStatement = "CREATE INDEX idxNeedsPart ON Parts (needsPart)"
Q1ColumnGenerateFrom = "partNumber"
Q2ColumnGenerateFrom = "needsPart"
Q1Num = 1
Q2Num = 2

if __name__ == "__main__":
    dropAllIndexes()
    avgEachDb(Q1Query,50,50,50,10,5,Q1ColumnGenerateFrom, Q1Num)
    avgEachDb(Q2Query,50,50,50,10,5,Q2ColumnGenerateFrom, Q2Num)
    makeIndex(indexCreationStatement)
    avgEachDb(Q1Query,50,50,50,10,5,Q1ColumnGenerateFrom, Q1Num)
    avgEachDb(Q2Query,50,50,50,10,5,Q2ColumnGenerateFrom, Q2Num)

