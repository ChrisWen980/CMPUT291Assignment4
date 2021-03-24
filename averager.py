'''
Winter 2021 Cmput 291
Assignment 4, Part 1
Ahmad, Chris
'''
import sqlite3
import sys
import time

def check(n, c):
    '''
    enforces connected database has cardinality n.
    '''
    c.execute("select COUNT(*) from Parts")
    if c.fetchone()[0] != n:
        sys.exit("DATABASE SIZE INCORRECT! You are either using the wrong database or have corrupted the correct database.")

def avgEachDb(strng, numTimesDB1, numTimesDB2, numTimesDB3, numTimesDB4, numTimesDB5):
    '''
    inputs:
        strng: an sql query.
        numTimesDBX: the number of trials over which to avg running time of strng against X Database.

    returns:
        tuple where index i gives the average time for running strng against the i+1th database over numTimesDB(i+1) trials.
    '''

    ans = [0, 0, 0, 0, 0]

    def func(c):
        startTime = time.time()
        c.execute(strng)
        endTime = time.time()
        return(endTime - startTime)

    conn = sqlite3.connect('A4v100.db')
    c = conn.cursor()
    check(10**2, c)
    for _ in range(numTimesDB1):
        ans[0] += func(c)
    conn.close()

    conn = sqlite3.connect('A4v1k.db')
    c = conn.cursor()
    check(10**3, c)
    for _ in range(numTimesDB2):
        ans[1] += func(c)
    conn.close()

    conn = sqlite3.connect('A4v10k.db')
    c = conn.cursor()
    check(10**4, c)
    for _ in range(numTimesDB3):
        ans[2] += func(c)
    conn.close()

    conn = sqlite3.connect('A4v100k.db')
    c = conn.cursor()
    check(10**5, c)
    for _ in range(numTimesDB4):
        ans[3] += func(c)
    conn.close()

    conn = sqlite3.connect('A4v1M.db')
    c = conn.cursor()
    check(10**6, c)
    for _ in range(numTimesDB5):
        ans[4] += func(c)
    conn.close()

    ans[0] /= numTimesDB1
    ans[1] /= numTimesDB2
    ans[2] /= numTimesDB3
    ans[3] /= numTimesDB4
    ans[4] /= numTimesDB5

    return tuple(ans)

if __name__ == "__main__":
    pass