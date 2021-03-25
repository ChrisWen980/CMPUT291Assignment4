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

def checkDBSize(n, c):
    '''
    enforces connected database has cardinality n.
    '''
    c.execute("select COUNT(*) from Parts")
    if c.fetchone()[0] != n:
        sys.exit("DATABASE SIZE INCORRECT! You are either using the wrong database or have corrupted the correct database.")

def timeNeeded(strng, c, choice):
    '''
    returns time to run query "strng" against database c
    '''
    startTime = time.time()
    c.execute(strng,{'code': choice}) 
    endTime = time.time()
    return(endTime - startTime)

def timeNeededSimple(strng, c):
    startTime = time.time()
    c.execute(strng)
    endTime = time.time()
    return(endTime - startTime)


def avgEachDbSimple(strng, numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5, n):
    '''
    inputs:
        (string) strng: sql query
        (integer) numTimesDBX: the number of trials over which to avg running time of strng against X Database.
        (string) column: the column we randomly select from to get data to put into strng.

    returns:
        tuple where index i gives the average time for running strng against the i+1th database over numTimesDB(i+1) trials.
    '''

    dbList = ["A4v100.db", "A4v1k.db","A4v10k.db","A4v100k.db","A4v1M.db"]
    dbNumTimesList = [numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5]
    ans = [0, 0, 0, 0, 0]

    for i in range(len(dbList)):
        conn = sqlite3.connect(dbList[i])
        c = conn.cursor()
        dbSize = 10**(i+2)
        checkDBSize(dbSize, c)
        for _ in range(dbNumTimesList[i]):
            ans[i] += timeNeededSimple(strng, c)
        conn.close()
        ans[i] /= dbNumTimesList[i]
        print(f"{dbList[i]}: Ran Query {n} {dbNumTimesList[i]} times and got {ans[i]*1000} ms on average")

def avgEachDb(strng, numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5, column, n):
    '''
    inputs:
        (string) strng: sql query
        (integer) numTimesDBX: the number of trials over which to avg running time of strng against X Database.
        (string) column: the column we randomly select from to get data to put into strng.

    returns:
        tuple where index i gives the average time for running strng against the i+1th database over numTimesDB(i+1) trials.
    '''

    dbList = ["A4v100.db", "A4v1k.db","A4v10k.db","A4v100k.db","A4v1M.db"]
    dbNumTimesList = [numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5]
    ans = [0, 0, 0, 0, 0]

    for i in range(len(dbList)):
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