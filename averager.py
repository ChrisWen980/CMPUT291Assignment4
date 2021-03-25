'''
Winter 2021 Cmput 291
Assignment 4, Part 1
Ahmad, Chris
'''
import sqlite3
import sys
import time
import random

def getChoiceList(column, c):
    '''
    gives a random element of column from database.
    '''
    c.execute(f"Select {column} from Parts")
    return c.fetchall()

def makeIndex(strrng):
    '''
    given SQL index creation statement, creates index for all databases.
    '''
    dbList = ["A4v100.db", "A4v1k.db", "A4v10k.db","A4v100k.db","A4v1M.db"]
    for db in dbList:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute(strrng)
        print(f"{db}: Index has been created.")
        conn.commit()
        conn.close()

def checkDBSize(n, c):
    '''
    enforces connected database has cardinality n.
    '''
    c.execute("select COUNT(*) from Parts")
    if c.fetchone()[0] != n:
        sys.exit("DATABASE SIZE INCORRECT! Possibilities: running from wrong directory, using wrong database, corrupted database.")

def timeNeeded(strng, c, choice):
    '''
    returns time to run query "strng" against database c
    '''
    startTime = time.time()
    c.execute(strng,{'code': choice}) 
    endTime = time.time()
    return(endTime - startTime)

def timeNeededSimple(strng, c):
    '''
    same as timeNeeded() except the query is independent of any randomly generated component so choice is not required.
    '''
    startTime = time.time()
    c.execute(strng)
    endTime = time.time()
    return(endTime - startTime)

def dropAllIndexes():
    '''
    goes through each database and removes all possible indexes, assuming names of indexes haven't been tampered with.
    '''
    dbList = ["A4v100.db", "A4v1k.db", "A4v10k.db","A4v100k.db","A4v1M.db"]
    for db in dbList:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        idxList = ["idxMadeIn", "idxNeedsPart", "idxQ4Optimize", "idxQ6Optimize"]
        for idx in idxList:
            c.execute(f"DROP INDEX IF EXISTS {idx}")
        print(f"{db}: All indexes have been dropped, if any existed.")
        conn.commit()
        conn.close()

def avgEachDb(strng, numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5, column, n):
    '''
    inputs:
        (string) strng: sql query
        (integer) numTimesDBX: the number of trials over which to avg running time of strng against X Database.
        (string) column: the column we randomly select from to get data to put into strng.
        (integer) n: query number for print formatting purposes.

    returns:
        nothing, but prints all salient information.
    '''

    dbList = ["A4v100.db", "A4v1k.db","A4v10k.db","A4v100k.db","A4v1M.db"]
    dbNumTimesList = [numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5]
    ans = [0, 0, 0, 0, 0]

    for i in range(len(dbList)):
        if not dbNumTimesList[i]:
            print(f"Skipped {dbList[i]} as {dbNumTimesList[i]} iterations performed")
            continue
        conn = sqlite3.connect(dbList[i])
        c = conn.cursor()
        dbSize = 10**(i+2)
        checkDBSize(dbSize, c)
        optionList = getChoiceList(column, c)
        for _ in range(dbNumTimesList[i]):
            choice = random.choice(optionList)[0]
            ans[i] += timeNeeded(strng, c, choice)
        conn.close()
        ans[i] /= dbNumTimesList[i]
        print(f"{dbList[i]}: Ran Query {n} {dbNumTimesList[i]} times and got {ans[i]*1000} ms on average")


def avgEachDbSimple(strng, numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5, n):
    '''
    same as avgEachDb(), except we do not require column as the query statement does not require a randomly generated component.
    '''

    dbList = ["A4v100.db", "A4v1k.db","A4v10k.db","A4v100k.db","A4v1M.db"]
    dbNumTimesList = [numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5]
    ans = [0, 0, 0, 0, 0]

    for i in range(len(dbList)):
        if not dbNumTimesList[i]:
            print(f"Skipped {dbList[i]} as {dbNumTimesList[i]} iterations performed")
            continue
        conn = sqlite3.connect(dbList[i])
        c = conn.cursor()
        dbSize = 10**(i+2)
        checkDBSize(dbSize, c)
        for _ in range(dbNumTimesList[i]):
            ans[i] += timeNeededSimple(strng, c)
        conn.close()
        ans[i] /= dbNumTimesList[i]
        print(f"{dbList[i]}: Ran Query {n} {dbNumTimesList[i]} times and got {ans[i]*1000} ms on average")

if __name__ ==  "__main__":
    dropAllIndexes()